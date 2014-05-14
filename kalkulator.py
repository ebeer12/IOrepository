print("Podaj dwie liczby i działanie. Kalkulator wykona na nich podane działanie.")
a = input()
b = input()
print("Podaj działanie (+,-,*,/)")
task = input()
if(task == '+'):
    result = int(a) + int(b)
elif(task == '-'):
    result = int(a) - int(b)
elif(task == '*'):
    result = int(a) * int(b)
elif(task == '/'):
    result = int(a) / int(b)        
else:
    result = "BŁĄÐ"
print(result)
