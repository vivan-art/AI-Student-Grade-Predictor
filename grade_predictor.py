print("===== AI Student Grade Predictor =====")

name = input("Enter Student Name: ")
marks = float(input("Enter Marks (0-100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("\nPrediction Result")
print("Student:", name)
print("Marks:", marks)
print("Predicted Grade:", grade)
