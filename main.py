#coding:utf-8
class main():

    def __init__(self):
        #要検討
        self.a = 0

    def main(self):

        #騒音情報作成インスタンス生成
        cnd = create_noise_data_3.create_noise_data(60) #()内は録音時間(s)
        cnd.create_noise_data() #騒音情報作成メソッド

        #騒音情報送信インスタンス生成
        #()内は平均dB，算出日，時刻，警告要サウンドのボリューム，再生時間
        rwi = receive_warning_instruction_3.receive_warning_instruction(cnd.avg_dB,cnd.date,cnd.time,0.8,3)
        rwi.receive_warning_instruction() #警告命令受信メソッド


if __name__ == '__main__':
    import create_noise_data_3
    import receive_warning_instruction_3
    mn = main()
    mn.main()
