# Write your solution here
def converter(filename: str):
    recipes = []  # Create an empty list to store the matrix
    temp_recipe = []
    with open(filename) as new_file:
        lines = new_file.readlines()

    for line in lines:
        line = line.strip()  # Remove extra spaces and newlines
        if line:  # If the line is not empty, store the data
            temp_recipe.append(line)
        elif line == "":# If there's a blank line, save the collected recipe
            if temp_recipe:  
                name = temp_recipe[0]
                time = int(temp_recipe[1])
                ingredients = temp_recipe[2:]  # The rest are ingredients
                recipes.append([name, time, ingredients])
                temp_recipe = []  # Reset for the next recipe
                
    if temp_recipe:
        name = temp_recipe[0]
        time = int(temp_recipe[1])
        ingredients = temp_recipe[2:]  # The rest are ingredients
        recipes.append([name, time, ingredients])
        temp_recipe = []  # Reset for the next recipe
      # Return the list
    return  recipes


def search_by_name(filename: str, word: str):
    recipe_name = []
    recipe_name = converter(filename)
    recipe_name_temp = []
    for name in recipe_name:
        recipe_name_temp.append(name[0])
    matches = []
    search_term = word.lower()
# Loop through each word in the list
    for value in recipe_name_temp:
    # Check if the search term is a substring of the word
        if search_term in value.lower():
            matches.append(value)  # Add matching word to the list
    
    return matches

def search_by_time(filename: str, prep_time: int):
    time_list = []
    time_list = converter(filename)
    matches = []
    search_term = prep_time

    for value in time_list:
        checker = int(value[1])
        
        if checker <= search_term:
            name = value[0]
            times = value[1]
            matches.append(f"{name}, preparation time {times} min")
   
    return matches

def search_by_ingredient(filename: str, ingredient: str):
    ingredient_list = []
    ingredient_list = converter(filename)
    matches = []
    search_term = ingredient

    for name, time, ingredients in ingredient_list:
        
        if search_term in ingredients:
            matches.append(f"{name}, preparation time {time} min")

    return matches
if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_time("recipes1.txt", 20)
    for recipe in found_recipes:
        print(recipe)    

    found_recipes = search_by_ingredient("recipes1.txt", "milk")
    for recipe in found_recipes:
        print(recipe)
