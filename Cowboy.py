#from sys import argv
#script, name, past, past_answer = argv

prompt = "> "

print("What's your name, cowboy?")
name = input(prompt)

def past_menu():
    print(f"""What's your past, {name}?
1. A poor farmer, searching for money to save your farm.
2. A gunslinger, searching someone who needs your services.
3. A sheriff, searching a dangerous criminal who just escaped from prison.""")
    past = input(prompt)


    if past == "1":
        gun, bullets, career = "bow and arrow", 30, "farmer"
        past_conclusion(gun, bullets, career)
    elif past == "2":
        gun, bullets, career = "colt", 45, "gunslinger"
        past_conclusion(gun, bullets, career)
    elif past == "3":
        gun, bullets, career = "winchester", 40, "sheriff"
        past_conclusion(gun, bullets, career)
    else:
        print("Choose a valis past!\n")
        past_menu()
    return gun, bullets, career

def past_conclusion(gun, bullets, career):
    print(f"You are {name}, a {career}. Your equipment is an {gun} with {bullets} ammunitions.")
    print("Are you satisfied with your past? [Y/N]")
    past_answer = input(prompt)
    if (past_answer == 'N') or (past_answer == 'n'):
        past_menu()
    elif (past_answer != 'Y') and (past_answer != 'y'):
        print("Invalid answer!\n")
        past_conclusion(gun, bullets, career)


gun, bullets, career = past_menu()


def start():
    print(f"""\nYou are in the town of Still Water, with only your horse and equipment. You can go to 4 different places:
1. The Bar
2. The Hotel
3. The Precint
4. The Bank\n
Where do you go?""")
    town_choice = input(prompt)

    if town_choice == "1":
        end
    elif town_choice == "2":
        hotel1()

    elif town_choice == "3":
        end()
    elif town_choice == "4":
        end()
    else:
        print("Choose a valid option!\n\n")
        start()

# HOTEL ------------------------------------------------------------------------

def hotel1():
    print("""You enter in the Hotel. There seens to be no one at the reception, but there is a delicious smell of ribs coming from the kitchen.
You haven't eaten real food for days, and your stomach start to make noises. You can also hear people talking trought the kitchen door.\n
What do you do?
1. Go to the kitchen
2. Go back to the street""")
    hotel_choice1 = input(prompt)
    if hotel_choice1 == "1":
        hotel2()
    elif hotel_choice1 == "2":
        start()
    else:
        print("Choose a valid option!\n\n")
        hotel1()

def hotel2():
    print("""You find 4 people sitting on the table, eating some pork ribs. They talk to each other silently, in a tense way.
There is a lot of luggage on the floor, and a man standing alone, with a Colt on his holster and a sheriff badge.\n
What do you do?
1. Go talk to the sheriff
2. Sit on the corner of the table and ask for some ribs and a scotch
3. Go back to the hotel lobby""")
    hotel_choice2 = input(prompt)
    if hotel_choice2 == "1":
        hotel3()
    elif hotel_choice2 == "2":
        end()
    elif hotel_choice2 == "3":
        hotel1()
    else:
        print("Choose a valid option!\n\n")
        hotel2()

def hotel3():
    if career == "gunslinger":
        sh_ht3 = "He says: 'Hey, since you are a gunslinger, you could make a good money escorting these people to Capital City. I would do that, but I'm too here in town. What do you say?"
    elif career == "farmer":
        sh_ht3 = "He says: 'It may not be the easiest of jobs, but since you're searching for some money, you could escort these people to Capital City. What do you think?"
    elif career == "sheriff":
        sh_ht3 = "He says: 'Say, my friend. Couldn't you help a fellow sheriff? If you could escort these people to Capital City, I would own you a favor and help you to find this criminal you are going after. What do you say?"
    print(f"""You introduce yourself to the sheriff and asks what is this all about.
He tells you that these are citizen of still water wanting to go to Capital City, and are nervous becaude a lot of bandits inhabit the road.
{sh_ht3}""")

# ------------------------------------------------------------------------------

def end():
    print("This part is not done yet")

start()
