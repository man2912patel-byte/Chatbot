import SwiftUI

struct ContentView: View {
    
    // MARK: - Player
    
    @State private var playerX: CGFloat = 100
    @State private var playerY: CGFloat = 400
    
    @State private var velocityY: CGFloat = 0
    @State private var isJumping = false
    
    // MARK: - Game
    
    @State private var score = 0
    @State private var lives = 3
    @State private var gameOver = false
    
    // Game timer
    let timer = Timer.publish(
        every: 0.02,
        on: .main,
        in: .common
    ).autoconnect()
    
    var body: some View {
        
        GeometryReader { screen in
            
            ZStack {
                
                // MARK: Background
                
                LinearGradient(
                    colors: [.cyan.opacity(0.5), .blue.opacity(0.2)],
                    startPoint: .top,
                    endPoint: .bottom
                )
                .ignoresSafeArea()
                
                
                // Clouds
                
                Text("☁️")
                    .font(.system(size: 60))
                    .position(x: 80, y: 100)
                
                Text("☁️")
                    .font(.system(size: 50))
                    .position(x: 300, y: 160)
                
                
                // MARK: Score
                
                VStack {
                    
                    HStack {
                        
                        Text("⭐ \(score)")
                            .font(.headline)
                        
                        Spacer()
                        
                        Text("❤️ \(lives)")
                            .font(.headline)
                    }
                    .padding()
                    
                    Spacer()
                }
                
                
                // MARK: Ground
                
                Rectangle()
                    .fill(.green)
                    .frame(
                        width: screen.size.width,
                        height: 40
                    )
                    .position(
                        x: screen.size.width / 2,
                        y: screen.size.height - 20
                    )
                
                
                // MARK: Platform 1
                
                Rectangle()
                    .fill(.brown)
                    .frame(width: 130, height: 20)
                    .position(x: 150, y: 450)
                
                
                // MARK: Platform 2
                
                Rectangle()
                    .fill(.brown)
                    .frame(width: 130, height: 20)
                    .position(x: 330, y: 350)
                
                
                // MARK: Platform 3
                
                Rectangle()
                    .fill(.brown)
                    .frame(width: 120, height: 20)
                    .position(x: 100, y: 270)
                
                
                // MARK: Coin
                
                Text("🪙")
                    .font(.system(size: 35))
                    .position(x: 150, y: 410)
                
                
                // MARK: Enemy
                
                Text("👾")
                    .font(.system(size: 40))
                    .position(x: 300, y: screen.size.height - 70)
                
                
                // MARK: Player
                
                Text("🧑")
                    .font(.system(size: 45))
                    .position(
                        x: playerX,
                        y: playerY
                    )
                
                
                // MARK: Controls
                
                VStack {
                    
                    Spacer()
                    
                    HStack(spacing: 20) {
                        
                        // LEFT
                        Button {
                            playerX -= 20
                        } label: {
                            Text("⬅️")
                                .font(.system(size: 35))
                                .frame(width: 70, height: 60)
                                .background(.white.opacity(0.8))
                                .cornerRadius(15)
                        }
                        
                        
                        // JUMP
                        Button {
                            jump()
                        } label: {
                            Text("⬆️")
                                .font(.system(size: 35))
                                .frame(width: 70, height: 60)
                                .background(.white.opacity(0.8))
                                .cornerRadius(15)
                        }
                        
                        
                        // RIGHT
                        Button {
                            playerX += 20
                        } label: {
                            Text("➡️")
                                .font(.system(size: 35))
                                .frame(width: 70, height: 60)
                                .background(.white.opacity(0.8))
                                .cornerRadius(15)
                        }
                    }
                    .padding(.bottom, 20)
                }
                
                
                // MARK: Game Over
                
                if gameOver {
                    
                    Color.black.opacity(0.6)
                        .ignoresSafeArea()
                    
                    VStack(spacing: 20) {
                        
                        Text("GAME OVER")
                            .font(.largeTitle)
                            .fontWeight(.bold)
                            .foregroundStyle(.white)
                        
                        Text("Score: \(score)")
                            .font(.title2)
                            .foregroundStyle(.white)
                        
                        Button("Restart") {
                            restartGame()
                        }
                        .padding()
                        .frame(width: 150)
                        .background(.blue)
                        .foregroundStyle(.white)
                        .cornerRadius(12)
                    }
                }
            }
            
            // MARK: Game Loop
            
            .onReceive(timer) { _ in
                updateGame(screenHeight: screen.size.height)
            }
        }
    }
    
    
    // MARK: - Jump
    
    func jump() {
        
        if !isJumping {
            
            velocityY = -15
            isJumping = true
        }
    }
    
    
    // MARK: - Game Update
    
    func updateGame(screenHeight: CGFloat) {
        
        if gameOver {
            return
        }
        
        // Gravity
        velocityY += 0.6
        
        // Move player
        playerY += velocityY
        
        
        // Ground collision
        
        let groundY = screenHeight - 65
        
        if playerY >= groundY {
            
            playerY = groundY
            velocityY = 0
            isJumping = false
        }
        
        
        // Keep player on screen
        
        if playerX < 25 {
            playerX = 25
        }
        
        if playerX > 375 {
            playerX = 375
        }
    }
    
    
    // MARK: - Restart
    
    func restartGame() {
        
        playerX = 100
        playerY = 400
        
        velocityY = 0
        isJumping = false
        
        score = 0
        lives = 3
        
        gameOver = false
    }
}


#Preview {
    ContentView()
}
