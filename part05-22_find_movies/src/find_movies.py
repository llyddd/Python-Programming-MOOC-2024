# Write your solution here
def find_movies(database: list, search_term: str):
    
    matching_movies = []
    
    # Iterate through each movie in the database
    for movie in database:
        # Check if search term is in movie name (case-insensitive)
        if search_term.lower() in movie['name'].lower():
            # If match found, add the movie to matching_movies list
            matching_movies.append(movie)
    
    # Return the list of matching movies
    return matching_movies

if __name__ == "__main__":
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)