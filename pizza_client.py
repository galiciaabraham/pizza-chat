import socket
from tkinter import *
from tkinter import messagebox
import json
import emoji

root = Tk()
root.title('Pizza order')
root.geometry('300x300')


Header_label = Label(root, text = 'Order your pizza:', font=('Arial', 15))
Header_label.pack()

Pizza_label = Label(root, text = f'{emoji.emojize("🍕")}', font=('Helvetica', 32))
Pizza_label.pack()

First_name_label = Label(root, text = 'Last Name:')
First_name_label.pack()
First_name_entry = Entry(root)
First_name_entry.pack()

Phone_number_label = Label(root, text = 'Phone Number:')
Phone_number_label.pack()
Phone_number_entry = Entry(root)
Phone_number_entry.pack()

List_of_ingredients = [ 'Pepperoni', 'Sausage', 'Ham', 'Bell Pepper', 'Onion', 'Olives', 'Pineapple', 'Mushroom', 'Extra cheese']

Ingredient_vars = []
Ingredient_buttons = []

for name in List_of_ingredients:
    var = IntVar()
    button = Checkbutton(
        root, 
        text = name,
        variable=var,
        onvalue=1,
        offvalue=0,
        height=2,
        width=15
    )
    button.pack()
    Ingredient_vars.append(var)
    Ingredient_buttons.append(button)


def Order_pizza() :
    First_name = First_name_entry.get()
    Phone_number = Phone_number_entry.get()
    Selected_Ingredients = [
        name for name, var in zip(List_of_ingredients, Ingredient_vars) if var.get() == 1
    ]


    New_order = {'First_name' : First_name, 'Phone_number': Phone_number, 'Ingredients' : Selected_Ingredients}
    
    Order_json_string = json.dumps(New_order)

    HOST = '127.0.0.1'
    PORT = 12345

    try: 

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(Order_json_string.encode('utf-8'))
            data = s.recv(1024)
        
        messagebox.showinfo('Success', 'Pizza ordered correctly')
    except Exception as e:
        messagebox.showerror('Error', f'Order could not be processed, try again, {e}')

        print(f'Received {data!r}')



Order_button = Button(root, text='Order', command=Order_pizza)
Order_button.pack()

root.mainloop()

# Adjust ingredients selection position so they don't have to make the screen bigger.
# Add  an option for delivery and pickup, which will show
# additioanl fields to enter the address.
# add validation to the tkinter form.

