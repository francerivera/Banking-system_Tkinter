from tkinter import *
from tkinter import messagebox

def bill_area():
    if priceEntry.get()=='':
        messagebox.showerror('Error', 'No products are selected')
    textarea.delete(1.0, END)

    if pencilEntry.get() == '':
        messagebox.showerror('Error', 'Please enter the quantity of the product.')
    elif penEntry.get() == '':
        messagebox.showerror('Error', 'Please enter the quantity of the product.')
    elif padEntry.get() == '':
        messagebox.showerror('Error', 'Please enter the quantity of the product.')
    elif paperEntry.get() == '':
        messagebox.showerror('Error', 'Please enter the quantity of the product.')
    elif colorEntry.get() == '':
        messagebox.showerror('Error', 'Please enter the quantity of the product.')
    textarea.delete(1.0, END)



    textarea.insert(END, '\t     **Welcome Perpetualite**')
    textarea.insert(END, '\n==================================================')
    textarea.insert(END, '\nProduct\t\t     Quantity\t\t\tPrice')
    textarea.insert(END, '\n==================================================')
    if pencilEntry.get()!='0':
        textarea.insert(END, f'\nPencil\t\t\t{pencilEntry.get()}\t\tP {pencilprice}')
    if penEntry.get()!='0':
        textarea.insert(END, f'\nPen\t\t\t{penEntry.get()}\t\tP {penprice}')
    if padEntry.get()!='0':
        textarea.insert(END, f'\nYellow Pad\t\t\t{padEntry.get()}\t\tP {padprice}')
    if paperEntry.get()!='0':
        textarea.insert(END, f'\nBond Paper\t\t\t{paperEntry.get()}\t\tP {paperprice}')
    if colorEntry.get()!='0':
        textarea.insert(END, f'\nColor\t\t\t{colorEntry.get()}\t\tP {colorprice}')
    textarea.insert(END, '\n--------------------------------------------------')


    if taxEntry.get()!='P 0':
        textarea.insert(END, f'\nTax\t\t\t\t\t{taxEntry.get()}')
    textarea.insert(END,f'\nTOTAL\t\t\t\t\tP {totalbills}')
    textarea.insert(END, f'\nCHANGE\t\t\t\t\tP {change}')


def total():
    global pencilprice, penprice, padprice, paperprice, colorprice
    global totalbills
    global change
    pencilprice=int(pencilEntry.get())*15
    penprice=int(penEntry.get())*25
    padprice=int(padEntry.get())*2
    paperprice=int(paperEntry.get())*1
    colorprice=int(colorEntry.get())*45.50


    totalsuppliesprice=pencilprice+penprice+padprice+paperprice+colorprice
    priceEntry.delete(0, END)
    priceEntry.insert(0,f'P {totalsuppliesprice}')
    tax=totalsuppliesprice*0.10
    taxEntry.delete(0,END)
    taxEntry.insert(0,f'P {tax}')

    totalbills=totalsuppliesprice+tax
    cash = float(cashEntry.get())

    if cash < totalbills:
        messagebox.showerror('Error', 'Insufficient funds')
        return

    change = cash - totalbills
    cashEntry.delete(0, END)
    cashEntry.insert(0,  f'P {cash}')
    changeEntry.delete(0, END)
    changeEntry.insert(0, f'P {change:.2f}')



root=Tk()
root.title("France Rivera's Shop")
root.geometry("1270x685+300+150")
headingLabel=Label(root, text="France's Stationery", font=('Monotype Corsiva', 50, 'bold')
                   ,bg='#800000', fg='gold', bd=12,relief=FLAT)
headingLabel.pack(fill=X)

productsFrame=Frame(root)
productsFrame.pack(pady=20)

SuppliesFrame=LabelFrame(productsFrame, text='School Supplies',font=('Book Antiqua', 19, 'bold')
                   ,bg='#800000', fg='gold',bd=8, relief=GROOVE)
SuppliesFrame.grid(row=0, column=0)


pencilLabel=Label(SuppliesFrame, text="Pencil",font=('Helvetica', 15, 'bold')
                   ,bg='#800000', fg='white')
pencilLabel.grid(row=0,column=0, padx=10,pady=10,sticky='w')
pencilEntry=Entry(SuppliesFrame, font=('Helvetica', 15, 'bold'), width=10,
                  bd=5)
pencilEntry.grid(row=0,column=1, padx=10)
pencilEntry.insert(0,0)

penLabel=Label(SuppliesFrame, text="Pen",font=('Helvetica', 15, 'bold')
                   ,bg='#800000', fg='white')
penLabel.grid(row=1,column=0, padx=10,pady=10,sticky='w')

penEntry=Entry(SuppliesFrame, font=('Helvetica', 15, 'bold'), width=10,
                  bd=5)
penEntry.grid(row=1,column=1, padx=10)
penEntry.insert(0,0)

padLabel=Label(SuppliesFrame, text="Yellow Pad",font=('Helvetica', 15, 'bold')
                   ,bg='#800000', fg='white')
padLabel.grid(row=2,column=0, padx=10,pady=10,sticky='w')

padEntry=Entry(SuppliesFrame, font=('Helvetica', 15, 'bold'), width=10,
                  bd=5)
padEntry.grid(row=2,column=1, padx=10)
padEntry.insert(0,0)

paperLabel=Label(SuppliesFrame, text="Bond Paper",font=('Helvetica', 15, 'bold')
                   ,bg='#800000', fg='white')
paperLabel.grid(row=3,column=0, padx=10,pady=10,sticky='w')

paperEntry=Entry(SuppliesFrame, font=('Helvetica', 15, 'bold'), width=10,
                  bd=5)
paperEntry.grid(row=3,column=1, padx=10)
paperEntry.insert(0,0)

