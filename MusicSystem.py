"""Design and implement an Adapter Pattern for a Music System. """
class MusicPlayer:
    def play(self):
        pass

class Mp3Player:
    def play_mp3(self):
        print("Playing MP3 music")

class CdPlayer:
    def play_cd(self):
        print("Playing CD music")

class MusicPlayerAdapter(MusicPlayer):
    def __init__(self, player):
        self.adapter = player

    def play(self):
        if isinstance(self.adapter, Mp3Player):
            self.adapter.play_mp3()
        elif isinstance(self.adapter, CdPlayer):
            self.adapter.play_cd()

def main():
    mp3_player = Mp3Player()
    cd_player = CdPlayer()

    mp3_adapter = MusicPlayerAdapter(mp3_player)
    cd_adapter = MusicPlayerAdapter(cd_player)

    mp3_adapter.play() 
    cd_adapter.play()  

if __name__ == "__main__":
    main()