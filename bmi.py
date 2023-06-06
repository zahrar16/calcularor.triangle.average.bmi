
print("enter weight")
weight = float(input())

print("enter height")
height = float(input())

a = (weight / (height**2))*10000

if a < 18.5:
    print("shoma dochar kambode vaz hastin")
elif a >18.5 and a <24.9:
    print("shoma normal hastin")
elif a >25 and a <29.9:
    print("shoma normal hastin")
elif a > 30:
    print("shoma normal hastin")

