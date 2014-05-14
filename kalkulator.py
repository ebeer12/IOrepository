print("Podaj dwie liczby i działanie. Kalkulator doda/odejmie je od siebie.")
a = input()
b = input()
task = input()
if(task == '+'):
    result = int(a) + int(b)
elif(task == '-'):
    result = int(a) - int(b)
else:
    result = "BŁĄÐ"
print(result)
