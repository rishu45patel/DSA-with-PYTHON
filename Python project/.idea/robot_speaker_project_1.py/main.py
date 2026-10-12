# import os

# if __name__ =='__main__':
    
#     print("welcome to RoboSpeaker 1.1. created by ritesh")
    
#     while True:
#      x=input("enter what you want me to speak:..")
#      if x=="q":
#         break
#     command=f"say{x}"

#     os.system(command)

import pyttsx3

engine = pyttsx3.init()

#while True:
text = input("enter to me speak:...")
#    if text=="q":
#      break



engine.say(text)
engine.runAndWait()














