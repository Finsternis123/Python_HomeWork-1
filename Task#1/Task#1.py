# Найдите сумму цифр трехзначного числа
n = input("Enter a three-digit number: ")
n = int(n)
 
a1 = n % 10
a2 = n % 100 // 10
a3 = n // 100
 
print("Number sum:", a1 + a2 + a3)