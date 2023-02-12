from tkinter import *
from tkinter import messagebox
import hashlib

mdp = Tk()
mdp.title("Password")
mdp.geometry("390x300")


textexigences = Label(mdp,text="""
- 8 caractères minimum
- Une lettre majuscule 
- Une lettre minuscule 
- Un chiffre                  
- Un caractère spécial """,font=("arial",10,"bold"),fg="black")
textexigences.place(x=120, y=165)

def verifier_password():
    mdp = entry_mdp.get()
    if len(mdp) >= 8:
        minuscule = False
        majuscule = False
        num = False
        carac = False

        for char in mdp:
            if char.isdigit():
                num = True
            if char.islower():
                minuscule = True
            if char.isupper():
                majuscule = True
            if not char.isalnum():
                carac = True

        if minuscule and majuscule and num and carac:
            messagebox.showinfo(title="ERREUR", message="Mot de passe accepté")
            mdp_crypter = motdepasse_crypter(mdp)
            messagebox.showinfo(title="Mot de passe crypté", message="Mot de passe crypté :" + mdp_crypter)
    else:
        messagebox.showerror(title="ERREUR", message="Erreur, votre mot de passe répond pas aux exigences.")


def motdepasse_crypter(mdp):
    return hashlib.sha256(mdp.encode()).hexdigest()



Texte = Label(mdp, text="Entrez un mot de passe", font=("arial",15,"bold"), fg="black")
Texte.place(x=90, y=30)

entry_mdp = Entry(mdp, font=("arial",10))
entry_mdp.place(x=125, y=100, height=30, width=120)

ok = Button(mdp, text="OK", fg="black", font=("arial",10), bg="grey", command=verifier_password)
ok.place(x=260, y=100, height=30, width=30)


mdp.mainloop()