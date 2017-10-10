# -*- coding: utf-8 -*-
import urllib2
import urllib
import time
import json

def connectandget(filename):
    http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
    key = "AkJVea24vCoybWL_f_3R1Dn424Uw1gn2"
    secret = "03oALQ-P5PU3v9PXUDldsuo3K7KG-ry2"
    filepath = filename
    attribute='emotion'
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
    data.append(attribute)
    data.append('--%s' % boundary)
    fr=open(filepath,'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename="co33.jpg"' % 'image_file')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr.read())
    fr.close()
    data.append('--%s--\r\n' % boundary)

    http_body='\r\n'.join(data)
    #buld http request
    req=urllib2.Request(http_url)

    #header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    req.add_data(http_body)
    try:
        #post data to server
        if(json.load(urllib2.urlopen(req, timeout=10))['faces']):
            resp = json.load(urllib2.urlopen(req, timeout=10))['faces'][0]['attributes']['emotion']
        else :
            return "no face found"
        #get response
        #qrcont=resp.read()
        print '1'
        #print resp
        return resp
    except urllib2.HTTPError as e:
        print e.read()
        return e

if __name__=='__main__':
    connectandget('C:/Users/Harshit Soni/Downloads/sad.jpg')