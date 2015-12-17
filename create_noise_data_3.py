# coding: utf-8

import datetime
import pyaudio
import sys
import time
import wave
from scipy import fromstring, int16
import math

class create_noise_data():

    def __init__(self,rcdsec):
        self.rcdsec = rcdsec
        self.avg_dB = 0
        self.data = 0
        self.time = 0

    def create_noise_data(self):
        #マイクで1分間録音
        chunk = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        #サンプリング周波数
        RATE = 44100
        #録音時間(s)
        RECORD_SECONDS = self.rcdsec

        #pyaudioのインスタンス生成
        p = pyaudio.PyAudio()

        #マイク0番
        input_device_index = 0
        #マイクからデータ取得
        stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = chunk)
        all = []
        for i in range(0, RATE / chunk * RECORD_SECONDS):
            data = stream.read(chunk)
            all.append(data)

        stream.close()

        #結合
        data = ''.join(all)
        #WAVEファイル作成
        out = wave.open('noise_data.wav','w')
        out.setnchannels(2) #モノラル
        out.setsampwidth(2) #16bits
        out.setframerate(RATE)
        out.writeframes(data)
        out.close()

        wr = wave.open("noise_data.wav", "r")
        #waveファイルの音圧データを読み込む
        w_data = wr.readframes(wr.getnframes())
        #文字型から数値型に
        w_num_data = fromstring(w_data, dtype = int16)
        #各数値の絶対値をとる
        w_num_data = map(abs, w_num_data)

        #音圧の平均値を求める
        avg_vol = float(sum(w_num_data))/float(len(w_num_data))
        avg_vol = math.fabs(avg_vol)
        #デシベルに変換
        self.avg_dB = 20*math.log10(avg_vol/1)

        #現在日付・時刻のdatetime型データの変数を取得
        d = datetime.datetime.today()
        #strftime()メソッドで日付時刻の書式を指定して出力
        self.date = d.strftime("%Y/%m/%d")
        self.time = d.strftime("%H:%M:%S")

        #pyaudioを閉じる
        p.terminate()


if __name__=='__main__':
    import datetime
    import pyaudio
    import sys
    import time
    import wave
    from scipy import fromstring, int16
    from math import *
    cnd = create_noise_data(10)
    cnd.create_noise_data()







