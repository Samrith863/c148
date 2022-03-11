from tkinter import *
import random
root=Tk()
root.title("Picnic")
root.geometry("400x400")
list_1=["apple","Id card","sunglasses","bread","chocolates","blanket"]
label_1=Label(root)
label_2=Label(root)
label_1['text']="put item "+str(list_1)+" in the basket"
def PutItems():
    random_number=random.sample(range(0,6),1)
    label_2['text']="put item no."+str(random_number)+" in the bag"
    



btn=Button(root,text="put items",bg="lightblue",fg="white",command=PutItems)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
label_2.place(relx=0.5,rely=0.5,anchor=CENTER)
label_1.place(relx=0.5,rely=.6,anchor=CENTER)
root.mainloop()

