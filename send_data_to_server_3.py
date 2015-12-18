# coding:utf-8

import urllib, urllib2
import SimpleHTTPServer
import SocketServer


class send_data_to_server():

    def __init__(self,avg_dB,date,time,AreaID,RPID):
        self.avg_dB = avg_dB
        self.date = date
        self.time = time
        self.AreaID = AreaID
        self.RPID = RPID
        PORT = 8000

        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

        httpd = SocketServer.TCPServer(("", PORT), Handler)

        print "serving at port", PORT
        httpd.serve_forever()

##    def send_data_to_server(self):
##        print self.avg_dB
##        print self.date
##        print self.time
##        print self.AreaID
##        print self.RPID

    def real_send_data_to_server(self):

        #データを送信するURL
        url = 'localhost:8000/user.php'
        #送信するデータ(辞書型)
        params = {'avg_dB' : 1,
                  'date' : "2015/12",
                  'time' : "10:10"}

        #送信するデータをエンコードする
        params = urllib.urlencode(params)
        #リクエスト送信
        req = urllib2.Request(url + '?' + params)
        print url + '?' + params
##        responce = urllib2.urlopen('http://local:8000/user.php?id=8&name=yoshi')
##
####        #リクエストしたURLのレスポンスオブジェクト(ファイルライクオブジェクト)が帰ってくる
####        response = urllib2.urlopen(req)
####        #
##        body = response.read()

if __name__==('__main__'):
    import urllib, urllib2
    sdts = send_data_to_server(1,2,3,4,5)
    sdts.real_send_data_to_server()
