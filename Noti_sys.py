import time
from plyer import notification


if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please drink water",
            message = "Drinking accurate quantity of water is essential for every living being in order to stay healthy. We must drink adequate quantity of water daily to keep ourselves hydrated",
            app_icon = "D:\icon.ico",
            timeout=10
        )
        time.sleep(60*60)



