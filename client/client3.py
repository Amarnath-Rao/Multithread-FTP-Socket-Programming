import socket
import threading
import os

s = socket.socket()
s.connect(('localhost', 23000))
print("Connected Successfully!")

try:
    Answer = input("download/upload? ")

    if Answer.lower() == "download":

        mssg = "download".encode()
        s.send(mssg)

        FileName = input("Enter Filename to Download from server : ")

        Data = "Temp"

        while True:

            s.send(FileName.encode())

            Data = s.recv(1024)

            DownloadFile = open(FileName,"wb")

            i = 1

            while Data:

                print('Receiving...%d' %(i))

                DownloadFile.write(Data)

                Data = s.recv(1024)

                i = i + 1

            print("Done Receiving")

            DownloadFile.close()

            break

    elif Answer.lower() == "upload":

        mssg = "upload".encode()
        s.send(mssg)

        print(os.listdir("C://Users//Amar//Downloads//CN-PROJECT//client//"))

        FileName = input("Enter Filename to Upload On server : ")

        s.send(FileName.encode())

        UploadFile = open("C://Users//Amar//Downloads//CN-PROJECT//client//"+FileName,"rb")

        Read = UploadFile.read(1024)

        i = 1

        while Read:

            print("Sending...%d" %(i))

            s.send(Read) #sending 1KB

            Read = UploadFile.read(1024)

            i = i + 1

        print("Done Sending")

        UploadFile.close()

except Exception as e: 
    print("something's wrong with localhost:23000. Exception is %s" % (e))

s.close()