# convert months to days
def day_converter(number_months):
    days = (number_months * 30)
    return(days)
print(day_converter(3))
print(day_converter(4))
how_many_months = int(input("How many months? "))
print(day_converter(how_many_months))