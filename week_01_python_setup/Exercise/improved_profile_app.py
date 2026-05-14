name = input("What is your name? ")
age = input("How old are you? ")
city = input("Where do you live? ")
favorite_movie = input("Favorite movie: ")
favorite_car = input("Favorite car: ")
favorite_food = input("Favorite food: ")
fun_fact = input("Random fun fact about you: ")

age_in_five_years = int(age) + 5

print()
print("===== Mini Profile =====")
print(f"Name: {name}")
print(f"City: {city}")
print(f"Favorite movie: {favorite_movie}")
print(f"Favorite car: {favorite_car}")
print(f"Favorite food: {favorite_food}")
print(f"Fun fact: {fun_fact}")
print(f"In 5 years, you will be {age_in_five_years}.")
print("========================")

