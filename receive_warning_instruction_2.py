# coding:utf-8
import make_a_warning_sound_2

class receive_warning_instruction():

    def __init__(self,param,vol,playtime):
        self.a = param
        #警告音再生インスタンス生成
        #()内はボリューム，再生時間
        self.mws = make_a_warning_sound_2.make_a_warning_sound(vol,playtime)


    def receive_warning_instruction(self):
        if self.a == 1:
            self.mws.make_a_warning_sound()
        else:
            print "鳴らさない"



if __name__ == '__main__':
    import make_a_warning_sound_2
    rwi = receive_warning_instruction(1,0.5,5)
    rwi.receive_warning_instruction()

