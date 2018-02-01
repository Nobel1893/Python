import urllib
def readfile (name):
    myfile=open(name)
    text=myfile.read()
    myfile.close()
    
    return text

def checkProfanity(word):
    con=urllib.urlopen("http://www.wdylike.appspot.com/?q="+word)
    res=con.read()
    return res

def checkfileprofanity(fileurl):
    text=readfile(fileurl)
    mylist=text.split(" ")
    for word in mylist:
        print "checking word : "+word
        if checkProfanity(word) == "true":
            print "profanity detected : "+word
        


checkfileprofanity("file_path")
