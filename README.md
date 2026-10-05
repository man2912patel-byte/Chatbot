import SwiftUI

struct ContentView: View {
    
    // Marks
    @State private var maths = ""
    @State private var physics = ""
    @State private var chemistry = ""
    
    // Result
    @State private var total = 0
    @State private var percentage = 0.0
    @State private var grade = ""
    
    var body: some View {
        
        ZStack {
            
            // Background
            Color.blue.opacity(0.05)
                .ignoresSafeArea()
            
            // Background icons
            Image(systemName: "graduationcap.fill")
                .font(.system(size: 120))
                .foregroundStyle(.blue.opacity(0.08))
                .offset(x: 120, y: -300)
            
            Image(systemName: "book.fill")
                .font(.system(size: 100))
                .foregroundStyle(.purple.opacity(0.08))
                .offset(x: -120, y: -180)
            
            Image(systemName: "backpack.fill")
                .font(.system(size: 100))
                .foregroundStyle(.orange.opacity(0.08))
                .offset(x: 120, y: 150)
            
            Image(systemName: "books.vertical.fill")
                .font(.system(size: 90))
                .foregroundStyle(.green.opacity(0.08))
                .offset(x: -120, y: 300)
            
            
            // Main screen
            VStack(spacing: 18) {
                
                // Main Icon
                Image(systemName: "graduationcap.fill")
                    .font(.system(size: 55))
                    .foregroundStyle(.blue)
                
                // Title
                Text("Student Grade Calculator")
                    .font(.title2)
                    .fontWeight(.bold)
                
                Text("Enter your marks")
                    .foregroundStyle(.gray)
                
                
                // Maths
                HStack {
                    
                    Text("Maths")
                        .frame(width: 80, alignment: .leading)
                    
                    TextField("Marks", text: $maths)
                        .keyboardType(.numberPad)
                    
                    Image(systemName: "function")
                        .foregroundStyle(.blue)
                }
                .padding()
                .background(.white)
                .cornerRadius(12)
                
                
                // Physics
                HStack {
                    
                    Text("Physics")
                        .frame(width: 80, alignment: .leading)
                    
                    TextField("Marks", text: $physics)
                        .keyboardType(.numberPad)
                    
                    Image(systemName: "atom")
                        .foregroundStyle(.purple)
                }
                .padding()
                .background(.white)
                .cornerRadius(12)
                
                
                // Chemistry
                HStack {
                    
                    Text("Chemistry")
                        .frame(width: 80, alignment: .leading)
                    
                    TextField("Marks", text: $chemistry)
                        .keyboardType(.numberPad)
                    
                    Image(systemName: "flask.fill")
                        .foregroundStyle(.green)
                }
                .padding()
                .background(.white)
                .cornerRadius(12)
                
                
                // Calculate Button
                Button("Calculate") {
                    calculateResult()
                }
                .frame(maxWidth: .infinity)
                .padding()
                .background(.blue)
                .foregroundStyle(.white)
                .cornerRadius(12)
                
                
                // Result
                Text("Total Marks: \(total) / 300")
                
                Text("Percentage: \(percentage, specifier: "%.2f")%")
                
                Text("Grade: \(grade)")
                    .font(.title3)
                    .fontWeight(.bold)
                
                
                // Reset Button
                Button("Reset") {
                    
                    maths = ""
                    physics = ""
                    chemistry = ""
                    
                    total = 0
                    percentage = 0
                    grade = ""
                }
                .foregroundStyle(.red)
                
                Spacer()
            }
            .padding()
        }
    }
    
    
    // Calculate Function
    func calculateResult() {
        
        let m = Int(maths) ?? 0
        let p = Int(physics) ?? 0
        let c = Int(chemistry) ?? 0
        
        total = m + p + c
        
        percentage = Double(total) / 300 * 100
        
        if percentage >= 90 {
            grade = "A+"
        }
        else if percentage >= 80 {
            grade = "A"
        }
        else if percentage >= 70 {
            grade = "B"
        }
        else if percentage >= 60 {
            grade = "C"
        }
        else if percentage >= 50 {
            grade = "D"
        }
        else {
            grade = "F"
        }
    }
}


#Preview {
    ContentView()
}
