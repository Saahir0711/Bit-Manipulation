numA = 1
numB = 0
numC = 1

num1 = numA & numB
num2 = numB ^ numC
num3 = numB | numC
num4 = num2 & num3
final = num1 & num4

print (final)