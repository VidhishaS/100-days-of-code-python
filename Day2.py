#subscript prints the first character of the string mentioned, also start from 0th
print("Hello"[4])
# type() helps to find the data type of a variable
# Cant concatenate an integer to a string
# ** is squaring a number , *** cubing
# / converts result to a float number  , // makes it int
# round() rounds the below number to 2 decimals
print(round(2.88888,2))
# f-string allows you to add integer values by calling a variable in flower brackets
age=9
print(f"Age is:{age}")
# Tip calculator
print("Welcome to tip calculator!")
bill=float(input("What was your total bill? $"))
tip=float(input("What percentage tip would you like to give? 10, 12, or 15?"))
ppl=float(input("How many people are to split the bill?"))
total_tip = bill*(int(tip)/100)
total_bill=bill+total_tip
res= total_bill/ppl
t_res=round(res,2)
# if we want to round to two decimal points and show the zero as well, use
# t_res="{:.2f}",format(res)




print(f"Each person should pay: ${t_res}")