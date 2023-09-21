import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
listOfName = ["Welcome Moin","Hello Abdul","Sorry to Saqlain","Hardware Zeeshan","Tracker Vivek"]
for lon in listOfName:
    speaker.Speak(lon)