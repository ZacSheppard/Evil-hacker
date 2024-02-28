
def farenheit_to_celcius(temp_in_farenheit):
    temp_in_celcius = (temp_in_farenheit - 32) * (5/9)
    return temp_in_celcius


current_temp = farenheit_to_celcius(111)
print(current_temp)