#Michael Dupuis CIS261 Movie Guide Part2

with open("movies.txt", "w") as file:
    file.write("Cat on a Hot Tin Roof\nOn the Waterfront\nMonty Python and the Holy Grail\n")
    
def populate_list(file_name):
    movie_list = []
    with open(file_name, "r") as file:
        for line in file:
            movie_list.append(line.strip())
    return movie_list

def display_menu():
    print("Movie list program\n")
    print("Comand Menu")
    print("list --> Display movie titles")
    print("add --> Add movie title")
    print("delete --> Delete movie title")
    print("exit --> Exit program\n")

def display_title(movie_list):
    print("\nMovie Titles: ")
    for idx, title in enumerate(movie_list, start=1):
        print(f"{idx}. {title}")
        
def add_title(movie_list, title, file_name):
    movie_list.append(title)
    with open(file_name, "a") as file:
        file.write(title +"\n")
    print(f"\n{title} has been added")

def delete_title(movie_list, index, file_name):
    if 1 <= index <= len(movie_list):
        delete_title = movie_list.pop(index - 1)
        with open(file_name, "w") as file:
            file.write("\n".join(movie_list))
        print(f"\n {delete_title} has been removed")
    else:
        print(f"\nInvalid index number. No movie was deleted")
        
def main():
    movie_file = "movies.txt"
    movie_list = populate_list(movie_file)
    
    while True:
        display_menu()
        command = input("Enter command: ")
        
        if command == "list":
            display_title(movie_list)
        elif command == "add":
            new_title = input("Enter new movie title: ")
            add_title(movie_list, new_title, movie_file)
            display_title(movie_list)
        elif command == "delete":
            display_title(movie_list)
            index = int(input("Enter number to delete title: "))
            delete_title(movie_list, index, movie_file)
            display_title(movie_list)
        elif command == "exit":
            print("Have a  good day")
            break
        else:
            print("Invalid command entered")
            
if __name__ == "__main__":
    main()

            

    

        