import os
from cryptography.fernet import Fernet
from tkinter import messagebox

# Les directoire de la base de donées et le dossier des resultats
directory = 'C:\Programation\Python\Enc_Proj\MATLAB_FingerPrint-master\DB'
directory2 = 'C:\Programation\Python\Enc_Proj\enc'
directory3 = 'C:\Programation\Python\Enc_Proj\dec'

    
file = open('key.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()

#message boxes

def status_info(message):
    messagebox.showinfo("Status Report", message)

def status_confirm(message):
    return messagebox.askyesno("Status Report", message)

# partie cryp/decryp
def file_encrypt():

    global fernet
    for filename in os.listdir(directory):
        # ouverture de la bdd en mode écriture
        file = os.path.join(directory, filename)
        with open(file, 'rb') as f:
            # passage des données du dossier a la variable 'data'
            data = f.read()  
        # Cryptage des données avec l'algorithme Fernet
        encrypted = fernet.encrypt(data) 

        # mettre les images crypter dans le dossier
        with open("enc\\" + filename[:-4] + ".encrypted", 'wb') as f:

            f.write(encrypted)  

    file_delete('.tif')# suppression des données précédentes   
    # message de confirmation
    msg = "Encryption complete, resault in " + directory2
    status_info(msg)    
    

def file_decrypt():

    for filename in os.listdir(directory2):
        # ouverture de la bdd en mode lecture
        with open("enc\\" + filename, 'rb') as f:
            # passage des données du dossier a la variable 'data'
            data = f.read()
        # Decryptage des données avec l'algorithme Fernet
        decrypted = fernet.decrypt(data)

        # mettre les images Decrypter dans le dossier
        with open("enc\\" + filename[:-10] + ".tif" , 'wb') as f :
            
            f.write(decrypted)

    file_delete('.encrypted')# suppression des données précédentes  
    # message de confirmation
    msg = "Decryption complete, resault in " + directory2
    status_info(msg)
               
# func supp
""" def file_delete_enc():
    msg = "Delete encrypted files ?"
    response = status_confirm(msg)
    if response:
        for filename in os.listdir(directory2) :
            os.remove(directory2 + "\\" + filename) """
    

""" def file_delete_dec():
    msg = "Delete decrpyted files ?"
    response = status_confirm(msg)
    if response:
        for filename in os.listdir(directory3) :
            os.remove(directory3 + "\\" + filename) """
   
def file_delete_all():
    #parcourir les images
    for filename in os.listdir(directory2):
        #la suppression des images
        os.remove(os.path.join(directory2, filename))

def file_delete(end):
    #parcourir les images
    for filename in os.listdir(directory2):
        #la suppression des images basé sur l'extension(soit'.tif' ou '.encrypted')
        if filename.endswith(end):
            os.remove(os.path.join(directory2, filename))
