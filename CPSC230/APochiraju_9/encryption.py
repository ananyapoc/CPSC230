#nikita,gabriel,and zach all helped thank them for me please with an extra point or something
import operator
def readFile(myfile):
    file=open(myfile,"r")
    filecontents=file.readlines()
    filestring="".join(filecontents)
    file.close()
    return filestring

def writeFile(str,fileName):
    file = open(fileName,"w")
    file.write(str)  #writes string to new file
    file.close()

def encrypt(str,shift):
    encryptedtxt = ""
    for item in str:
        if (item.isalpha()) == True:
            item=item.lower()
            ASCII=ord(item)+shift
            if(ASCII>122):               #z is 122
                ASCII=(ASCII-122)+96      #a is 97
            encryptedtxt=encryptedtxt+chr(ASCII)
        else:
            encryptedtxt+=item #spaces and apostrophes or such
    return encryptedtxt

def buildDictionary(encryptedstr):
    dict={}
    for item in encryptedstr:
        if (item.isalpha())==True:
            if item in dict:
                dict[item]=dict[item]+1 #reoccuring letter
            else:
                dict[item]=1  #one time appearance
    return dict

def findShift(encryptedstr):
    frequency=buildDictionary(encryptedstr)
    letter = max(frequency.items(), key=operator.itemgetter(1))[0]
    shift = abs(ord(letter)-101)  #nikita helped me with this line; to find the shift number
    return shift

def decrypt(encryptedstr):
    shift=findShift(encryptedstr)
    originaltext=""
    for item in encryptedstr:
        if (item.isalpha())==True:
            newASCII=ord(item)-shift
            if(newASCII<97):
                newASCII+=26
            originaltext+=chr(newASCII)  #decrypt the text using ASCII
        else:
            originaltext+=item
    return originaltext

writeFile(encrypt(readFile("hp.txt"),3),"encrypted.txt")   #encrypting the code
writeFile(decrypt(readFile("encrypted.txt")),"decrypted.txt")   #decrypting the code 
















'''readFile("hello.txt")
writeFile(readFile("hello.txt"),"goodbye.txt")
writeFile(encrypt(readFile("hello.txt"),3),"goodbye.txt")'''
