#coding:utf-8
class main():

    def __init__(self,rcdsec,playvol,playtime):
        #要検討
        self.rcdsec = rcdsec
        self.playvol = playvol
        self.playtime = playtime

    def main(self):

        for var in range(0,1):
            #騒音情報作成インスタンス生成
            cnd = create_noise_data_5.create_noise_data(self.rcdsec) #()内は録音時間(s)
            cnd.create_noise_data() #騒音情報作成メソッド

            #騒音情報送信インスタンス生成
            #()内は平均dB，算出日，時刻，警告要サウンドのボリューム，再生時間
            rwi = receive_warning_instruction_3.receive_warning_instruction(cnd.avg_dB,cnd.date,cnd.time,self.playvol,self.playtime)
##            rwi.receive_warning_instruction() #警告命令受信メソッド

if __name__ == '__main__':
    import create_noise_data_5
    import receive_warning_instruction_3
    import sys

    prms = sys.argv
    argv = sys.argv
    arglen = len(argv)

    if (arglen != 4):
        print 'Usage: # python %s filename' % argv[0]
        quit()         # プログラムの終了

    rcdsec = int(argv[1])
    playvol = float(argv[2])
    playtime = int(argv[3])

    mn = main(rcdsec,playvol,playtime)
    mn.main()
