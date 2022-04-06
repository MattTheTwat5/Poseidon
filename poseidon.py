import requests
import time


print()
print()
print("                              ====================================================================")
print("                              ||  ██████╗░░█████╗░░██████╗███████╗██╗██████╗░░█████╗░███╗░░██╗  ||")
time.sleep(0.2)
print("                              ||  ██╔══██╗██╔══██╗██╔════╝██╔════╝██║██╔══██╗██╔══██╗████╗░██║  ||")
time.sleep(0.2)
print("                              ||  ██████╔╝██║░░██║╚█████╗░█████╗░░██║██║░░██║██║░░██║██╔██╗██║  ||")
time.sleep(0.2)
print("                              ||  ██╔═══╝░██║░░██║░╚═══██╗██╔══╝░░██║██║░░██║██║░░██║██║╚████║  ||")
time.sleep(0.2)
print("                              ||  ██║░░░░░╚█████╔╝██████╔╝███████╗██║██████╔╝╚█████╔╝██║░╚███║  ||")
time.sleep(0.2)
print("                              ||  ╚═╝░░░░░░╚════╝░╚═════╝░╚══════╝╚═╝╚═════╝░░╚════╝░╚═╝░░╚══╝  ||")
time.sleep(0.2)
print("                              ||                                                                ||")
time.sleep(0.2)
print("                              ||    -by MattTheTwat5                                            ||")
time.sleep(0.2)
print("                              ====================================================================")
print()
print("                                     <1.>  FAKE IP GRABBER           <2.>  CHATFLOOD ATTACK")
time.sleep(1)
print()
print()


#variables
choice = ""
prank = ""
flood = ""
flood_message = ""

choice = input("<<< WHAT KIND OF ATTACK DO YOU WANT TO LAUNCH (SEPERATION WITH ,) >>>  \n")



#inputs
API = input("Enter a discord channel API link: \n")
print()
token = input("Enter your didcord token: \n")
print()
tts = input("Do you want the message to be in text to speech? \n")
print()


#checking what kind of attack the user wants to use
if choice == "1":
    prank = "Y"
    flood = "N"

if choice == "2":
    flood = "Y"
    prank = "N"



#flooding message
if flood == "Y":
    message_count = float(input("<<< HOW MANY MESSAGES DO YOU WANT TO SEND >>> \n"))  #float makes the input a number instead of a string (a float makes it so the string will become a number)

if flood == "Y":
    flood_message = input("<<< WHAT DO YOU WANT THE CHATFLOOD TO SPAM >>> \n")
elif flood == "N":
    print()

#tts
if tts == "Y":
    tts = "true"
elif tts == "N":
    tts == "false"


#flood message content
if flood == "Y":
    payload = {
        "content": flood_message,
        "tts": tts
    }
elif flood =="N":
    print()


#other messages
payload_2 = {
    "content": "``<<< LAUNCHING CHATFLOOD ATTACK... >>>``"
}

payload_3 = {
    "content": "``<<< GRABBING IP... >>>``"
}

payload_4 = {
    "content": "``<<< SAVING IP... >>>``"
}

payload_5 = {
    "content": "``<<< TARGET LOCATION SAVED... >>>``"
}



#dc token
header = {
    "authorization": token
}




#bit of making it look cool
if flood == "Y":
    r = requests.post(API, data = payload_2, headers = header)
elif flood == "N":
    print()

if prank == "Y":
    time.sleep(0.5)
    r = requests.post(API, data = payload_3, headers = header)
    time.sleep(0.5)
    r = requests.post(API, data = payload_4, headers = header)
    time.sleep(0.5)
    r = requests.post(API, data = payload_5, headers = header)
    time.sleep(3)
elif prank == "N":
    print()


#spam part
if flood == "Y":
    i = 0
    while i != message_count:
        time.sleep(0.5)
        r = requests.post(API, data = payload, headers = header)
        i = i + 1
elif flood == "N":
    print()

print("<<< ATTACK ENDED >>>")