colorLabel=Label(SuppliesFrame, text="Color",font=('Helvetica', 15, 'bold')
                   ,bg='#800000', fg='white')
colorLabel.grid(row=4,column=0, padx=10,pady=10,sticky='w')

colorEntry=Entry(SuppliesFrame, font=('Helvetica', 15, 'bold'), width=10,
                  bd=5)
colorEntry.grid(row=4,column=1, padx=10)
colorEntry.insert(0,0)

tagFrame=LabelFrame(productsFrame, text='Prices',font=('Book Antiqua', 19, 'bold')
                   ,bg='#800000', fg='gold',bd=8, relief=GROOVE)
tagFrame.grid(row=0, column=1)

pencilpriceLabel=Label(tagFrame, text="Pencil:",font=('Helvetica', 15, 'bold')
                   ,bg='#800000', fg='white')
pencilpriceLabel.grid(row=0,column=0, padx=10,pady=10,sticky='w')
pencilprice1Label=Label(tagFrame, text="P 15.00",font=('Helvetica', 15)
                   ,bg='#800000', fg='white')
pencilprice1Label.grid(row=0,column=1, padx=10,pady=10,sticky='w')


penpriceLabel=Label(tagFrame, text="Pen:",font=('Helvetica', 15, 'bold')
                   ,bg='#800000', fg='white')
penpriceLabel.grid(row=1,column=0, padx=10,pady=10,sticky='w')
penprice1Label=Label(tagFrame, text="P 25.00",font=('Helvetica', 15)
                   ,bg='#800000', fg='white')
penprice1Label.grid(row=1,column=1, padx=10,pady=10,sticky='w')


padpriceLabel=Label(tagFrame, text="Yellow Pad:",font=('Helvetica', 15, 'bold')
                   ,bg='#800000', fg='white')
padpriceLabel.grid(row=2,column=0, padx=10,pady=10,sticky='w')
padprice1Label=Label(tagFrame, text="P 2.00",font=('Helvetica', 15)
                   ,bg='#800000', fg='white')
padprice1Label.grid(row=2,column=1,padx=10, pady=10,sticky='w')


paperpriceLabel=Label(tagFrame, text="Bond Paper:",font=('Helvetica', 15, 'bold')
                   ,bg='#800000', fg='white')
paperpriceLabel.grid(row=3,column=0, padx=10,pady=10,sticky='w')
paperprice1Label=Label(tagFrame, text="P 1.00",font=('Helvetica', 15)
                   ,bg='#800000', fg='white')
paperprice1Label.grid(row=3,column=1,padx=10, pady=10,sticky='w')


colorpriceLabel=Label(tagFrame, text="Color:",font=('Helvetica', 15, 'bold')
                   ,bg='#800000', fg='white')
colorpriceLabel.grid(row=4,column=0, padx=10,pady=10,sticky='w')
colorprice1Label=Label(tagFrame, text="P 45.50",font=('Helvetica', 15)
                   ,bg='#800000', fg='white')
colorprice1Label.grid(row=4,column=1,padx=10, pady=10,sticky='w')



billFrame=Frame(productsFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=2, padx=10)

billareaLabel=Label(billFrame,text='Bill Receipt',font=('Helvetica', 20, 'bold'),bd=7, relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billFrame,height=14,width=50,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)


menuFrame=LabelFrame(root, text='Checkout',font=('Book Antiqua', 19, 'bold')
                   ,bg='#800000', fg='gold',bd=8, relief=GROOVE)
menuFrame.pack()

priceLabel=Label(menuFrame, text="Total Price",font=('Helvetica', 15, 'bold')
                   ,bg='#800000', fg='white')
priceLabel.grid(row=0,column=0, padx=10,pady=10,sticky='w')

priceEntry=Entry(menuFrame, font=('Helvetica', 15, 'bold'), width=10,
                  bd=5)
priceEntry.grid(row=0,column=1, padx=10, pady=10)


cashLabel=Label(menuFrame, text="Cash",font=('Helvetica', 15, 'bold')
                   ,bg='#800000', fg='white')
cashLabel.grid(row=1,column=0, padx=10,pady=10,sticky='w')

cashEntry=Entry(menuFrame, font=('Helvetica', 15, 'bold'), width=10,
                  bd=5)
cashEntry.grid(row=1,column=1, padx=10, pady=10)


changeLabel=Label(menuFrame, text="Change",font=('Helvetica', 15, 'bold')
                   ,bg='#800000', fg='white')
changeLabel.grid(row=1,column=2, padx=10,pady=10,sticky='w')

changeEntry=Entry(menuFrame, font=('Helvetica', 15, 'bold'), width=10,
                  bd=5)
changeEntry.grid(row=1,column=3, padx=10, pady=10)




taxLabel=Label(menuFrame, text="Tax:   0.10%",font=('Helvetica', 15, 'bold')
                   ,bg='#800000', fg='white')
taxLabel.grid(row=0,column=2, padx=10,pady=10,sticky='w')

taxEntry=Entry(menuFrame, font=('Helvetica', 15, 'bold'), width=10,
                  bd=5)
taxEntry.grid(row=0,column=3, padx=10, pady=10)

buttonFrame=Frame(menuFrame,bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=1)

totalButton=Button(buttonFrame, text="Total Amount", font=('arial', 16, 'bold'), bg='#800000',fg='white'
                   ,bd=5, width=12, pady=10, command=total)
totalButton.grid(row=0,column=0)

billButton=Button(buttonFrame, text="Bill", font=('arial', 16, 'bold'), bg='#800000',fg='white'
                   ,bd=5, width=12, pady=10, command=bill_area)
billButton.grid(row=0,column=1)


root.mainloop()
