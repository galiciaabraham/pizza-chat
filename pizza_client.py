import socket
from tkinter import *
from tkinter import messagebox
import json
import emoji

#The root creates the Tkinter window for the user to interact with the connection.
root = Tk()
root.title('Pizza order')
root.geometry('700x500')
root.configure(padx=20, pady=20)

#The header label creates a header for the tkinter window.
Header_label = Label(root, text = 'Order your pizza:', font=('Arial', 15))
Header_label.pack(pady=(10, 20), fill='x')

#A pizza emoji
Pizza_label = Label(root, text = f'{emoji.emojize("🍕")}', font=('Helvetica', 32))
Pizza_label.pack()

#A frame to better organize form
customer_info_frame = Frame(root)
customer_info_frame.pack(pady=10, fill='x')

First_name_label = Label(customer_info_frame, text = 'First Name:', font=('Helvetica', 12), bd=2, relief='solid', width=20, anchor='w')
First_name_label.grid(row=0, column=0,padx=10, pady=5)
First_name_entry = Entry(customer_info_frame, font=('Helvetica', 12), width=20)
First_name_entry.grid(row=1, column=0, padx=10, pady=5)

Phone_number_label = Label(customer_info_frame, text = 'Phone Number:', font=('Helvetica', 12), bd=2, relief='solid', width=20, anchor='w')
Phone_number_label.grid(row=0, column=1, padx=10, pady=5)
Phone_number_entry = Entry(customer_info_frame, font=('Helvetica', 12), width=20 )
Phone_number_entry.grid(row=1, column=1, padx=10, pady=5)

#A frame to create a box for the ingredients
ingredients_frame = Frame(root, bd=2, relief='solid', padx=10, pady=10)
ingredients_frame.pack(pady=20, fill='x')

ingredients_label = Label(ingredients_frame, text='Select your ingredients:', font=('Helvetica', 12))
ingredients_label.grid(row=0, column=0, columnspan=3, sticky='w', pady=(0,10))

List_of_ingredients = [ 'Pepperoni', 'Sausage', 'Ham', 'Bell Pepper', 'Onion', 'Olives', 'Pineapple', 'Mushroom', 'Extra cheese']

Ingredient_vars = []
Ingredient_buttons = []

for list, name in enumerate(List_of_ingredients):
    var = IntVar()
    button = Checkbutton(
        ingredients_frame, 
        text = name,
        variable=var,
        font=('Helvetica',12),
        padx=10,
        pady=5        
    )

    columns = 3
    row = 1 + list // columns
    col = list % columns
    button.grid(row=row, column=col, sticky='w', padx=20, pady=5)
    Ingredient_vars.append(var)


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

# Add  an option for delivery and pickup, which will show
# additioanl fields to enter the address.
# add validation to the tkinter form.

