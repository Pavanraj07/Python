from abc import ABC, abstractmethod

class Amplifier:
    def on(self):
        print("Amplifier on")

    def off(self):
        print("Amplifier off")

    def set_volume(self, volume):
        print(f"Amplifier volume set to {volume}")

class CdPlayer:
    def on(self):
        print("CdPlayer on")

    def off(self):
        print("CdPlayer off")

    def play(self, cd):
        print(f"Playing {cd} on CdPlayer")

class DvdPlayer:
    def on(self):
        print("DvdPlayer on")

    def off(self):
        print("DvdPlayer off")

    def play(self, dvd):
        print(f"Playing {dvd} on DvdPlayer")

class Projector:
    def on(self):
        print("Projector on")

    def off(self):
        print("Projector off")

    def focus(self):
        print("Projector focused")

class Screen:
    def down(self):
        print("Screen down")

    def up(self):
        print("Screen up")

class TheaterLights:
    def dim(self):
        print("Theater lights dimmed")

    def bright(self):
        print("Theater lights brightened")

class HomeTheatreFacade:
    def __init__(self):
        self.amplifier = Amplifier()
        self.cd_player = CdPlayer()
        self.dvd_player = DvdPlayer()
        self.projector = Projector()
        self.screen = Screen()
        self.theater_lights = TheaterLights()

    def watch_movie(self, movie):
        print("Getting ready to watch a movie...")
        self.theater_lights.dim()
        self.screen.down()
        self.projector.on()
        self.projector.focus()
        self.amplifier.on()
        self.amplifier.set_volume(5)
        self.dvd_player.on()
        self.dvd_player.play(movie)
        print("Enjoy the movie!")

    def end_movie(self):
        print("Shutting down movie theatre...")
        self.theater_lights.bright()
        self.screen.up()
        self.projector.off()
        self.amplifier.off()
        self.dvd_player.off()
        print("Movie theatre shut down.")

if __name__ == "__main__":
    home_theatre = HomeTheatreFacade()
    home_theatre.watch_movie("Inception")
    home_theatre.end_movie()
