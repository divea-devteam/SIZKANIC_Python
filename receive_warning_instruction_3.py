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

	print self.a
	print self.d
	print self.t

    def receive_warning_instruction(self):

	#URL
	url = 'http://192.168.33.10/test/json.php'

	#parames_encode
	params = {'dB' : self.a,'date':self.d,'time':self.t}
	params = urllib.urlencode(params)

	#URL_parames_bond
	URL = url + '?' + params

	print URL

	#server_reqest
	response = urllib2.urlopen(URL)

	#server_response
	content = response.read()
	#print(content)

        if '"go"' == content:
            self.mws.make_a_warning_sound()
        else:
            print "no"



if __name__ == '__main__':
    import make_a_warning_sound_2
    rwi = receive_warning_instruction(5,2015/12/25,1800,0.8,3)
    rwi.receive_warning_instruction()

