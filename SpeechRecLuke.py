import speech_recognition as sr
import os
from datetime import datetime
import requests
import os.path

r = sr.Recognizer()
m = sr.Microphone()
api_address = 'INSERT_API'
city = "CITY"
blank = "''"
url = api_address + city


try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print("Please run this in Python 3, I am no longer updating this project for Python 2. If you'd like to know why have a read up on Chaos Theory.")
            else:  # this version of Python uses unicode for strings (Python 3+)
                if "time" in value: 
                    if "date" in value: 
                        now = datetime.now()
                        current_time = now.strftime("%D %H:%M & the seconds are %S")
                        print("")
                        print("Luke the current date & time is: " + current_time)
                        print("")
                    else: 
                        now = datetime.now()
                        current_time = now.strftime("%H:%M & the seconds are %S")
                        print("")
                        print("Luke the current time is: " + current_time + ".")
                        print("")
                if "weather" in value: 
                    json_data = requests.get(url).json()
                    formatted_data = json_data['weather'][0]['description']
                    print("")
                    print("Luke, the weather forcast is: " + formatted_data)
                    print("")
                if "script" in value: 
                    with m as source: r.adjust_for_ambient_noise(source)
                    print("What is the name of your skript?: ")
                    with m as source: audio = r.listen(source)
                    print("Created your Skript!")
                    filedirct = ('/Users/lukelucas/Documents/Skripts')
                    value = r.recognize_google(audio)
                    value = "_".join(value.split())
                    completeName = os.path.join(filedirct, value +".sk")
                    file1 = open(completeName, "w")
                    print(value + ".sk has been created.")
                    with m as source: r.adjust_for_ambient_noise(source)
                    print("Do you want to create any commands?: ")
                    with m as source: audio = r.listen(source)
                    value = r.recognize_google(audio)
                    if "yes" in value: 
                        with m as source: r.adjust_for_ambient_noise(source)
                        print("What is the name of your command?: ")
                        with m as source: audio = r.listen(source)
                        value = r.recognize_google(audio)
                        value = "_".join(value.split())
                        file1.write("command /" + value + ":\n" )
                        with m as source: r.adjust_for_ambient_noise(source)
                        print("Do you want any permissions?: ")
                        with m as source: audio = r.listen(source)
                        value = r.recognize_google(audio)
                        if "yes" in value: 
                            with m as source: r.adjust_for_ambient_noise(source)
                            print("What is the name of your permission?: ")
                            with m as source: audio = r.listen(source)
                            value = r.recognize_google(audio)
                            value = ".".join(value.split())
                            file1.write("   permission: " +  value + "\n")
                            with m as source: r.adjust_for_ambient_noise(source)
                            print("What is the description of your command?: ")
                            with m as source: audio = r.listen(source)
                            value = r.recognize_google(audio)
                            file1.write("   description: " + value + "\n")
                            file1.write("   trigger: \n")
                if "stop" in value: 
                    break
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
