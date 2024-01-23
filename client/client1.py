import socket
import os

# Client-1
s = socket.socket()
host = 'localhost'
port = 23001
s.connect(('localhost', 23000))

output = input("download/upload?")

if output == "download":
    mssg = "download"
    s.send(mssg.encode())
    FileName = input("Enter Filename to Download from server: ")
    s.send(FileName.encode())

    # Specify the path where you want to save the downloaded file
    download_path = os.path.join("C:\\Users\\Amar\\Downloads\\CN-PROJECT\\client", FileName)

    with open(download_path, "wb") as DownloadFile:
        i = 1
        while True:
            Data = s.recv(1024)
            if not Data:
                break
            print('Receiving...%d' % i)
            DownloadFile.write(Data)
            i += 1
        print("Done Receiving")


elif output == "upload":
    mssg = "upload"
    s.send(mssg.encode())
    
    print(os.listdir("C:\\Users\\Amar\\Downloads\\CN-PROJECT\\client"))

    FileName = input("Enter Filename to Upload On server: ")
    s.send(FileName.encode())
    
    UploadFile = open("C:\\Users\\Amar\\Downloads\\CN-PROJECT\\client\\" + FileName, "rb")
    Read = UploadFile.read(1024)
    i = 1
    while Read:
        print("Sending...%d" % i)
        s.send(Read)  # sending 1KB
        Read = UploadFile.read(1024)
        i += 1
    print("Done Sending")
    UploadFile.close()

# Close the socket connection
s.close()
