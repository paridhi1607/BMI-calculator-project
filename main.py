# generate a bmi calculator
name = str(input("please enter your NAME"))
age = int(input("please enter your AGE"))
gender = input("please enter your GENDERr. Make sure it is either male or female")
height = float(input("please enter your HEIGHT in CENTIMETRES"))
height_m = height/100
weight = float(input("please enter your WEIGHT in KG"))
print ("WARNING - RECHECK IF YOUR HEIGHT AND WEIGHT IS IN CM AND KG RESPECTIVELY")
bmi = weight/height_m**2
if (bmi<18.5):
    category = "underweight"
    advice = "increase calorie intake by +300kcal/day."
elif 18.5<=bmi<24.9:
    category = "normal weight"
    advice = "maintain your calorie at normal level"
elif 24.9<=bmi<29.9:
    category = "over weight"
    advice = "mild calorie deficient(-300kcal/day)"
else:
    category = "obese"
    advice = "please consult a dietician."

#counting kcal required 


if gender == "male" or gender == "MALE" or gender == "Male":
    bmr= (10*weight)+(6.25*height)-(5*age)+5
elif gender == "female" or gender =="FEMALE"or gender == "Female":
    bmr= 10*weight+6.25*height-5*age-161
else:
    bmr = "none "
    
kcal = bmr*1.375

report = print("HEALTH REPORT")
print(report)
print("NAME:",name)
print("AGE:",age)
print("gender", gender)
print("height in metres",height)
print("weight in kilos",weight)
print("BMI according to your age and gender and height", bmi)
print(category)
print(advice)
print("BMR", bmr)
print(kcal)
