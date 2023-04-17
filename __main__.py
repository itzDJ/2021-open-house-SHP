#!/usr/bin/env python3

# using 4 spaces for indent to follow PEP 8
# file containing functions for the script (main.py)
import sys
import time
import os


def typewriter(message):
    # function to give text an animated look
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.05)
        else:
            time.sleep(0.5)


def welcome():
    typewriter(
        "Welcome and thank you for coming to Seton Hall Prep's 2021 Open House!"
    )
    time.sleep(3)
    typewriter(
        "\n\nSeton Hall Prep offers an abundance of opportunities.\nI am a junior taking computer science here at The Prep.\nI was given an opportunity to write this program which I happily accepted!\n"
    )


def learn():
    typewriter("\nWhat would you like to learn about?")
    typewriter("\n1. Academics\n2. Sports\n3. Clubs\n")

    ans = ""
    reqs = ("1", "one", "academics", "2", "two", "sports", "3", "three",
            "clubs")
    while ans != reqs:
        typewriter("Choice: ")
        ans = input("").lower()
        if ans == "1" or ans == "one" or ans == "academics":
            academics()
            break
        elif ans == "2" or ans == "two" or ans == "sports":
            sports()
            break
        elif ans == "3" or ans == "three" or ans == "clubs":
            clubs()
            break
        else:
            typewriter(
                "\nThat is not an option. Enter the number corresponding to the option."
            )


def learn_more():
    typewriter(
        "\n\nWould you like to learn more about The Prep or exit the program (more / exit): "
    )
    ans = ""
    while ans != "more" or ans != "exit":
        ans = input("")
        if ans == "more":
            learn()
            break
        elif ans == "exit":
            break
        else:
            typewriter("That is not an option. Enter 'more' or 'exit': ")


def academics():
    typewriter("\nWhat academic field would you like to cover?")
    typewriter(
        "\n1. General Information\n2. Theology\n3. Math\n4. English\n5. Science\n6. History\n7. Foreign Language\n8. Computer Science\n9. Electives\n"
    )
    ans = ""
    reqs = ("1", "one", "general information", "general", "general info", "2",
            "two", "theology", "3", "three", "math", "4", "four", "english",
            "5", "five", "science", "6", "six", "history", "7", "seven",
            "foreign language", "8", "eight", "computer science", "cs",
            "comp sci", "9", "nine", "electives")
    while ans != reqs:
        typewriter(
            "\nPlease enter the departpartment you would like to know more about: "
        )
        ans = input("").lower()
        if ans == "1" or ans == "one" or ans == "general":
            typewriter(
                "Seton Hall offers many academic opportunies and support for their students.\nThere are three levels of classes (CP (College Prep), Honors, and High Honors / AP (Advanced Placement)), so students can customize their schedule based on their strengths."
            )
            typewriter(
                "\nTheology (unless you're a peer leader your senior year), math, and English are four year required courses."
            )
            typewriter(
                "\nScience and History are three year required courses.")
            typewriter("\nForeign language is a two year required course.")
            typewriter(
                "\n\nThe Prep has unique periods built into the day to relieve stress."
            )
            typewriter(
                "\nOn Tuesdays and Thursdays, our second period is 'Activity Period' where students can go to help class, make up work, go to clubs, or hang out with friends."
            )
            typewriter(
                "\nOn Fridays, our second period is 'Enrichment Period' where students can sign up for help class or a large variety of stress relieving activities."
            )
            typewriter(
                "\nThose activities include Bingo, Lego building, Kahoot!, Beach games, and much more."
            )
            time.sleep(1)
            learn_more()
            break
        elif ans == "2" or ans == "two" or ans == "theology":
            typewriter(
                "Theology is a four year required course unless you're a peer leader your senior year. Every freshman spends the first half of their lunch with their peer leaders and peer group."
            )
            typewriter(
                "\nStudents take Introduction to Catholic Theology, Ecclesiology and Moral Theology, Sacred Scriptures, and Senior Theology (or is a peer leader)."
            )
            time.sleep(1)
            learn_more()
            break
        elif ans == "3" or ans == "three" or ans == "math":
            typewriter(
                "Math is a four year required course. Algebra I, Geometry, Algebra II, and Pre-Calc are the required courses."
            )
            typewriter(
                "\nThe AP math courses are AP Calc AB, AP Calc BC, and AP Stat."
            )
            typewriter(
                "\nMath courses are offered at SHP over the summer allowing students to get ahead and excel."
            )
            time.sleep(1)
            learn_more()
            break
        elif ans == "4" or ans == "four" or ans == "english":
            typewriter(
                "English is a four year required course. English I, English II, English III, and English IV are the required courses."
            )
            typewriter(
                "\nAP English Language and Composition is the junior year AP, and AP English Literature is the senior year AP."
            )
            time.sleep(1)
            learn_more()
            break
        elif ans == "5" or ans == "five" or ans == "science":
            typewriter(
                "Science is a three year required course. Many students take Physical science, Physics, Chemistry, and Biology."
            )
            typewriter(
                "\nAP Physics C, AP Biology, AP Environmental Science, AP Chemistry, and High Honors Organic Chemistry are our advanced science classes."
            )
            time.sleep(1)
            learn_more()
            break
        elif ans == "6" or ans == "six" or ans == "history":
            typewriter(
                "History is a three year required course. World History and US History are the required courses.\nEveryone other than the Seton Scholars take world history over two years."
            )
            typewriter(
                "\nAP Human Geography (only offered to Seton Scholars), AP World History, AP US History, AP Microeconomics, and AP Government are our advanced history classes."
            )
            time.sleep(1)
            learn_more()
            break
        elif ans == "7" or ans == "seven" or ans == "foreign language":
            typewriter(
                "Foreign language is a two year required course. Seton Hall offers Spanish, Italian, Mandarin, and Latin."
            )
            typewriter(
                "\nAP Spanish Language, AP Spanish Literature, AP Italian, AP Mandarin, and AP Latin IV are our advanced foreign language classes."
            )
            typewriter("")
            time.sleep(1)
            learn_more()
            break
        elif ans == "8" or ans == "eight" or ans == "computer science" or ans == "cs" or ans == "comp sci":
            typewriter(
                "The Computer Science classes are electives that students can take junior and senior year."
            )
            typewriter(
                "\nThe following classes are offered under our Comp Sci department:"
            )
            typewriter("\nCP Computer Applications")
            typewriter("\nCP Computer Projects: 21st Century Computing")
            typewriter("\nHonors Programming with Java")
            typewriter("\nAP Computer Science A")
            typewriter("\niOS App Development")
            typewriter("\nAP Computer Science Principles")
            time.sleep(1)
            learn_more()
            break
        elif ans == "9" or ans == "nine" or ans == "electives":
            typewriter(
                "Electives are taken junior and senior year. Some electives include: "
            )
            typewriter(
                "\nCinema\nCreative Writing\nAnglo-Saxon Literature\nMusic Theory (CP, Honors, and AP)\nPublic Speaking\nVideo Production"
            )
            time.sleep(1)
            learn_more()
            break
        else:
            typewriter(
                "\nThat is not an option. Enter the number corresponding to the option."
            )


