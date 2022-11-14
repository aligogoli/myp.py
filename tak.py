taklif = float(input("nomre1:"))
work = float(input('nomre2:'))
exam = float(input('nomre3:'))
if taklif>20 or work>30 or exam>50:
    print("it's not true")
else:
    print(float((taklif+work+exam)*20)/100)
