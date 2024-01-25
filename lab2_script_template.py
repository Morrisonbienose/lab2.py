


def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
                'full_name': 'morrison bienose',
                'student_id' : 10314960,    
                'pizza_toppings' :['MAYO','WHITE ONION','GREEN PEPPER'],
                'movies' : [
                        {'title' : 'prison break','genre' : 'Action'},
                        {'title' : 'Host','genre' : 'Agent47'},
                ],
    }

    # TODO: Step 3 - Add another movie to the data structure
    
    new_movie = {'title' : 'Avengers End Game','genre' : 'sci-fi'}
    about_me['movies'].append(new_movie)

    print_student_name_and_id(about_me)
    add_pizza_toppings(about_me, ("Chicken", "Bread"))
     
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me['full_name']
    first_name = (full_name.split())[0]
    student_id = about_me['student_id']

    print(f"My name is {full_name},but you can call me Mr {first_name}.\nMy student id is {student_id}")
    
    return


# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    for top in toppings:
        about_me['pizza_toppings'].append(top)
    
    about_me['pizza_toppings'] = list(set(about_me['pizza_toppings']))
    about_me['pizza_toppings'].sort()

    about_me['pizza_toppings'] = [topping.lower() for topping in about_me['pizza_toppings']]


# TODO: Step 6 - Function that prints bullet list of pizza toppings 
def pizza_toppings_list(about_me):
    toppings_item = about_me["pizza_toppings"].split(", ")
    print("My favorite pizza toppings are:")
    print(f"- {toppings_item[0]}")
    print(f"- {toppings_item[1]}")
    print(f"- {toppings_item[2]}")

# TODO: Step 7 - Function that prints comma-seperated list of movie genres
def print_movie_genres(about_me):
    movies = about_me["movies"]
    genres_list = [movie["genre"] for movie in movies]
    print(f"I like to watch {genres_list} movies.")

# TODO: Step 8 - Function that prints comma-seperated list of movie titles
    def movie_title_list(about_me):
        movie_title_list = [film['title'] for film in about_me['movies']]
        print(f"Some of my favorite movies are: {', '.join(movie_title_list)}")

if __name__ == '_main_':
        main()

            
