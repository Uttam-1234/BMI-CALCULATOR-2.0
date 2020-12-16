# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
height_square = height**2
bmi = weight/height_square
if bmi<18.5:
  round_bmi = round(bmi,0)
  print(f"Your BMI is {round_bmi}, you are underweight." )

elif bmi>18.5 and bmi<25.0:
  round_bmi=int(round(bmi,0))
  print(f"Your BMI is {round_bmi}, you have a normal weight.")

elif bmi>25.0 and bmi<30.0:
  round_bmi=int(round(bmi,0))
  print(f"Your BMI is {round_bmi}, you are slightly overweight.")

elif bmi>30.0 and bmi<35.0:
  round_bmi=int(round(bmi,0))
  print(f"Your BMI is {round_bmi}, you are obese.")

else :
  round_bmi=int(round(bmi,0))
  print(f"Your BMI is {round_bmi}, you are clinically obese.")


