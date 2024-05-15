# replace the ./Frames/game_play/components/audio.py with this code if the computer has no audio
# became lazy to integrate it with disabled audio feature


import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'  # Set the audio driver to dummy (no audio)
import pygame

class Audio:
    def __init__ (self):
        pygame.mixer.init()
        pygame.init()
        
    def correct(self):
        pygame.mixer.music.load("./assets/audios/audios_correct.mp3")  # Load the audio file
        pygame.mixer.music.play()  # Play the audio
        
    def wrong(self):
        pygame.mixer.music.load("./assets/audios/audios_wrong.mp3")  # Load the audio file
        pygame.mixer.music.play()  # Play the audio
        
    def win(self):
        pygame.mixer.music.load("./assets/audios/audios_win.mp3")  # Load the audio file
        pygame.mixer.music.play()  # Play the audio

    def lose(self):
        pygame.mixer.music.load("./assets/audios/audios_lose.mp3")  # Load the audio file
        pygame.mixer.music.play()  # Play the audio
        
    def click(self):
        pygame.mixer.music.load("./assets/audios/button_click.mp3")  # Load the audio file
        pygame.mixer.music.play()  # Play the audio
        
    def skill(self, character: str, skill_number: str):
        pygame.mixer.music.load(f"./assets/audios/{character}_skill_{skill_number}_audio.mp3")  # Load the audio file
        pygame.mixer.music.play()  # Play the audio
        
play_audio = Audio()
