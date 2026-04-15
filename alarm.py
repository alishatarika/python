# import time
# import win32com.client
# import msvcrt

# speaker = win32com.client.Dispatch("SAPI.SpVoice")

# current_hour = int(time.strftime("%H"))


# target_hour = 14

# if current_hour == target_hour:
#     while True:
#          if msvcrt.kbhit():
#             print("Alarm stopped.")
#             break
#          speaker.Speak("Wake up, you are getting late")

import time
import pygame
import msvcrt


pygame.mixer.init()

song_path = r"C:\Users\ankus\Downloads\Yaari.mp3"

 
current_hour = int(time.strftime("%H"))

target_hour = 20

if current_hour == target_hour:
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(-1)  # Play the song indefinitely
    while True:
        if msvcrt.kbhit():
            print("Alarm stopped.")
            pygame.mixer.music.stop()
            break
        time.sleep(1) 