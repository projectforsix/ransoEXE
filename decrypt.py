import os
import sys
import time
import pyaes
import glob
from pathlib import Path
import threading

try:
    desktop = Path.home() / "OneDrive/Documentos" 
except Exception as error:
    pass

os.chdir(desktop)

# abrir o arquivo novamente
def descrypter():
    try:
        
        for filling in glob.glob('*.ransomEXE'):
            file = open(filling, 'rb')
            filedata = file.read()
            file.close()

            # chave para decrypt

            key = b"NUnN9502jasaiN0m"
            aes = pyaes.AESModeOfOperationCTR(key)
            decrypt_data = aes.decrypt(filedata)

            # remover o arq ciptografado

            novofile = open(f'{desktop}\\{novofile}', 'wb')
            novofile.write(decrypt_data)
            novofile.close()
            
    except:
        pass
    
if __name__ == "__main__":
    descrypter()

threading.Thread(target=descrypter).start()