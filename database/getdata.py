import usermood

ob = usermood.addusermood()
data = ob.getFromUserMood()

file = open("dataset.arff",'a')
#file.write("userid, period, fear, disgust, anger, neutral, happiness, sad, surprise \n")

for row in data:
    for entry in row[:-1]:
        file.write(str(entry)+',')
    file.write(str(row[-1])+'\n')
file.close()