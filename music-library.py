#LOOK_UP = 1
#ADD = 2
#CHANGE = 3
#DELETE = 4
#NUM_TITLES = 5
#TITLES_ARTISTS = 6
#TITLES = 7
#QUIT = 8
#in main()
#   names = {}
#   choice = 0 for initializing
#in get_choice()
#   print 1. Look up by title
#   print 2. Add a new title and artist(s)
#   print 3. Change existing artist(s)
#   print 4. Delete a title and artist(s)
#   print 5. Print the number of titles
#   print 6. Print all titles and artist(s)
#   print 7. Print all titles
#   print 8. Quit the program
#   choice = prompt user to enter a choice
#   while choice < LOOK_UP or choice > QUIT
#       choice = prompt user to enter a valid choice
#   return choice
#in look_up(names)
#   title = prompt user to enter albums title
#   print names.get(title, 'The specified title was not found.')
#in add(names)
#   title = prompt user to enter albums title
#   artist = prompt user to enter artists name
#   if title not in names
#       names[title] = artist
#   else
#       print title already exists
#in change(names)
#   title = prompt user to enter albums title
#   if title in names
#       artist = prompt user to enter the name of the new artist
#       names[title] = artist
#   else
#       print 'The specified title was not found'
#in delete(names)
#   title = prompt user to enter albums title
#   if title in names
#       del names[title]
#   else
#       print 'The specified title was not found'
#back in main()
#   while choice != QUIT
#       choice = get_choice()
#   if choice == LOOK_UP
#       look_up(names)
#   elif choice == ADD
#       add(names)
#   elif choice == CHANGE
#       change(names)
#   elif choice == DELETE
#       delete(names)
#   elif choice == NUM_TITLES
#       print f'There are {len(names)} titles'
#   elif choice == TITLES_ARTISTS
#       for k,v in names.items()
#           print k and v
#   elif choice == TITLES
#       for k in names
#           print k

#Global constants
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
NUM_TITLES = 5
TITLES_ARTISTS = 6
TITLES = 7
QUIT = 8

def main():
    
    names = {}

    #Initialize users choice variable
    choice = 0

    while choice != QUIT:

        choice = get_choice()

        #call a function
        if choice == LOOK_UP:
            look_up(names)
        elif choice == ADD:
            add(names)
        elif choice == CHANGE:
            change(names)
        elif choice == DELETE:
            delete(names)

        #this displays the number of titles
        elif choice == NUM_TITLES:
            print(f'There are {len(names)} titles')

        #this displays all titles and artists
        elif choice == TITLES_ARTISTS:
            for k,v in names.items():
                print(f'{k} by {v}')

        #this displays all the titles
        elif choice == TITLES:
            for k in names:
                print(f'{k}')
    

    

  

def get_choice():
    print('MENU')
    print('-----------------------------------')
    print('1. Look up by title')
    print('2. Add a new title and artist(s)')
    print('3. Change existing artist(s)')
    print('4. Delete a title and artist(s)')
    print('5. Print the number of titles')
    print('6. Print all titles and artist(s)')
    print('7. Print all titles')
    print('8. Quit the program')
    #get users choice
    choice = int(input('\nEnter your choice: '))

    #make sure user inputs a valid choice
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice '))
    return choice

def look_up(names):

    #get the albums title
    title = input('Enter the albums title ')

    #look the title up
    print(names.get(title, 'The specified title was not found.'))

def add(names):

    #get the name of album and artist
    title = input('Enter the albums title ')
    artist = input('Enter the artists name ')

    #add the title if not in dictionary
    if title not in names:
        names[title] = artist
    else:
        print('Title already exists.')

def change(names):
    title = input('Enter the albums title ')

    #change the title if in dictionary
    if title in names:
        artist = input('Enter the name of the new artist ')
        names[title] = artist
    else:
        print('The specified title was not found.')

def delete(names):
    title = input('Enter the albums title ')

    #delete a title if in dictionary
    if title in names:
        del names[title]
    else:
        print('The specified title was not found.')
        
if __name__ == '__main__':
    main()




