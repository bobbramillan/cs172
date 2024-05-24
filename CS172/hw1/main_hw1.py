#Bavanan Bramillan bb3323 
#program that gives nutritional info of an item from users inputs

from food import FoodItem
import inputroutines as ine


food_name = input("\nEnter food item's name: ")

try:
    serving_size = input("\nEnter the serving size in grams (or mL for liquids): ")
    fat = input("\nEnter the grams of fat per serving: ")
    carbs = input("\nEnter the grams of carbs per serving: ")
    protein = input("\nEnter the grams of protein per serving: ")
except ValueError:
    serving_size = ine.intInRange(0, 500)
    fat = ine.floatInRange(0.00, 50.00)
    carbs = ine.floatInRange(0.00, 50.00)
    protein = ine.floatInRange(0.00, 50.00)

fi = FoodItem(food_name, serving_size, fat, carbs, protein)

print(f'Nutritional information per serving of {fi.getName()}')
print(f'Serving Size: {fi.getServingSize()} grams / mL')
print(f'Fat: {fi.getFat():.2f} grams')
print(f'Carbohydrates: {fi.getCarbs():.2f} grams')
print(f'Protein: {fi.getProtein():.2f} grams')
print(f'Number of calories for 1 serving: {fi.calculateCalories(1):.2f} calories')

try:
    num_serv = input("\nEnter the number of servings consumed: ")
except ValueError:
    num_serv = ine.intInRange(0,10)


new_cal = num_serv * fi.calculateCalories()
print(f'\nNumber of calories for 3 serving(s): {new_cal:.2f}')

