# Import the required libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

class Item:
    def total_price(self, x, y):
        return self.price * self.quantity

item1 = Item()
item1.name = "Apple"
item1.price = 2.5
item1.quantity = 425

item2 = Item()
item2.name = "Banana"
item2.price = 5
item2.quantity = 315

# # Create an instance of tkinter frame
root= Tk()
root.configure(background='#474747')
root.title('Data_Analysis')
root.resizable(0, 0)
# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.columnconfigure(2, weight=3)
root.columnconfigure(3, weight=3)
# Size of window
root.geometry("960x700")
#bg = PhotoImage(file = "C:\\Users\\Kamil\\img.jpg")

# Define a function to show the popup message
def show_apples():
   messagebox.showinfo("Message",(item1.total_price(item1.price,item1.quantity)))
def show_bananas():
    messagebox.showinfo("Message",(item2.total_price(item2.price,item2.quantity)))

# Header label
Label(root, background='#474747', text= ("DATA ANALYSIS"), font= ('Lato',35)).pack(pady= 30)
# Choose option label
Label(root, background='#474747', text= ("Choose ANALysis options:"), font= ('Lato',15)).pack(pady= 30)
# Create a Button to display the message
ttk.Button(root, text= "📃 Option #1", command=show_apples).pack(pady= 20)
ttk.Button(root, text= "📃 Option #2", command=show_apples).pack(pady= 20)
ttk.Button(root, text= "📃 Option #3", command=show_apples).pack(pady= 20)
ttk.Button(root, text= "📃 Option #4", command=show_apples).pack(pady= 20)
ttk.Button(root, text= "📃 Option #5", command=show_apples).pack(pady= 20)

# ttk.grid(row = 1, column = 0, sticky = W, pady = 2)
# root = Tk()

# testy moje:
def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
        )
    path.insert(END, tf)
    tf = open(tf)
    data = tf.read()
    tf.close()

path = Entry(root)
path.pack(side=LEFT, expand=True, fill=X, padx=20)

Button(root, text="Open File", command=openFile).pack(side=RIGHT, expand=True, fill=X, padx=20)

root.mainloop()


# siema tutaj co tam 
from tkinter import *
from tkinter import filedialog

from openpyxl import workbook, load_workbook

# główne okno programu
root = Tk()
root.title("DATA ANALISYS")
root.geometry("720x480")
# ---


# ---
def funkcja_start():

    if varpdf.get() and (var1.get() or var2.get() or var3.get()):
        # generuj plik pdf z wynikami.
        testyyy = Label(root, text=varpdf.get())
        testyyy.grid(row=9, column=0)
    elif (var1.get() or var2.get() or var3.get()) and wpisywanieplikow.get():
        podglad = Toplevel()
        if var1.get():
            komunikat1 = Label(podglad, text="var1. wykres")
            komunikat1.pack()
        if var2.get():
            liczenie_mediana()

            wb = load_workbook('testy_arkusz.xlsx')
            ws = wb.active

            komunikat2 = Label(podglad, text="var2. Mediana")
            komunikat2a = Label(podglad, text=int(wynik_med[0]))
            komunikat2.pack()
            komunikat2a.pack()
        if var3.get():
            komunikat3 = Label(podglad, text="var3. srednia")
            komunikat3.pack()
    else:
        testyyy2 = Label(root, text="Zaznacz pożądane opcje")
        testyyy2.grid(row=8, column=2)


wynik_med = []

    # Obliczenia wszystkie

    # Podgląd wyników w nowym oknie



# ---
# ---
def liczenie_mediana():



    aa1 = 5
    aa2 = 6
    aa3 = 2
    aa4 = 8
    ans1 = aa1 + aa3 * aa4 - aa2
    wynik_med.append(ans1)
# ---
def open():
    root.filename = filedialog.askopenfilename(initialdir="/", title="select a file", filetypes=(
        ("txt files", "*.txt"), ("xlsx files", "*.xlsx"), ("all type", "*.*")))
    wpisywanieplikow.delete(0, "end")
    wpisywanieplikow.insert(0, root.filename)
# ---


# ---
# GUI programu:
xd = "sdsd"
opis = "Witaj w programie do analizy danych.\n Aby rozpocząć wybierz plik, a następnie zaznacz \ninteresujące cię opcję.\n " \
       "Po wciśnięciu przycisku start wyświetli się podgląd z wynikami \n a jeśli chcesz aby wyniki pojawiły się w pliku pdf,\n wystarczy że zaznaczysz opcję generuj pdf\n" \
       "i po wciśnięciu przycisku start zamiast podglądów\n wygeneruje ci się plik pdf z tymi wszystkimi wynikami."
# creating a label widget
myLabel = Label(root, text="DATA ANALISYS")
mypusto = Label(root, text="                             ")
mypusto2 = Label(root, text="                             ")
wpisywanieplikow  = Entry(root, width=35, borderwidth=5)
przycisk_pliki = Button(root, text="Open file", command=open)
myopisheader = Label(root, text="OPIS")
myopis = Label(root, text=opis)

var1 = IntVar()
opcja1 = Checkbutton(root, text="Wykres", variable=var1)
var2 = IntVar()
opcja2 = Checkbutton(root, text="Mediana", variable=var2)
var3 = IntVar()
opcja3 = Checkbutton(root, text="Srednia", variable=var3)
varpdf = IntVar()
opcjapdf = Checkbutton(root, text="generuj pdf", variable=varpdf)


myStart = Button(root, text="Start", command=funkcja_start)


# shoving it onto the screen
myLabel.grid(row=0, column=1)
mypusto.grid(row=1, column=0)
mypusto2.grid(row=2, column=0)
wpisywanieplikow.grid(row=3, column=0)
przycisk_pliki.grid(row=3, column=1)
myopisheader.grid(row=3, column=2)
myopis.grid(row=4, column=2)

opcja1.grid(row=4, column=0)
opcja2.grid(row=5, column=0)
opcja3.grid(row=6, column=0)

opcjapdf.grid(row=7, column=0)

myStart.grid(row=9, column=2)
# ----



# ---
root.mainloop()
