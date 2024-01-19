# convert months to days
def day_converter(number_months):
    days = (number_months * 30)
    return(days)
#print(day_converter(3))
#print(day_converter(4))
how_many_months = int(input("How many months? "))
print("there are " + str(day_converter(how_many_months)) + " days in " + str(how_many_months) + " months.")

# convert months and years to days
def day_converter(number_months, how_many_years):
    months_augmented = (int(how_many_years) * 12)
    number_months = (int(number_months) + months_augmented)
    days = (number_months * 30)
    return(days)

how_many_months, how_many_years = input("How many months and years? ") .split()

print("there are " + str(day_converter(how_many_months, how_many_years)) + " days in " + str(how_many_months) + " months and " + str(how_many_years) + " years.")
