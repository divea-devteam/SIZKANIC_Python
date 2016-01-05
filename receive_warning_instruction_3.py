# coding:utf-8
import make_a_warning_sound_2
import urllib
import urllib2
import json

class receive_warning_instruction():

    def __init__(self,avg_dB,date,time,vol,playtime):
    	self.a = avg_dB
    	self.d = date
     	self.t = time

        #警告音再生インスタンス生成
        #()内はボリューム，再生時間
        self.mws = make_a_warning_sound_2.make_a_warning_sound(vol,playtime)

        #テスト用
    	print self.a
    	print self.d
    	print self.t

    def receive_warning_instruction(self):

    	#URLを指定する
    	url = 'http://192.168.33.10/test/json.php'

    	#平均dB値，算出日，算出時刻のパラメータ作成
    	params = {'dB' : self.a,'date':self.d,'time':self.t}
        #パラメータをエンコードする
    	params = urllib.urlencode(params)

    	#パラメータをURLに結合する
    	URL = url + '?' + params

    	print URL

    	#サーバにリクエストを送る
    	response = urllib2.urlopen(URL)

    	#サーバからレスポンスを受け取る
    	content = response.read()

    	#print(content)

        #警告音を鳴らす命令を受け取った場合警告音を鳴らすメソッドを呼び出す
        #鳴らさない命令を受け取った場合何もしない
        if '"go"' == content:
            self.mws.make_a_warning_sound()
        else:
            print "no"


if __name__ == '__main__':
    import make_a_warning_sound_2
    rwi = receive_warning_instruction(5,2015/12/25,1800,0.8,3)
    rwi.receive_warning_instruction()

