import SwiftUI

struct ContentView: View {
    
    @State private var maths = ""
    @State private var physics = ""
    @State private var chemistry = ""
    
    @State private var total = 0
    @State private var percentage = 0.0
    @State private var grade = ""
    
    var body: some View {
        NavigationStack{
            ZStack{
                Image(systemName: "graduationcap.fill")
                    .font(.system(size: 100))
                    .foregroundStyle(.blue.opacity(0.20))
                    .offset(x:100,y:-290)
                
                
                VStack(spacing: 20) {
                    
                    Text("Student Grade Calculator")
                        .font(.title2)
                        .fontWeight(.bold)
                    
                    TextField("Maths Marks", text: $maths)
                        .textFieldStyle(.roundedBorder)
                        .keyboardType(.numberPad)
                    
                    TextField("Physics Marks", text: $physics)
                        .textFieldStyle(.roundedBorder)
                        .keyboardType(.numberPad)
                    
                    TextField("Chemistry Marks", text: $chemistry)
                        .textFieldStyle(.roundedBorder)
                        .keyboardType(.numberPad)
                    
                    Button("Calculate") {
                        calculateResult()
                    }
                    .frame(maxWidth: .infinity)
                    .padding()
                    .background(.blue)
                    .foregroundStyle(.white)
                    .cornerRadius(10)
                    
                    Text("Total Marks: \(total) / 300")
                    
                    Text("Percentage: \(percentage, specifier: "%.2f")%")
                    
                    Text("Grade: \(grade)")
                        .font(.title3)
                        .fontWeight(.bold)
                    
                    Button("Reset") {
                        maths = ""
                        physics = ""
                        chemistry = ""
                        total = 0
                        percentage = 0
                        grade = ""
                    }
                    .foregroundStyle(.red)
                }
                .padding()
            }
        }
    }
        
        func calculateResult() {
            
            let m = Int(maths) ?? 0
            let p = Int(physics) ?? 0
            let c = Int(chemistry) ?? 0
            
            total = m + p + c
            
            percentage = Double(total) / 300 * 100
            
            if percentage >= 90 {
                grade = "A+"
            } else if percentage >= 80 {
                grade = "A"
            } else if percentage >= 70 {
                grade = "B"
            } else if percentage >= 60 {
                grade = "C"
            } else if percentage >= 50 {
                grade = "D"
            } else {
                grade = "F"
            }
        }
      }
    
#Preview {
    ContentView()
}
