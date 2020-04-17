import os
from datetime import datetime
import requests
import os.path


api_address = 'InsertAPIKey'
city = "INSERT_CITY"
blank = "''"

url = api_address + city

question = input("Hello, how can I help you today?: ")
if "time" in question:
    if "date" in question: 
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
if "weather" in question: 
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    print("")
    print("Luke, the weather forcast is: " + formatted_data)
    print("")
if "skript" in question: 
    SKName = input("What is the name of your skript going to be?: ")
    p = ('/Users/lukelucas/Documents/Skripts')
    completeName = os.path.join(p, SKName+".sk")
    file1 = open(completeName, "w")
    SKCommands = input("Do you want to create a command?: ")
    while SKCommands == "yes":
        SKCommandsName = input("What's the name of your command?: ")
        file1.write("command /" + SKCommandsName + ":\n" )
        SKCommandsPermissions = input("Will there be any permissions for this command?: ")
        if SKCommandsPermissions == "yes": 
            SKCommandsPermissionsPermission = input("What is the permission?: ")
            file1.write("   permission: " + SKCommandsPermissionsPermission + "\n")
            SKCommandsDescription = input("What is the description of your command?: ")
            file1.write("   description: " + SKCommandsDescription + "\n")
            file1.write("   trigger: \n")
            QuestionClearChat = input("Luke, I noticed the name of your command included clearchat. Do you want me to include the default clear chat command?: ")
            if QuestionClearChat == "yes": 
                file1.write("      loop 100 times: \n")
                file1.write("         broadcast " + blank + "\n")
                file1.write("      broadcast '&e%player% &fhas cleared the chat.' ")
            trytoBreakOut = input("Do you want to create another command?: ")
            if "yes" in trytoBreakOut: 
                file1.write("\n")
            else: 
                break
        else:
            SKCommandsDescription = input("What is the description of your command?: ")
            file1.write("   description: " + SKCommandsDescription + "\n")
            file1.write("   trigger: \n")
            if "clearchat" in SKCommandsName: 
                QuestionClearChat = input("Luke, I noticed the name of your command included clearchat. Do you want me to include the default clear chat command?: ")
                if QuestionClearChat == "yes": 
                    file1.write("      loop 100 times: \n")
                    file1.write("         broadcast " + blank + "\n")
                    file1.write("      broadcast '&e%player% &fhas cleared the chat.' ")
            trytoBreakOut = input("Do you want to create another command?: ")
            if "yes" in trytoBreakOut: 
                file1.write("\n")
            else: 
                break
