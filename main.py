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

