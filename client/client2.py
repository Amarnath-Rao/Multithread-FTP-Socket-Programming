import socket
import os

# Client-2
s = socket.socket()
host = 'localhost'
port = 49158
try:
    s.connect(('localhost', 23000))
    print("Connected Successfully!")
except Exception as e:
    print("something's wrong with %s:%d. Exception is %s" % (host, 23000, e))

Answer = input("download/upload?")

if Answer == "download":
    mssg = "download"
    s.send(mssg.encode())
    FileName = input("Enter Filename to Download from server: ")

    # Specify the path where you want to save the downloaded file
    download_path = os.path.join("C://Users//Amar//Downloads//CN-PROJECT//client", FileName)

    Data = "Temp"
    while True:
        s.send(FileName.encode())
        Data = s.recv(1024)
        DownloadFile = open(download_path, "wb")

        i = 1

        while Data:
            print('Receiving...%d' % i)
            DownloadFile.write(Data)
            Data = s.recv(1024)
            i = i + 1

        print("Done Receiving")
        DownloadFile.close()
        break

elif Answer == "upload":
    mssg = "upload"
    s.send(mssg.encode())
    
    print(os.listdir("C://Users//Amar//Downloads//CN-PROJECT//client//"))

    FileName = input("Enter Filename to Upload On server: ")
    s.send(FileName.encode())
    
    UploadFile = open("C://Users//Amar//Downloads//CN-PROJECT//client//" + FileName, "rb")
    Read = UploadFile.read(1024)
    i = 1
    while Read:
        print("Sending...%d" % i)
        s.send(Read)  # sending 1KB
        Read = UploadFile.read(1024)
        i += 1
    print("Done Sending")
    UploadFile.close()
    s.close()
