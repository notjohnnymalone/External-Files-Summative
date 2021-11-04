##########################
#Ext Files Summative
#Reid A. Martin
##########################

#answer#
#The benefits of having a program like this use external files are very prevalent.
#You can store values in a user readable format, the file can be accessed outside of python,
#and most importantly... The values are saved. That is a gamechanger.


#--Empty List to temp store a stripped list for the final sentence
ready_list = []

############################

def main():
    if __name__ == '__main__': #if main file, goes
        done = False
        while done == False:
            choice = input("""Welcome to Reid's character creator!!!!
********************************************************
What would you like to do?
1. Create a character
2. Read a character
3. Exit
********************************************************
>""")
            if choice == '1':
                c_name = input("What is your character's name?\n>").lower()
                print(f"Your file will be called {c_name}.txt")
                file_name = c_name + '.txt' #puts char name and .txt together to make new file
                make_char(file_name) #runs make char funct
                
                
            elif choice == '2':
                c_name = input("What is your character's name?\n>").lower()
                print(f"Looking for {c_name}.txt")
                file_name = c_name + '.txt' #puts char name and .txt together to find file
                read_char(file_name) #runs read func
                
            elif choice == '3':
                done = True
                
            else:
                print("please use a number")
            
def make_char(file_name):
    create = open(file_name, 'w') #makes file
    
    gender = input("What gender is your character?\n>").lower()
    print(f"Your character's gender is {gender}.")
    create.write(gender) #writes gender
    
    species = input("What race/species is your character?\n>").lower()
    print(f"Your character is a {species}.")
    create.write(f"\n{species}") #writes species
    
    weapon = float(input("""**********************************************************
So, now that the baseline is made... you need to choose a weapon for your character.
*********************************************************
What weapon would you like?
1. a knife
2. a child
3. words
>"""))
    
    if weapon == 1:
        print("That's boring")
        create.write("\na knife")#writes knife
    elif weapon == 2:
        print("Logical choice... they are repulsive.")
        create.write("\na child")#writes child
    elif weapon == 3:
        print("congrats. you are a d--k.")
        create.write("\nwOrDs")#writes the ahole weapon
    else:
        print("because you can't type a simple number, you get nothing")
        create.write("\na big fat nothing") #writes nothing....
    
    ability = float(input("""Time to pick a special ability!
1. Super Strength
2. Anxiety
3. Intense PTSD
>"""))
    if ability == 1:
        print("cliche")
        create.write("\nsuper strength")#writes strength
    elif ability == 2:
        print("damn that's relatable")
        create.write("\ncrippling anxiety") #writes anxiety
    elif ability == 3:
        print("having some flashbacks, hey?")
        create.write("\nintense PTSD")#writes PTSD
    else:
        print("y'know what? you get financial debt.")
        create.write("\ndebt") #write debt
        
    create.close()#closes file
    
def read_char(file_name):
    char_file = open(file_name, 'r') #opens file
    read_file = char_file.readlines() #puts file into list
    #char_list = print(read_file)
    for elements in read_file:
        ready_list.append(elements.strip("\n")) #takes \n off values and puts in temp list
    print(ready_list) #prints temp list
        
    print(f"""Your character is a {ready_list[0]} {ready_list[1]}, who has {ready_list[3]},
and wields {ready_list[2]}""") #prints values from the temp_list
    
    ready_list.clear()
    char_file.close()#closes file
    
##########
main()