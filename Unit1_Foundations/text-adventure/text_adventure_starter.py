print(start)

keep_going = True
repeat = False

while keep_going:
    while repeat:
        first = input("Type 'school' to go to school or 'water' to get water.")
        if first == "school":
            print('''Your family will be dehydrated for the day.
            But you got good education.
            However, you met some bullies on the way and they want your money.
            ''') # finished the story by writing what happens
            second = input("Type 'give' to give your money or 'keep' to keep it.")
            if second == "give":
                repeat = False
                print('''You are safe now, but you don't have enough money to buy food for your family.
                Your family will starve for another day.
                GAME OVER''')
                break
            elif second == "keep":
                repeat = False
                print('''You got beat up by the bullies, but you were able to secure the money.
                You limp over to the grocery store and get your family food.
                Your family will eat well tonight.
                GAME OVER''')
                keep_going = False
            else:
                repeat = True
                print("Wrong input.Try again.")
        elif first == "water":
            print('''You decided to sacrifice your education for you family.
            You have a choice of fetching water from a dirty lake right next to your home
            or getting clean water from a river by walking 2 miles from your home. ''') # finished the story writing what happens
            third = input("Type 'dirty' to fetch dirty water or 'clean' to fetch clean water.")
            if third == "dirty":
                print('''Your sister drank the water that you brought.
                She got sick with cholera and you don't have enough money to take her to the doctors.
                GAME OVER''')
            elif third == "clean":
                print('''You've finally got the clean water and now you are walking back.
                On the way back you find some wild berries''')

        else:
            repeat = True
            print("Wrong input. Try again.")
