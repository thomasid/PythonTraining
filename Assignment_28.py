# finding max among variables

var1 = 10
var2 = 100
var3 = 1000

varlist = [var1, var2, var3]
max = 0
for x in varlist:
    if x > max:
        max = x

print(max)