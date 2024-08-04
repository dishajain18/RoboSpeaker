import os

if __name__ == '__main__':
    while True:
       print("Welcome to RoboSpeaker Created by Disha")
       x = input("Enter what you want me to speak: ")
       if x == "q" :
           break
       command = f" PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');\""
       os.system(command)
