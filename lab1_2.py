var1 = int(input("Please enter the first value: "))
var2 = int(input("Please enter the second value: "))
sum = var1 + var2
diff = var1 - var2
if diff < 0:
    diff = - diff
prod = var1 * var2

print(f" var1: {var1} \n var2: {var2} \n sum: {sum} \n diff: {diff} \n prod: {prod} \n")