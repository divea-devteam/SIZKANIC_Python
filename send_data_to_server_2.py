# coding:utf-8

import urllib, urllib2

class send_data_to_server():

    def __init__(self,avg_dB,date,time,AreaID,RPID):
        self.avg_dB = avg_dB
        self.date = date
        self.time = time
        self.AreaID = AreaID
        self.RPID = RPID

    def send_data_to_server(self):
        print self.avg_dB
        print self.date
        print self.time
        print self.AreaID
        print self.RPID

    def real_send_data_to_server():
        #データを送信するURL
        url = ''
        #送信するデータ(辞書型)
        values = {'avg_dB' : 1,
                  'date' : "2015/12",
                  'time' : "10:10"}

        #送信するデータをエンコードする
        data = urllib.urlencode(values)
        #リクエスト送信
        req = urllib2.Request(url, data)
        #リクエストしたURLのレスポンスオブジェクト(ファイルライクオブジェクト)が帰ってくる
        response = urllib2.urlopen(req)
        #
        the_page = response.read()

if __name__==('__main__'):
    import urllib, urllib2
    send_data_to_server()
