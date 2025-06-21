import os

def menu():
    print ("------- Menu --------")
    print ("-                   -")
    print ("- 1. Select journal -")
    print ("- 2. Read journal   -")
    print ("- 3. Add entry      -")
    print ("- 4. Parent mode    -")
    print ("- 5. Exit           -")
    print ("---------------------")
    maxMenuItems=5
    valid = False
    while valid != True:
        try:
            choice = int(input("Enter your choice "))
            if choice <1 or choice >maxMenuItems:
                print("Invalid choice")
            else:
                valid = True
                return choice
        except:
            print ("Not a valid choice")

def selectJournal():
    print ("**********************")
    print ("***                ***")
    print ("*** Select Journal ***")
    print ("***                ***")
    print ("**********************")
    print()

    path = "/home/spencer/Documents/code/journal/journals/"
    dir_list = os.listdir(path)
    for dir in dir_list:
        print("* " + dir[:-4])
    print ()


selectJournal()