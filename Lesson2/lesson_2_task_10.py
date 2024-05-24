def bank(x,y):
    for i in range(y):
        x = x + (x * 10) / 100
    return x
x = int(input("ввести сумму "))
y = int(input("ввести срок ")) 
print("итоговая сумма с процентами в конце срока ", bank(x,y)) 
