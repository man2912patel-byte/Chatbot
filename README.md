import SwiftUI

struct ContentView: View {
    
    @State private var playerX = 100
    @State private var score = 0
    
    var body: some View {
        
        ZStack {
            
            // Background
            Color.cyan.opacity(0.3)
                .ignoresSafeArea()
            
            
            VStack {
                
                // Score
                Text("⭐ Score: \(score)")
                    .font(.title2)
                    .bold()
                
                Spacer()
            }
            .padding()
            
            
            // ☁️ Cloud
            Text("☁️")
                .font(.system(size: 60))
                .position(x: 100, y: 150)
            
            
            // 🪙 Coin
            Button {
                score += 1
            } label: {
                Text("🪙")
                    .font(.system(size: 40))
            }
            .position(x: 250, y: 350)
            
            
            // 🟫 Platform
            Rectangle()
                .fill(.brown)
                .frame(width: 150, height: 25)
                .position(x: 250, y: 430)
            
            
            // 🟩 Ground
            Rectangle()
                .fill(.green)
                .frame(height: 60)
                .position(x: 200, y: 750)
            
            
            // 🧑 Player
            Text("🧑")
                .font(.system(size: 50))
                .position(x: CGFloat(playerX), y: 680)
            
            
            // Controls
            VStack {
                
                Spacer()
                
                HStack(spacing: 20) {
                    
                    // Left
                    Button {
                        playerX -= 20
                    } label: {
                        Text("⬅️")
                            .font(.system(size: 35))
                            .padding()
                            .background(.white)
                            .cornerRadius(15)
                    }
                    
                    
                    // Jump
                    Button {
                        score += 1
                    } label: {
                        Text("⬆️")
                            .font(.system(size: 35))
                            .padding()
                            .background(.white)
                            .cornerRadius(15)
                    }
                    
                    
                    // Right
                    Button {
                        playerX += 20
                    } label: {
                        Text("➡️")
                            .font(.system(size: 35))
                            .padding()
                            .background(.white)
                            .cornerRadius(15)
                    }
                }
                
                .padding(.bottom, 20)
            }
        }
    }
}

#Preview {
    ContentView()
}
