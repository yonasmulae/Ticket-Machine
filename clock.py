# -----------------------------------Project on Ticket Machine by "Dawit" & "Yonas"---------------------------------
# The program will ask the consumer which of the places they wish to visit, and depending on the
# area they choose, it will assign them a relevant turn number.

# to make emoji we need to import and install emoji library
import emoji as emoji

# to make timer we need to import and install time library
import time

# define the countdown function
def countdown():
    time_sec = 10
    while time_sec > 0:
        minutes, secs = divmod(time_sec, 60)
        hour, minutes = divmod(minutes, 60)
        timeleft = str(hour).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(secs).zfill(2)
        print(timeleft + "\r", end='')
        time.sleep(1)
        time_sec -= 1
        print(timeleft)
    print('\n You are done for today !!')
    print(emoji.emojize('\n\t\t\t\t\tThank you for visiting us '
                        '\n\t\t\t\t\t\t Have a nice day :grinning_face_with_big_eyes::thumbs_up:'))
