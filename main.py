#coding:utf-8
class main():

    def __init__(self):
        self.a = 0

    def main(self):

        #騒音情報作成インスタンス生成
        cnd = create_noise_data_3.create_noise_data(10) #()内は録音時間(s)
        cnd.create_noise_data() #騒音情報作成メソッド

        #騒音情報送信インスタンス生成
        #()内は平均dB，算出日，時刻，エリアID，Raspberry Pi ID
        sdts = send_data_to_server_2.send_data_to_server(cnd.avg_dB,cnd.date,cnd.time,"flor1","RP1_1")
        sdts.send_data_to_server() #騒音情報送信メソッド

        #警告命令受信インスタンス生成
        #()内はflag(1:再生)，ボリューム，再生時間(s)
        rwi = receive_warning_instruction_2.receive_warning_instruction(1,0.5,5)
        rwi.receive_warning_instruction() #警告命令受信メソッド


if __name__ == '__main__':
    import create_noise_data_3
    import send_data_to_server_2
    import receive_warning_instruction_2
    mn = main()
    mn.main()
