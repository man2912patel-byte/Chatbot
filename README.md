import SwiftUI

struct ContentView: View {
    
    // Player
    @State private var playerX: CGFloat = 100
    @State private var playerY: CGFloat = 500
    
    // Jump
    @State private var isJumping = false
    
    // Game
    @State private var score = 0
    @State private var gameOver = false
    
    var body: some View {
        
        ZStack {
            
            // Background
            LinearGradient(
                colors: [.blue.opacity(0.3), .cyan.opacity(0.1)],
                startPoint: .top,
                endPoint: .bottom
            )
            .ignoresSafeArea()
            
            
            // Score
            VStack {
                HStack {
                    
                    Text("⭐ \(score)")
                        .font(.title3)
                        .bold()
                    
                    Spacer()
                    
                    Text("Mini Game")
                        .font(.headline)
                    
                }
                .padding()
                
                Spacer()
            }
            
            
            // Cloud
            Text("☁️")
                .font(.system(size: 60))
                .position(x: 80, y: 130)
            
            
            // Second Cloud
            Text("☁️")
                .font(.system(size: 50))
                .position(x: 320, y: 180)
            
            
            // Platform
            Rectangle()
                .fill(.brown)
                .frame(width: 140, height: 20)
                .position(x: 250, y: 430)
            
            
            // Coin
            Button {
                score += 1
            } label: {
                Text("🪙")
                    .font(.system(size: 40))
            }
            .position(x: 250, y: 380)
            
            
            // Ground
            Rectangle()
                .fill(.green)
                .frame(height: 80)
                .position(x: 200, y: 750)
            
            
            // Player
            Text("🧑")
                .font(.system(size: 50))
                .position(
                    x: playerX,
                    y: playerY
                )
            
            
            // Controls
            VStack {
                
                Spacer()
                
                HStack(spacing: 15) {
                    
                    // LEFT
                    Button {
                        moveLeft()
                    } label: {
                        Text("⬅️")
                            .font(.system(size: 30))
                            .frame(width: 65, height: 55)
                            .background(.white)
                            .cornerRadius(15)
                    }
                    
                    
                    // JUMP
                    Button {
                        jump()
                    } label: {
                        Text("⬆️")
                            .font(.system(size: 30))
                            .frame(width: 65, height: 55)
                            .background(.white)
                            .cornerRadius(15)
                    }
                    
                    
                    // RIGHT
                    Button {
                        moveRight()
                    } label: {
                        Text("➡️")
                            .font(.system(size: 30))
                            .frame(width: 65, height: 55)
                            .background(.white)
                            .cornerRadius(15)
                    }
                }
                
                .padding(.bottom, 20)
            }
        }
    }
    
    
    // MARK: - Move Left
    
    func moveLeft() {
        
        withAnimation {
            playerX -= 30
        }
        
        if playerX < 30 {
            playerX = 30
        }
    }
    
    
    // MARK: - Move Right
    
    func moveRight() {
        
        withAnimation {
            playerX += 30
        }
        
        if playerX > 370 {
            playerX = 370
        }
    }
    
    
    // MARK: - Jump
    
    func jump() {
        
        if isJumping {
            return
        }
        
        isJumping = true
        
        // Go up
        withAnimation(.easeOut(duration: 0.3)) {
            playerY = 350
        }
        
        // Come down
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.3) {
            
            withAnimation(.easeIn(duration: 0.3)) {
                playerY = 500
            }
            
            isJumping = false
        }
    }
}


#Preview {
    ContentView()
}
