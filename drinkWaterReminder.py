import win32com.client
import time
from plyer import notification

speaker = win32com.client.Dispatch("SAPI.SpVoice")


while True:
    speaker.speak("Drink Water")  # It will speak in console fordrinking water

    notification.notify( # This will send us a notification
        title="Water Reminder",
        message="It's time to drink water!",
        app_name="Water Reminder App",
        timeout=3  # The notification will automatically close after 10 seconds
    )
    time.sleep(10)
        