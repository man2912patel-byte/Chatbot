import SpriteKit

class GameScene: SKScene {
    
    // MARK: - Player
    
    var mario: SKSpriteNode!
    
    var marioX: CGFloat = 50
    var marioY: CGFloat = 0
    
    var isJumping = false
    
    
    // MARK: - Obstacle
    
    var obstacle: SKSpriteNode!
    
    var obstacleX: CGFloat = 800
    
    
    // MARK: - Game
    
    var score = 0
    var gameRunning = true
    
    
    // MARK: - Labels
    
    var scoreLabel: SKLabelNode!
    var gameOverLabel: SKLabelNode!
    var restartLabel: SKLabelNode!
    
    
    // MARK: - Buttons
    
    var leftButton: SKLabelNode!
    var rightButton: SKLabelNode!
    var upButton: SKLabelNode!
    
    
    // MARK: - Game Start
    
    override func didMove(to view: SKView) {
        
        createGame()
    }
    
    
    // MARK: - Create Game
    
    func createGame() {
        
        removeAllChildren()
        
        score = 0
        marioX = 50
        marioY = 0
        obstacleX = size.width
        gameRunning = true
        isJumping = false
        
        
        // MARK: Background
        
        backgroundColor = .cyan
        
        
        // MARK: Ground
        
        let ground = SKSpriteNode(
            color: .green,
            size: CGSize(
                width: size.width,
                height: 50
            )
        )
        
        ground.position = CGPoint(
            x: size.width / 2,
            y: 25
        )
        
        ground.zPosition = 1
        
        addChild(ground)
        
        
        // MARK: Mario
        
        mario = SKSpriteNode(
            color: .red,
            size: CGSize(
                width: 50,
                height: 50
            )
        )
        
        mario.position = CGPoint(
            x: marioX,
            y: 50 + marioY
        )
        
        mario.zPosition = 5
        
        addChild(mario)
        
        
        // MARK: Obstacle
        
        obstacle = SKSpriteNode(
            color: .brown,
            size: CGSize(
                width: 40,
                height: 70
            )
        )
        
        obstacle.position = CGPoint(
            x: obstacleX,
            y: 50
        )
        
        obstacle.zPosition = 5
        
        addChild(obstacle)
        
        
        // MARK: Score
        
        scoreLabel = SKLabelNode(
            fontNamed: "Menlo-Bold"
        )
        
        scoreLabel.text = "Score : 0"
        scoreLabel.fontSize = 22
        scoreLabel.fontColor = .black
        
        scoreLabel.horizontalAlignmentMode = .left
        
        scoreLabel.position = CGPoint(
            x: 20,
            y: size.height - 40
        )
        
        scoreLabel.zPosition = 10
        
        addChild(scoreLabel)
        
        
        // MARK: Controls
        
        createControls()
        
        
        // MARK: Game Over
        
        createGameOver()
    }
    
    
    // MARK: - Controls
    
    func createControls() {
        
        // LEFT
        
        leftButton = SKLabelNode(
            fontNamed: "Arial-BoldMT"
        )
        
        leftButton.text = "⬅️"
        leftButton.fontSize = 35
        
        leftButton.position = CGPoint(
            x: size.width - 100,
            y: 30
        )
        
        leftButton.zPosition = 20
        
        addChild(leftButton)
        
        
        // RIGHT
        
        rightButton = SKLabelNode(
            fontNamed: "Arial-BoldMT"
        )
        
        rightButton.text = "➡️"
        rightButton.fontSize = 35
        
        rightButton.position = CGPoint(
            x: size.width - 40,
            y: 30
        )
        
        rightButton.zPosition = 20
        
        addChild(rightButton)
        
        
        // UP
        
        upButton = SKLabelNode(
            fontNamed: "Arial-BoldMT"
        )
        
        upButton.text = "⬆️"
        upButton.fontSize = 35
        
        upButton.position = CGPoint(
            x: size.width / 2,
            y: 30
        )
        
        upButton.zPosition = 20
        
        addChild(upButton)
    }
    
    
    // MARK: - Game Over
    
