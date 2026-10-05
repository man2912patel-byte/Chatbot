import SwiftUI

struct ContentView: View {
    
    // MARK: - Player
    
    @State private var playerX: CGFloat = 80
    @State private var playerY: CGFloat = 520
    
    @State private var isJumping = false
    
    
    // MARK: - Coin
    
    @State private var coinX: CGFloat = 250
    @State private var coinY: CGFloat = 520
    @State private var coinVisible = true
    
    
    // MARK: - Game
    
    @State private var score = 0
    
    
    var body: some View {
        
        ZStack {
            
            // MARK: Background
            
            LinearGradient(
                colors: [
                    .cyan.opacity(0.4),
                    .blue.opacity(0.15)
                ],
                startPoint: .top,
                endPoint: .bottom
            )
            .ignoresSafeArea()
            
            
            // MARK: Score
            
            VStack {
                
                HStack {
                    
                    Text("⭐ Score: \(score)")
                        .font(.title3)
                        .fontWeight(.bold)
                    
                    Spacer()
                    
                    Text("Mini Game")
                        .font(.headline)
                }
                .padding()
                
                Spacer()
            }
            
            
            // MARK: Clouds
            
            Text("☁️")
                .font(.system(size: 55))
                .position(x: 80, y: 130)
            
            Text("☁️")
                .font(.system(size: 45))
                .position(x: 320, y: 170)
            
            
            // MARK: Platform
            
            Rectangle()
                .fill(.brown)
                .frame(width: 150, height: 20)
                .position(x: 250, y: 430)
            
            
            // MARK: Coin
            
            if coinVisible {
                
                Text("🪙")
                    .font(.system(size: 40))
                    .position(
                        x: coinX,
                        y: coinY
                    )
            }
            
            
            // MARK: Ground
            
            Rectangle()
                .fill(.green)
                .frame(
                    width: 400,
                    height: 80
                )
                .position(
                    x: 200,
                    y: 750
                )
            
            
            // MARK: Player
            
            Text("🧑")
                .font(.system(size: 50))
                .position(
                    x: playerX,
                    y: playerY
                )
            
            
            // MARK: Controls
            
            VStack {
                
                Spacer()
                
                HStack(spacing: 15) {
                    
                    // LEFT
                    
                    Button {
                        moveLeft()
                    } label: {
                        
                        Text("⬅️")
                            .font(.system(size: 30))
                            .frame(
                                width: 65,
                                height: 55
                            )
                            .background(.white)
                            .cornerRadius(15)
                    }
                    
                    
                    // JUMP
                    
                    Button {
                        jump()
                    } label: {
                        
                        Text("⬆️")
                            .font(.system(size: 30))
                            .frame(
                                width: 65,
                                height: 55
                            )
                            .background(.white)
                            .cornerRadius(15)
                    }
                    
                    
                    // RIGHT
                    
                    Button {
                        moveRight()
                    } label: {
                        
                        Text("➡️")
                            .font(.system(size: 30))
                            .frame(
                                width: 65,
                                height: 55
                            )
                            .background(.white)
                            .cornerRadius(15)
                    }
                }
                
                
                // RESET
                
                Button("Reset Game") {
                    resetGame()
                }
                .padding(.top, 10)
                .foregroundStyle(.red)
                
                .padding(.bottom, 15)
            }
        }
    }
    
    
    // MARK: - Move Left
    
    func moveLeft() {
        
        withAnimation {
            playerX -= 30
        }
        
        // Screen boundary
        
        if playerX < 30 {
            playerX = 30
        }
        
        checkCoin()
    }
    
    
    // MARK: - Move Right
    
    func moveRight() {
        
        withAnimation {
            playerX += 30
        }
        
        // Screen boundary
        
        if playerX > 370 {
            playerX = 370
        }
        
        checkCoin()
    }
    
    
    // MARK: - Jump
    
    func jump() {
        
        // Already jumping?
        
        if isJumping {
            return
        }
        
        isJumping = true
        
        
        // Player goes UP
        
        withAnimation(.easeOut(duration: 0.3)) {
            playerY = 350
        }
        
        // Player comes DOWN
        
        DispatchQueue.main.asyncAfter(
            deadline: .now() + 0.3
        ) {
            
            withAnimation(.easeIn(duration: 0.3)) {
                playerY = 520
            }
            
            isJumping = false
            
            checkCoin()
        }
    }
    
    
    // MARK: - Coin Collision
    
    func checkCoin() {
        
        // Check distance between player and coin
        
        let xDistance = abs(playerX - coinX)
        let yDistance = abs(playerY - coinY)
        
        if xDistance < 50 && yDistance < 50 {
            
            if coinVisible {
                
                score += 1
                
                coinVisible = false
            }
        }
    }
    
    
    // MARK: - Reset
    
    func resetGame() {
        
        playerX = 80
        playerY = 520
        
        coinX = 250
        coinY = 520
        
        coinVisible = true
        
        score = 0
        
        isJumping = false
    }
}


#Preview {
    ContentView()
}
