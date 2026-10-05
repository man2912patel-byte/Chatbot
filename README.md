import SwiftUI

struct ContentView: View {
    
    @State private var playerX = 0
    @State private var score = 0
    @State private var coinVisible = true
    @State private var jumping = false
    
    var body: some View {
        
        VStack {
            
            // Score
            HStack {
                Text("⭐ Score: \(score)")
                    .font(.title3)
                    .bold()
                
                Spacer()
                
                Text("Mini Game")
                    .bold()
            }
            .padding()
            
            // Game Area
            ZStack {
                
                Color.cyan.opacity(0.2)
                
                VStack {
                    
                    Text("☁️")
                        .font(.system(size: 50))
                    
                    Spacer()
                    
                    // Coin
                    if coinVisible {
                        Text("🪙")
                            .font(.system(size: 40))
                    }
                    
                    Spacer()
                    
                    // Player
                    Text("🧑")
                        .font(.system(size: 50))
                        .offset(
                            x: CGFloat(playerX),
                            y: jumping ? -100 : 0
                        )
                    
                    // Ground
                    Rectangle()
                        .fill(.green)
                        .frame(height: 50)
                }
            }
            .clipShape(RoundedRectangle(cornerRadius: 20))
            
            
            // Controls
            HStack(spacing: 15) {
                
                Button("⬅️") {
                    playerX -= 30
                }
                .font(.largeTitle)
                
                
                Button("⬆️") {
                    
                    if !jumping {
                        
                        jumping = true
                        
                        DispatchQueue.main.asyncAfter(
                            deadline: .now() + 0.5
                        ) {
                            jumping = false
                        }
                    }
                }
                .font(.largeTitle)
                
                
                Button("➡️") {
                    
                    playerX += 30
                    
                    // Coin collection
                    if playerX >= 180 && coinVisible {
                        score += 1
                        coinVisible = false
                    }
                }
                .font(.largeTitle)
            }
            .padding()
            
            
            // Reset
            Button("Reset Game") {
                playerX = 0
                score = 0
                coinVisible = true
                jumping = false
            }
            .foregroundStyle(.red)
            .padding(.bottom)
        }
    }
}

#Preview {
    ContentView()
}
