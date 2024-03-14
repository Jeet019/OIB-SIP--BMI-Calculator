class Bmi:
    def __init__(self, weight, height):
        self.weight=weight
        self.height=height
    
    def calculate_bmi(self,weight,height):
        bmi=round((self.weight / self.height**2)*10000,2)
        print(f"Your BMI is {bmi}")
        
        if bmi<16:
            return "Severe Thinness"
        elif bmi>=16 and bmi<17:
            return  "Moderate Thinness"
        elif bmi>=17 and bmi<18.5:
            return  "Mild Thinness"
        elif bmi>=18.5 and bmi<25:
            return  "Normal Weight"
        elif bmi>=25 and bmi<30:
            return   "Overweight"
        elif bmi>=30 and bmi<35:
            return  "Obese Class I"
        elif bmi>=35 and bmi<40:
            return  "Obese Class II"
        else:
            return  "Obese Class III"

w=int(input('Enter your weight in kg : '))
h=int(input("Enter your height in cm : "))
bm=Bmi(w,h)
print(bm.calculate_bmi(w,h))

        

