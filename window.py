from tkinter import *
from tkinter import filedialog

import file_enc as fe

import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#creer un premiere fenetre
window = Tk()
window.resizable(0,0)
window.title("B.S.E")
window.geometry("640x240")
window.minsize(640, 240)

#personaliser fenetre
label_title = Label(window, text = "Biomertic Security Applicaition", font=("", 20), pady=10, relief = SUNKEN)
label_title.pack()

label_subtitle = Label(window, text = "Une application de secutité biométrique.", pady= 30)
label_subtitle.pack()
#root frame

def pw_gen():
    
    password_provided = input.get()
    password = password_provided.encode()  # Convertion en octets

    salt = b'\xe2\xaf\xbc:\xdd'

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    fe.key = base64.urlsafe_b64encode(kdf.derive(password))# Assigner la variable 'key' ça valeur
    fe.fernet = fe.Fernet(fe.key)# Assigner la variable 'key' a l'algorithme de cryptage

    file = open('key.key', 'wb')# ouverture du fichier en mode ecriture binaire
    file.write(fe.key)
    file.close() 

#deuxieme fenetre
def open_db():
    
    top.filename = filedialog.askopenfilename(initialdir=fe.directory2,
                                                title="Select A File",
                                                filetypes=(("All files","*.*"),))

def open_original():
    top.filename = filedialog.askopenfile(initialdir=fe.directory,
                                            title="Select A File",
                                            filetypes=(("All files","*.*"),))


def open_random():

    global frame, key_text
    global top
    top = Toplevel()
    top.resizable(0,0)
    top.minsize(240, 240)
    top.title("Demonstration")

    frame = Frame(top)
    frame.pack()

    button1 = Button(frame, text="open DATABASE folder", command=open_db)
    button1.pack(pady=50)

def open_pw():

    global input
    top = Toplevel()
    top.resizable(0,0)
    top.minsize(240, 240)
    top.title("User Password Encryption")

    frame = Frame(top)
    frame.pack()

    label_top = Label(frame, text="Password input:", borderwidth=10 )
    label_top.pack()

    input = Entry(frame, width=30)
    input.config(show='*')
    input.pack(pady=5)

    button1 = Button(top,text="Encrypte", command=lambda: [f() for f in [pw_gen, fe.file_encrypt]])
    button1.pack(pady=5)

    button2 = Button(top,text="Decrypte", command=lambda: [f() for f in [pw_gen, fe.file_decrypt]])
    button2.pack(pady=5)

    button3 = Button(top,text="Open original DATABASE", command=open_original)
    button3.pack(pady=5)

    button4 = Button(top,text="Delete DATABASE", command=fe.file_delete_all)
    button4.pack(pady=5)
    
    

#creer boutton
button1 = Button(window, text="Demonstration", command=open_random, pady=5).pack(pady=5)
button2 = Button(window, text="Administrateur", command=open_pw, pady=5).pack(pady=5)

#affichage
window.mainloop()
