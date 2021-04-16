import tkinter as tk 
import tkinter.font as tkFont
from PIL import ImageTk, Image  

capital_alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter_to_index=dict(zip(capital_alphabet,range(len(capital_alphabet))))
# print(letter_to_index)
index_to_letter=dict(zip(range(len(capital_alphabet)),capital_alphabet))
# print(index_to_letter)

root=tk.Tk()
# root.geometry("500x500")
root.configure(bg="white")
logo=Image.open('vigenere.jpg')
logo=ImageTk.PhotoImage(logo)
image_lable=tk.Label(image=logo)
image_lable.image=logo
image_lable.pack()
Desired_font = tk.font.Font( family = "Comic Sans MS", 
                                 size = 20, 
                                 weight = "bold")
Desired_font2 = tk.font.Font( family = "Comic Sans MS", 
                                 size = 10, 
                                 weight = "bold")
title1=tk.Label(root,text='Cipher',font=Desired_font,bg="white")
title1.pack()
cipher=tk.Entry(root,width=50,borderwidth=5)
cipher.pack()
title2=tk.Label(root,text='Key',font=Desired_font,bg="white")
title2.pack()
key=tk.Entry(root, width=50,borderwidth=5)
key.pack()
def decrypt(cipher,key):
    decrypted_message=''
    splited_cipher=[cipher[i:i + len(key)]for i in range(0,len(cipher),len(key))]
    for each_splited_cipher in splited_cipher:
        i=0
        for letter in each_splited_cipher:
            number=(letter_to_index[letter]-letter_to_index[key[i]])%len(capital_alphabet)
            decrypted_message+=index_to_letter[number]
            i+=1
    return decrypted_message
def vigenere_decipher():
    c=cipher.get().upper()
    k=  key.get().upper()
    d=decrypt(c,k)
    output=tk.Label(root,text=d ,font=Desired_font2)
    output.pack()

mybutton=tk.Button(root,text="Decipher",bg="#20bebe",fg="white",height="2",width="15",command=vigenere_decipher,borderwidth=5)
mybutton.pack()
root.mainloop()

# def encrypt(message,key):
#     encrypted=''
#     split_message=[message[i:i + len(key)]for i in range(0,len(message),len(key))]
#     for each_split in split_message:
#         i=0
#         for letter in each_split:
#             number=(letter_to_index[letter]+letter_to_index[key[i]])%len(capital_alphabet)
#             encrypted+=index_to_letter[number]
#             i+=1
#     return encrypted