global one

def int():
    global one
    while True:
        i = int(raw_input("enter a number"))
        if(i==0):
            exit(False)
        else:
            one=str(i)
