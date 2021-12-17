import kahoot
import threading
import utils

class Flooder:
    def __init__(self, gamepin, botname, amount, delay, window):
        self.gamepin = gamepin
        self.botname = botname
        self.amount = amount
        self.delay = delay
        self.window = window

        self.suffix = 0
        self.bot = kahoot.client()

    def loop(self):
        if self.suffix < int(self.amount):
            self.suffix += 1
            self.bot.join(int(self.gamepin), f"{self.botname} [{self.suffix}]")
            self.bot.on("joined")            

            self.window.after(int(self.delay), self.loop())

    def start(self):
        notifier = utils.Notifier()
        notifier.send("Kahoot Flooder", f"Starting flood with {self.amount} bots, GUI may hang.")

        self.window.after(int(self.delay), self.loop())