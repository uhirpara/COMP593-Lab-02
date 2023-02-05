def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name':'Ujas Hirpara',
        'student_id':'10285939',
        'pizza_toppings':['BLACK OLIVES','ONION','PEPPERONI'],
        'movies':[{
            'title':'tare zammen par',
            'genre':'drama'
        },
        {
        'title':'red notice',
        'genre':'action'

        }]


    }
    
    # TODO: Step 3 - Add another movie to the data structure
    about_me['movies'].append({'title':'the conjuring','genre':'horror'})
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me,('EXTRA CHEESE','GREEN PAPER'))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me)
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    first_name=about_me['full_name'].split(" ")[0]
    print(f"My name is {about_me['full_name']}, but you can call me Lord {first_name}.")
    print(f"My student ID is {about_me['student_id']}.")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    
    for i,topping in enumerate (about_me['pizza_toppings']):
        about_me['pizza_toppings'][i] = topping.lower()
    about_me['pizza_toppings'].sort()

    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print(f"My favourite pizza toppings are:")

    for topping in about_me['pizza_toppings']:
        print(f"-{topping}")

    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    print(f"I like to watch",end=" ")
    genre=[g['genre'] for g in about_me['movies']]
    print(', '.join(genre),end='.\n')
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    print(f"Some of my favourite movies are ",end='')
    movie_titles=[m['title'].title() for m in movie_list['movies']]
    print(', '.join(movie_titles),end='!\n')
    return
    
if __name__ == '__main__':
    main()