from poll import Updater

TOKEN = "1436034831:YPhRWhXUze7d7SiqaLRxIrJJbvpHHPjlKJFI2kqi"


class MyUpdater(Updater):
    async def on_response(self, message):
        print(message)

updater = MyUpdater(TOKEN)

updater.start_polling()


