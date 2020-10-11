print("Ananya is in 10th grade. She recently joined Girls Who Code, even though she has no idea how to code.")
answer = input("Would you like to begin the adventure? (yes/no)")
if answer.lower().strip() == "yes":
    print("Ananya is looking at her computer. She is on the Girls who Code")
    print("google classroom and sees a link to join a Hackathon. Should she join? (yes/no)")
    answer = input("")
    if answer == "yes":
        print("Ananya's heart beats in her chest. Nervously, she clicks on the link. Ananya is excited, but scared.")


        #screen dims. next day.
        print("It is Saturday 9:00 AM. Ananya's alarm just rang but she is still very sleepy from the week of school")
        print("that just passed. Should she sleep in, or wake up? (sleep in/wake up) ")
        answer = input("")
        if answer == "sleep in":
            print("Ananya presses the snooze button. When she wakes up an hour later, she realizes that the")
            print("hackathon started at 9! Should she still try to join or is it too late?")
            answer = input("")

        elif answer == "wake up":
            print("Ananya grudgingly wakes up, remembering her wise brother's saying about the early coder getting")
            print("the facebook job. Whatever that means. She sees a flurry of email notifications on her screen and")
            print("realizes- the hackathon starts in a few minutes!")
        answer = input("")

    elif answer == "no":
        print("Ananya doesn't join. She spends the whole day thinking")
        print("about what could have happened if she did.. She cries herself to sleep.")

else:
    print("That's too bad!")