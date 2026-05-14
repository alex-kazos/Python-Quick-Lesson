name = input("What is your name? ").strip()
age_text = input("How old are you? ").strip()
city = input("Where do you live? ").strip()
favorite_movie = input("Favorite movie: ").strip()
favorite_car = input("Favorite car: ").strip()
favorite_food = input("Favorite food: ").strip()
fun_fact = input("Random fun fact about you: ").strip()

print()
print("=" * 32)
print("Mini Profile")
print("=" * 32)
print(f"Name: {name}")
print(f"City: {city}")
print(f"Favorite movie: {favorite_movie}")
print(f"Favorite car: {favorite_car}")
print(f"Favorite food: {favorite_food}")
print(f"Fun fact: {fun_fact}")

if age_text.isdigit():
    age = int(age_text)
    print(f"In 5 years, you will be {age + 5}.")
else:
    print("Age was not a valid whole number, so I skipped the age math.")

print("=" * 32)

