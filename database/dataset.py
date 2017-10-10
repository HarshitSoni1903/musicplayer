from Controls import apiconnect
import os
import tkFileDialog
class dataset:
    def __init__(self):
        pass

    def ensure_str(self,s):
        if isinstance(s, unicode):
            s = s.encode('utf-8')
        return s


    def startcreate(self):
        self.filelink = tkFileDialog.askdirectory(title="select directory to create dataset")
        print self.filelink
        self.files=[]
        for filename in os.listdir(self.filelink):
                    if filename.endswith(".jpg"):
                        print filename
                        self.files.append(self.ensure_str(filename))
        print self.files
dset = dataset()
dset.startcreate()
data = open("dataset.arff",'a')
print dset.files
i=0

while i<(len(dset.files)-1):
    filenamewithext=dset.files[i]
    filenamewoext = filenamewithext.split('.')[0]
    filecurrent = dset.filelink +'/' + dset.files[i]
    print filecurrent
    response=apiconnect.connectandget(filecurrent)
    print response
    i=i+1
    data.write(str(response['neutral'])+','+str(response['sadness'])+','+str(response['disgust'])+','+str(response['anger'])+','+str(response['surprise'])+','+str(response['fear'])+','+str(response['happiness'])+','+filenamewoext+'\n')
data.close()
