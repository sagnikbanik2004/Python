def calculate_bmr(weight, height, age, gender):
    if gender.lower() == "male":
        bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
    elif gender.lower() == "female":
        bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    else:
        raise ValueError("Invalid gender")

    return bmr


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
age = int(input("Enter your age in years: "))
gender = input("Enter your gender (Male/Female): ")

bmr = calculate_bmr(weight, height, age, gender)
print(f"Your Basal Metabolic Rate (BMR) is {bmr} calories/day.")
