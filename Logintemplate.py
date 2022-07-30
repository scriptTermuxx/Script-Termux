import sys, os ,time

x = 'example'
y = 'example'
def login():
    print ("login template")
    usr = raw_input("username : ")
    pas = raw_input("password : ")
    if usr ==x and pas ==y:
        print ("example text")
        time.sleep(2)
    else:
         print ("example text")
        
login()