def sports():
    typewriter("\nWhat sports would you like to cover?")
    typewriter("\n1. Fall\n2. Winter\n3. Spring\n")
    ans = ""
    reqs = ("1", "one", "fall", "2", "two", "winter", "3", "three", "spring")
    while ans != reqs:
        typewriter(
            "\nPlease enter the season you would like to know more about: ")
        ans = input("").lower()
        if ans == "1" or ans == "one" or ans == "fall":
            typewriter(
                "The following sports are offered in the fall:\nCrew (JV and Varsity)\nCross Country (Varsity)\nFootball (Freshman, JV, and Varsity)\nSoccer (Freshman, JV, and Varsity)"
            )
            time.sleep(1)
            learn_more()
            break
        elif ans == "2" or ans == "two" or ans == "winter":
            typewriter(
                "The following sports are offered in the winter:\nBasketball (Freshman, JV, and Varsity)\nBowling (Varsity)\nIce Hockey (JV and Varsity)\nIndoor Track (Varsity)\nRifle (Varsity)\nSwimming (Varsity)\nWrestling (Varsity)"
            )
            time.sleep(1)
            learn_more()
            break
        elif ans == "3" or ans == "three" or ans == "spring":
            typewriter(
                "The following sports are offered in the spring:\nBaseball (Freshman, JV, and Varsity)\nCrew (Varsity)\nGolf (Varsity)\nLacrosse (Freshman, JV, and Varsity)\nOutdoor Track (Varsity)\nTennis (JV and Varsity)"
            )
            time.sleep(1)
            learn_more()
            break
        else:
            typewriter(
                "That is not an option. Enter the number corresponding to the option.\n"
            )


def clubs():
    typewriter(
        "\nSeton Hall offers a wide variety of clubs.\nWe offer competitive teams such as the Math Team, the Quiz Bowl Team, and the Robotics Team.\nWe offer performing arts clubs such as the Fall Drama, the Spring Musical, and the Jazz Ensemble.\nBecause students can easily create clubs based on their interests, we also have clubs ranging from the Car Club, to the Engineering Club, to the Future Lawyers Club, to the Ping Pong Club, and much more."
    )
    time.sleep(1)
    learn_more()


def end():
    typewriter("\n\n\nThank you for coming to SHP! Have a nice day!")
    time.sleep(3)
    os.system("clear")  # clears terminal


# SCRIPT BEGINS HERE
def main():  # all code is run from this function
    while True:
        welcome()
        learn()
        end()


if __name__ == '__main__':  # used to tell readers that this is a script
    main()
