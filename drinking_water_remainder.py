import time
from plyer import notification

while True:
    notification.notify(
        title="*Take a break!*",
        message="Drink some water !",
        app_icon="C:/Users/parvp/Downloads/Icon.ico",
        timeout=5
    )


    time.sleep(10)
