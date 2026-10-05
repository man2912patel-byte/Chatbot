import UIKit
import PlaygroundSupport
import SpriteKit

class GameScene: SKScene {
    
    let player = SKSpriteNode(
        color: .red,
        size: CGSize(width: 40, height: 40)
    )
    
    let obstacle = SKSpriteNode(
        color: .brown,
        size: CGSize(width: 30, height: 60)
    )
    
    var score = 0
    var scoreLabel = SKLabelNode()
    var gameOver = false
    
    override func didMove(to view: SKView) {
        
        backgroundColor = .cyan
        
        // Player
        player.position = CGPoint(x: 80, y: 100)
        addChild(player)
        
        // Ground
        let ground = SKSpriteNode(
            color: .green,
            size: CGSize(width: 500, height: 40)
        )
        
        ground.position = CGPoint(x: 250, y: 20)
        addChild(ground)
        
        // Obstacle
        obstacle.position = CGPoint(x: 450, y: 80)
        addChild(obstacle)
        
        // Score
        scoreLabel.text = "Score: 0"
        scoreLabel.fontSize = 25
        scoreLabel.fontColor = .black
        scoreLabel.position = CGPoint(x: 80, y: 300)
        
        addChild(scoreLabel)
    }
    
    override func update(_ currentTime: TimeInterval) {
        
        if gameOver {
            return
        }
        
        // Move obstacle
        obstacle.position.x -= 5
        
        // Obstacle goes back
        if obstacle.position.x < -30 {
            
            obstacle.position.x = 450
            
            score += 1
            
            scoreLabel.text = "Score: \(score)"
        }
        
        // Collision
        if player.frame.intersects(obstacle.frame) {
            
            gameOver = true
            
            scoreLabel.text = "GAME OVER"
        }
    }
    
    // Jump
    func jump() {
        
        if gameOver {
            return
        }
        
        let up = SKAction.moveBy(
            x: 0,
            y: 100,
            duration: 0.3
        )
        
        let down = SKAction.moveBy(
            x: 0,
            y: -100,
            duration: 0.3
        )
        
        player.run(
            SKAction.sequence([
                up,
                down
            ])
        )
    }
}


// Create scene

let scene = GameScene()

scene.size = CGSize(
    width: 500,
    height: 350
)

scene.scaleMode = .aspectFit


// Playground live view

let view = SKView(
    frame: CGRect(
        x: 0,
        y: 0,
        width: 500,
        height: 350
    )
)

view.presentScene(scene)

PlaygroundPage.current.liveView = view
