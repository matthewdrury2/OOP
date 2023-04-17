import InsectClass as I


mosquito = I.Insect('mosquito', 2, 4)
housefly = I.Insect('housefly', 2, 4)

mosquito.flight_length()
housefly.flight_length()


print(f'the {mosquito.get_name()} can fly up to {mosquito.get_miles()} miles')

print(f'the {housefly.get_name()} can fly up to {housefly.get_miles()} miles')
