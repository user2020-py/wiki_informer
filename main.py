import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import PhotoImage

w = 460; h = 335
window = tk.Tk()
window.title("Wiki Informer UZ-RU-EN")
ww = window.winfo_reqwidth()
wh = window.winfo_reqheight()
pr = int(window.winfo_screenwidth()/2 - ww/2)
pd = int(window.winfo_screenheight()/2 - wh/2)
window.geometry("+{}+{}".format(pr, pd))
window.maxsize(width=w, height=h)
window.minsize(width=w, height=h)
window.configure(background='skyblue')

from tkinter import*
from PIL import ImageTk, Image
import os
import wikipedia
from googletrans import Translator
from datetime import date
result_global = str()

class result_lang:
    def uz(t, a):
        try:
            translator = Translator()
            translated = translator.translate(t, src='uz', dest='en').text
            itemsforlistbox= wikipedia.search(translated)
            r = list()
            for k in itemsforlistbox:
                r.append(translator.translate(k, src='en', dest='uz').text)
            root=Tk()
            root.title('Search results')
            
            def CurSelet(evt):
                values = [mylistbox.get(idx) for idx in mylistbox.curselection()]
                a.set(', '.join(values))
                ok['state']='enable'
                root.destroy()
            mylistbox=Listbox(root, font=('times',13), width=100, height=len(itemsforlistbox))
            mylistbox.bind('<<ListboxSelect>>',CurSelet)
            mylistbox.pack()
            for items in r:
                mylistbox.insert(END,items)
            root.mainloop()
        except:
            messagebox.showerror('App', "Connect Error or content not found")
        
################
    def ru(t, a):
        try:
            root1=Tk()
            translator = Translator()
            translated = translator.translate(t, src='ru', dest='en').text
            itemsforlistbox= wikipedia.search(translated)
            r = list()
            for k in itemsforlistbox:
                r.append(translator.translate(k, src='en', dest='ru').text)
            root1.title('Search results')
            
            def CurSelet(evt):
                values = [mylistbox.get(idx) for idx in mylistbox.curselection()]
                a.set(', '.join(values))
                ok['state']='enable'
                root1.destroy()
            mylistbox=Listbox(root1, font=('times',13), width=100, height=len(itemsforlistbox))
            mylistbox.bind('<<ListboxSelect>>',CurSelet)
            mylistbox.pack()
            for items in r:
                mylistbox.insert(END,items)
            root1.mainloop()
        except:
            messagebox.showerror('App', "Connect Error or content not found")
################3    
    def en(t, a):
        try:
            translator = Translator()
            itemsforlistbox= wikipedia.search(t)
            root=Tk()
            root.title('Search results')
            
            def CurSelet(evt):
                values = [mylistbox.get(idx) for idx in mylistbox.curselection()]
                a.set(', '.join(values))
                ok['state']='enable'
                root.destroy()
            mylistbox=Listbox(root, font=('times',13), width=100, height=len(itemsforlistbox))
            mylistbox.bind('<<ListboxSelect>>',CurSelet)
            mylistbox.pack()
            for items in itemsforlistbox:
                mylistbox.insert(END,items)
            root.mainloop()
        except:
            messagebox.showerror('App', "Connect Error or content not found")

def get_text_result(self, lang):
    global result_global
    sel={'Uzbek': 'uz', 'Russian': 'ru'}
    try:
        translator = Translator()
        if lang!='English':
            translated = translator.translate(self, src=sel[lang], dest='en').text
            result = wikipedia.summary(translated)
            result_global = translator.translate(result, src='en', dest=sel[lang]).text
        else:
            result_global = wikipedia.summary(self)
    except:
        messagebox.showerror('App', "Connect Error or content not found")
    print(result_global)
    save['state']='enable'
    messagebox.showinfo('App', "Completed\nClick the save button")

def search_result(self, lang, a):
    if(lang=="             Language" and self==''): messagebox.showerror('App', 'Enter the language and text')
    elif(lang=="             Language"): messagebox.showerror('App', 'Enter the language')
    elif(self==''): messagebox.showerror('App', 'Enter the text')
    elif(lang=="Uzbek"): result_lang.uz(self, a)
    elif(lang=="Russian"): result_lang.ru(self, a)
    elif(lang=="English"): result_lang.en(self, a)
        
def save_file():
    today = date.today()
    file = open('result'+today.strftime("%d%m%Y")+'.txt', 'w+')
    try:
        file.write(str(result_global))
        messagebox.showinfo('App', "Saved")
        os.startfile('result'+today.strftime("%d%m%Y")+'.txt')
    except:
        messagebox.showinfo('App', "Unfortunately, the file was not saved\nYou can see the result on the console")

a = tk.StringVar();
frame1 = tk.Frame(window,bg='skyblue')
text = tk.Entry(frame1, width=62, textvariable=a, relief="solid",highlightbackground="black", highlightcolor="black", highlightthickness=0)
text.grid(column=0, row=0, columnspan=5)
frame2 = tk.Frame(frame1,bg='skyblue')

c = tk.StringVar(); c.set('             Language')
sel_lang = ttk.Combobox(frame1, textvariable=c, values=('Uzbek', 'Russian', 'English'), state='readonly')
sel_lang.grid(column=0, row=2, pady=5)


save = ttk.Button(frame2, text='Save', state='disabled', command=lambda: save_file())
save.grid(column=3, row=1, pady=8)
ok = ttk.Button(frame2, text='OK', state='disabled', command=lambda: get_text_result(text.get(), sel_lang.get()))
ok.grid(column=2, row=1, pady=8, padx=10)
s = ttk.Button(frame2, text='Search', state='enable', command=lambda: search_result(text.get(), sel_lang.get(), a))
s.grid(column=1, row=1, pady=8)

Photo=ImageTk.PhotoImage(Image.open('logo.png'))
pl = tk.Label(frame1, image=Photo).grid(column=0, row=3, pady=5, padx=5)
frame1.grid(column=0, row=0, pady=10, padx=10)
frame2.grid(column=0, row=1, padx=100)
window.mainloop()