    func createGameOver() {
        
        gameOverLabel = SKLabelNode(
            fontNamed: "Arial-BoldMT"
        )
        
        gameOverLabel.text = "GAME OVER"
        gameOverLabel.fontSize = 45
        gameOverLabel.fontColor = .white
        
        gameOverLabel.position = CGPoint(
            x: size.width / 2,
            y: size.height / 2 + 30
        )
        
        gameOverLabel.zPosition = 50
        
        gameOverLabel.isHidden = true
        
        addChild(gameOverLabel)
        
        
        restartLabel = SKLabelNode(
            fontNamed: "Arial-BoldMT"
        )
        
        restartLabel.text = "🔄 TAP TO RESTART"
        restartLabel.fontSize = 22
        restartLabel.fontColor = .white
        
        restartLabel.position = CGPoint(
            x: size.width / 2,
            y: size.height / 2 - 30
        )
        
        restartLabel.zPosition = 50
        
        restartLabel.isHidden = true
        
        addChild(restartLabel)
    }
    
    
    // MARK: - Game Loop
    
    override func update(_ currentTime: TimeInterval) {
        
        if gameRunning == false {
            return
        }
        
        
        // Move obstacle
        
        obstacleX -= 5
        
        obstacle.position.x = obstacleX
        
        
        // Obstacle passed
        
        if obstacleX < -40 {
            
            obstacleX = size.width + 40
            
            score += 1
            
            scoreLabel.text = "Score : \(score)"
        }
        
        
        // Collision
        
        if mario.frame.intersects(obstacle.frame) {
            
            gameOver()
        }
    }
    
    
    // MARK: - Move Right
    
    func moveRight() {
        
        if gameRunning == false {
            return
        }
        
        marioX += 10
        
        if marioX >= size.width - 50 {
            marioX = size.width - 50
        }
        
        mario.position.x = marioX
    }
    
    
    // MARK: - Move Left
    
    func moveLeft() {
        
        if gameRunning == false {
            return
        }
        
        marioX -= 10
        
        if marioX <= 25 {
            marioX = 25
        }
        
        mario.position.x = marioX
    }
    
    
    // MARK: - Jump
    
    func jump() {
        
        if isJumping || gameRunning == false {
            return
        }
        
        isJumping = true
        
        
        // Jump UP
        
        let jumpUp = SKAction.moveBy(
            x: 0,
            y: 140,
            duration: 0.3
        )
        
        
        // Jump DOWN
        
        let jumpDown = SKAction.moveBy(
            x: 0,
            y: -140,
            duration: 0.3
        )
        
        
        // Finish
        
        let finishJump = SKAction.run {
            
            self.isJumping = false
        }
        
        
        let jumpSequence = SKAction.sequence([
            jumpUp,
            jumpDown,
            finishJump
        ])
        
        mario.run(jumpSequence)
    }
    
    
    // MARK: - Game Over
    
    func gameOver() {
        
        gameRunning = false
        
        gameOverLabel.isHidden = false
        restartLabel.isHidden = false
    }
    
    
    // MARK: - Touch
    
    override func touchesBegan(
        _ touches: Set<UITouch>,
        with event: UIEvent?
    ) {
        
        guard let touch = touches.first else {
            return
        }
        
        let location = touch.location(in: self)
        
        
        // Restart
        
        if gameRunning == false {
            
            if restartLabel.contains(location) {
                
                createGame()
            }
            
            return
        }
        
        
        // Left button
        
        if leftButton.contains(location) {
            
            moveLeft()
        }
        
        
        // Right button
        
        else if rightButton.contains(location) {
            
            moveRight()
        }
        
        
        // Jump button
        
        else if upButton.contains(location) {
            
            jump()
        }
    }
    
    
    // MARK: - Keyboard
    
    override func keyDown(
        with event: NSEvent
    ) {
        
        if gameRunning == false {
            return
        }
        
        
        if event.keyCode == 123 {
            moveLeft()
        }
        
        
        if event.keyCode == 124 {
            moveRight()
        }
        
        
        if event.keyCode == 126 ||
           event.keyCode == 49 {
            
            jump()
        }
    }
}
