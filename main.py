import multiplication
import addition
import division
import mod
import subtraction

x = 8
y = 5
result_of_subtraction = subtraction.sub(x,y)
result_of_addition = addition.add(x,y)
result_of_multiplication = multiplication.multiply(x,y)
result_of_division = division.divide(x,y)
result_of_mod = mod.mod(x,y)

print("X=8 and Y=5")
print("Result of subtraction: "+str(result_of_subtraction))
print("Result of addition: "+str(result_of_addition))
print("Result of multiplication: "+str(result_of_multiplication))
print("Result of division: "+str(result_of_division))
print("Result of mod: "+str(result_of_mod))