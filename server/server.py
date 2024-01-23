import socket
import threading
import os

# Server Side

class ThreadServer:

    def __init__(self):
        self.host = 'localhost'
        self.port = 23000
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.host, self.port))

    def listen(self):
        self.s.listen(5)
        print("The server is listening...")
        while True:
            c, addr = self.s.accept()
            c.settimeout(60)
            threading.Thread(target=self.listen_to_client, args=(c, addr)).start()

    def listen_to_client(self, c, addr):
        block_size = 1024
        print('Got connection from', addr)
        data = c.recv(1024)

        if data.decode() == "download":
            print(os.listdir(r"C:\Users\Amar\Downloads\CN-PROJECT\server"))

            file_name = c.recv(1024)
            file_found = 0

            for file in os.listdir(r"C:\Users\Amar\Downloads\CN-PROJECT\server"):
                if file == file_name.decode():
                    file_found = 1
                    break

            if file_found == 0:
                print("Not Found On Server")
            else:
                print("File Found")
                upload_file = file_name.decode()
                upload_file_path = os.path.join(r"C:\Users\Amar\Downloads\CN-PROJECT\server", upload_file)
                with open(upload_file_path, "rb") as upload_file:
                    read_data = upload_file.read(1024)
                    i = 1
                    while read_data:
                        print("Sending...%d" % i)
                        c.send(read_data)  # 1KB sending
                        read_data = upload_file.read(1024)
                        i += 1
                print("Done Sending")
            # closing socket
            c.close()



        elif data.decode() == "upload":
            file_name = c.recv(1024)
            download_file_name = file_name.decode()
            download_file_path = os.path.join(r"C:\Users\Amar\Downloads\CN-PROJECT\server", download_file_name)

            with open(download_file_path, "wb") as download_file:
                i = 1
                while data:
                    print('Receiving...%d' % i)
                    download_file.write(data)
                    data = c.recv(1024)
                    i += 1
                print("Done Receiving")


        # Closing socket
        c.close()

if __name__ == "__main__":
    ThreadServer().listen()
