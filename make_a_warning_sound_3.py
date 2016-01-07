#coding:utf-8
import pygame.mixer
import time

class make_a_warning_sound():

    def __init__(self,vol,playtime):
        self.vol = vol
        self.playtime = playtime


    def make_a_warning_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load('test.wav') #警告用サウンド読み込み
        pygame.mixer.music.play(1) #再生回数(1)
        pygame.mixer.music.set_volume(self.vol) #ボリューム設定
        time.sleep(self.playtime) #再生時間(s)
        pygame.mixer.music.stop() #再生を停止


if __name__==('__main__'):
    import pygame.mixer
    import time
    mws = make_a_warning_sound(0.5, 5)
    mws.make_a_warning_sound()

