import os
import time
import webbrowser
import pyttsx3
import speech_recognition as sr

print("Hello! I'm an application that can help you open different programs easily")
pyttsx3.speak("Hello! I'm an application that can help you open different programs easily")
time.sleep(1)
print("Let's see the different tasks that I can perform...")
pyttsx3.speak("Let's see the different tasks that I can perform...")
time.sleep(1)
print("***************************")
print("I can open:")
print("1. Google Chrome")
print("2. Notepad")
print("3. Calculator")
print("4. Windows Media Player")
print("5. Valorant Game")
print("6. Linkedin")
print("7. Facebook")
print("8. Whatsapp")
print("9. Visual Studio Code")
print("10. Google Meet")
print("11. Google Something...")
print("12. Hibernate the System")
print("13. Launch a Docker Instance")
print("***************************")
print("So here we go...",end="")
pyttsx3.speak("So here we go...")
time.sleep(1)
pyttsx3.speak("What would you like me to do?")

while True:
    print()
    print("What would you like me to do?")
    
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Start Saying...")
            pyttsx3.speak("Start Saying...")
            audio = r.listen(source)
            print("We Got it! Speech Done!")
            pyttsx3.speak("We Got it! Speech Done!")
        opt = r.recognize_google(audio).lower()
    except:
        print("Sorry I didn't catch that.")
        pyttsx3.speak("Sorry I didn't catch that.")
        
        
    if("don't" in opt or "do not" in opt):
        print("Query incorrect, Try again...")
        pyttsx3.speak("Query incorrect, Try again...")
        
    elif( ("chrome" in opt) ):
        #webbrowser.open("http://192.168.249.130/cgi-bin/{}1.py?x=date")
        pyttsx3.speak("Opening Google Chrome.")
        os.system("chrome")
        
    elif(("notepad" in opt) or ("editor" in opt) or ("note" in opt)):
        pyttsx3.speak("Opening Note Pad.")
        os.system("notepad")
        
    elif(("calculator" in opt) or ("calculation" in opt)):
        pyttsx3.speak("Opening Calculator.")
        os.system("calc")
        
    elif(("media" in opt) or ("player" in opt)):
        pyttsx3.speak("Opening Windows Media Player.")
        os.system("wmplayer")
        
    elif(("valorant" in opt) or ("game" in opt)):
        pyttsx3.speak("Starting Valorant. Please Wait.")
        os.chdir(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games")
        os.system("start VALORANT")
        
    elif(("linkedin" in opt)):
        pyttsx3.speak("Opening Linkedin")
        os.system("start https://www.linkedin.com")
        
    elif(("facebook" in opt) or ("fb" in opt)):
        pyttsx3.speak("Opening Facebook")
        os.system("start https://www.facebook.com")
        
    elif(("whatsapp" in opt)):
        pyttsx3.speak("Opening Whatsapp. Happy Chatting!")
        os.system("start https://web.whatsapp.com/")
        
    elif(("visual studio" in opt) or ("code" in opt)):
        pyttsx3.speak("Opening VS Code. Happy Coding!")
        os.system("Code")
        
    elif(("hibernate" in opt) or ("shut down" in opt) or ("shutdown" in opt)):
        pyttsx3.speak("Hibernating System. Bye!")
        os.system("shutdown /h")
        
    elif(("meet" in opt) or ("class" in opt))or(("google" in opt) and ("meet" in opt)):
        print("Enter the google meet code (Without the -):")
        pyttsx3.speak("Type in the google meet code")
        print()
        meet_code=input()
        pyttsx3.speak("Staring Google meet session.")
        os.system("start https://meet.google.com/lookup/"+"{}".format(meet_code))
        
    elif(("google" in opt) or ("browse" in opt)):
        pyttsx3.speak("Please type what you want to search for?")
        print("Type what you want to search for?")
        search=input()
        os.system("start https://www.google.com/search?q={}".format(search,search))

    elif(("docker" in opt)):
        pyttsx3.speak("Here you go!")
        os.system("start http://192.168.0.7/drun.html")
        
    elif("exit" in opt or "bye" in opt or "quit" in opt):
        print("Good Bye! Have a Great Day!")
        pyttsx3.speak("Good Bye! Have a Great Day!")
        break
    
    else:
        print("Query incorrect, Try again...")
        pyttsx3.speak("Query incorrect, Try again...")
