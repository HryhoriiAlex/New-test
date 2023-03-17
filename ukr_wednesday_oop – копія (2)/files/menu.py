from tkinter import *
from tkinter import ttk
from PIL import Image as img
from PIL import ImageTk as imgtk

class Menu:
    def __init__(self):
        with open("files/menu/files/settings.txt", "r", encoding="utf8") as file:
            self.lis = file.readlines()

    def open_menu(self):
        global Combo, inp
        regim = "".join("".join(self.lis[self.found_name("Режим(1 або 2) - ")].split("Режим(1 або 2) - ")).replace("\\", '/').split("\n"))

        root2 = Tk()
        root2.title("Меню")
        root2.geometry("626x368")
        root2.configure(bg='black')
        root2.iconbitmap('files/icon/icon3.ico')
        root2.resizable(0, 0)

        canvas = Canvas(
                root2, 
                width = 626, 
                height = 97,
                background="black",
                bg="black"
                ) 

        canvas.pack()

        imag = img.open('files/menu/baner.png')
        imag = imag.resize((626, 97))
        imag = imgtk.PhotoImage(imag)  
        canvas.create_image(0, 0, anchor=NW, image=imag) 
        
        frame = Frame(root2)
        frame.pack()

        vlist = [1, 2]
        
        Combo = ttk.Combobox(values = vlist)
        Combo.set(int(regim))
        Combo.place(x=60, y=137, width=195, height=33)

        label_combo = Label(text="Режим", fg= "#A9A9A9", font=('Times 14'))
        label_combo.config(bg="black")
        label_combo.place(x=60, y=105)

        regim = "".join("".join(self.lis[self.found_name("Ім'я - ")].split("Ім'я - ")).replace("\\", '/').split("\n"))

        but_img = PhotoImage(file='files/menu/but.png')
        
        but = Button(text="Підтвердити",command=self.check, image=but_img, width=198, height=48)
        but.config(bg="black")
        but.place(x=214, y=184) 

        inp = Entry()
        inp.place(x=326, y=137, width=234, height=33)
        inp.insert(0, regim)

        label_inp = Label(text="Як до вас звертатись?", fg= "#A9A9A9", font=('Times 14'))
        label_inp.config(bg="black")
        label_inp.place(x=326, y=105)
        
        but2_img = PhotoImage(file='files/menu/but2.png')

        but2 = Button(text="Налаштування",command=self.sett, image=but2_img)
        but2.config(bg="black")
        but2.place(x=183, y=258) 

        root2.mainloop()
    
    def found_name(self, title):
        with open("files/menu/files/settings.txt", "r", encoding="utf8") as file:
            found = file.readlines()
        n = 0
        for i in found:
            if title in i:
                return n

            n += 1
    
    def sett(self):
        import tkinter as tk
        from tkinter import ttk

        global names, listboxes, pathes, end

        root = tk.Tk()
        root.title("Налаштування")
        root.resizable(0, 0)
        root.iconbitmap('files/icon/icon3.ico')
        container = ttk.Frame(root)
        canvas = tk.Canvas(container, height=626, width=482)

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        title = Label(root, text="Назва", font=('Times 14'))
        title.place(x=56, y=2)

        shl = Label(root, text="Шлях", font=('Times 14'))
        shl.place(x=350, y=2)

        butl =  tk.Button(root, text="Підтвердити", command=self.gett)
        butl.pack()

        names = []
        listboxes = []
        pathes = []

        for i in range(49):
            listbox1 = tk.Listbox (scrollable_frame, height=3, width=15, selectmode =  tk.SINGLE)
            list1 = ["Прогамма","Сайт","Комбінація"]
            for e in list1:
                listbox1.insert ( tk.END, e)
            
            listboxes.append(listbox1)

            inpu =  tk.Entry(scrollable_frame)
            names.append(inpu)
            path =  tk.Entry(scrollable_frame)
            pathes.append(path)

            inpu.grid(row=i, column=0)
            listbox1.grid(row=i, column=1)
            path.grid(row=i, column=2)


        with open("files/menu/files/text.txt", "r") as f:
            text = f.readlines()

        if len(text) == 0:
            for i in range(49):
                text.append("\n")
            
            with open("files/menu/files/text.txt", "w") as f:
                f.writelines(text)
        else:
            for n in range(len(names)):
                names[n].insert(0, "".join(text[n].split("\n")))

        with open("files/menu/files/listbox.txt", "r") as f:
            listbox = f.readlines()

        if len(listbox) == 0:
            for i in range(49):
                listbox.append("\n")
            
            with open("files/menu/files/listbox.txt", "w") as f:
                f.writelines(listbox)

        with open("files/menu/files/path.txt", "r") as f:
            path = f.readlines()

        if len(path) == 0:
            for i in range(49):
                path.append("\n")
            
            with open("files/menu/files/path.txt", "w") as f:
                f.writelines(path)
        else:
            for n in range(len(path)):
                pathes[n].insert(0, "".join(path[n].split("\n")))

        with open("files/menu/files/end.txt", "r") as f:
            end = f.readlines()

        if len(end) == 0:
            for i in range(49):
                end.append("\n")
            
            with open("files/menu/files/end.txt", "w") as f:
                f.writelines(end)

        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        root.mainloop()

    def gett(self):
        global names, listboxes, pathes, end

        with open("files/menu/files/text.txt", "r") as f:
            text = f.readlines()
        
        with open("files/menu/files/listbox.txt", "r") as f:
            listbox = f.readlines()
        
        for l in range(len(listboxes)):
            for b in listboxes[l].curselection():
                listbox[l] = listboxes[l].get(b) + "\n"

        with open("files/menu/files/listbox.txt", "w") as f:
            f.writelines(listbox)
        
        for i in range(len(names)):
            text[i] = names[i].get() + "\n"
            
        with open("files/menu/files/text.txt", "w") as f:
            f.writelines(text)
        
        with open("files/menu/files/path.txt", "r") as f:
            path_l = f.readlines()

        for i in range(len(path_l)):
            path_l[i] = pathes[i].get() + "\n"
            
        with open("files/menu/files/path.txt", "w") as f:
            f.writelines(path_l)

        with open("files/menu/files/text.txt", "r") as f:
            text = f.readlines()

        with open("files/menu/files/path.txt", "r") as f:
            path_l = f.readlines()
        
        with open("files/menu/files/listbox.txt", "r") as f:
            listbox = f.readlines()


        for i in range(49):

            if text[i] != "\n" and path_l[i] != "\n" and listbox[i] != "\n":
                text[i] = "".join(text[i].split("\n"))
                listbox[i] = "".join(listbox[i].lower().split("\n"))
                path_l[i] = "".join(path_l[i].split("\n"))
                end[i] = f"{text[i]}({listbox[i]}) - {path_l[i]}\n"
                with open("files/menu/files/end.txt", "w") as f:
                    f.writelines(end)
        
        for i in range(49):

            if text[i] == "\n" and path_l[i] == "\n" and end[i] != "\n":
                end[i] = "\n"
        
                with open("files/menu/files/end.txt", "w") as f:
                    f.writelines(end)


    def check(self):
        if Combo.get() != "1" and Combo.get() != "2":
            Combo.set(1)
        
        with open("files/menu/files/settings.txt", "r", encoding="utf-8") as file:
            read = file.readlines()

        ind_of_regim = self.found_name("Режим(1 або 2) - ")
        new_string_regim = f"Режим(1 або 2) - {Combo.get()}\n"
        read[ind_of_regim] = new_string_regim

        ind_of_name = self.found_name("Ім'я - ")
        new_string_name = f"Ім'я - {inp.get().lower()}\n"
        read[ind_of_name] = new_string_name
        
        with open("files/menu/files/settings.txt", "w", encoding="utf-8") as file:
            file.writelines(read)