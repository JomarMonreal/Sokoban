"""
Jomar P. Monreal
CMSC 12 T23L
This is a simple Sokoban game that can be played at the terminal.
"""
import menu
import gameplay

#main program for SOKOBAN
def main():
    #initialization
    has_saved=False
    has_continued=False
    highscore=0

    #main program loop
    user_input=1
    while user_input !=0:
        user_input=menu.display_main_menu(has_saved,highscore)
        if has_saved:
            if user_input!=1 and user_input!=2:
                print("Goodbye!")
                user_input=0
                break
            if user_input==1:
                has_continued=True
        else:
            if user_input!=1:
                print("Goodbye!")
                user_input=0
                break
        has_continued,has_saved,highscore=gameplay.start(has_continued,has_saved,highscore)
                

if __name__=="__main__":
    main()