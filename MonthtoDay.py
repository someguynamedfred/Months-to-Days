# convert months to days
#this is working
def day_converter(number_months):
    days = (number_months * 30)
    return(days)
#print(day_converter(3))
#print(day_converter(4))
how_many_months = int(input("How many months? "))
print("there are " + str(day_converter(how_many_months)) + " days in " + str(how_many_months) + " months.")

# convert months and years to days
#this is not
def day_converter(number_months, number_years):
    months = (int(number_years) * 12)
    number_months = (int(number_months) + months)
    days = (number_months * 30)
    return(days)
how_many_months, how_many_years = input("How many months and years? ") .split()
print("there are " + str(day_converter(how_many_months, how_many_years)) + " days in " + str(how_many_months) + " months.")
