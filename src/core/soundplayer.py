from pygame import mixer

class SoundPlayer:
    def __init__(self):
        self.cache = {}

    def play_music(self, music):
        mixer.music.load(music)
        mixer.music.play(-1)

    def play_sound(self, path, volume):
        if path not in self.cache:
            self.cache[path] = mixer.Sound(path)
        sound = self.cache[path]
        sound.set_volume(volume)
        sound.play()