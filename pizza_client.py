import socket
from tkinter import *
from tkinter import messagebox
import json
import emoji

#The root creates the Tkinter window for the user to interact with the connection.
root = Tk()
root.title('Pizza order')
root.geometry('600x850')
root.configure(padx=20, pady=20)

#The header label creates a header for the tkinter window.
Header_label = Label(root, text = 'Order your pizza:', font=('Helvetica', 12))
Header_label.pack(pady=(10, 20), fill='x')

#A pizza emoji
Pizza_label = Label(root, text = f'{emoji.emojize("🍕")}', font=('Helvetica', 25))
Pizza_label.pack()

#A frame to better organize form
customer_info_frame = Frame(root)
customer_info_frame.pack(pady=10, fill='x')

First_name_label = Label(customer_info_frame, text = 'First Name:', font=('Helvetica', 10), bd=2, relief='solid', width=20, anchor='w')
First_name_label.grid(row=0, column=0,padx=10, pady=5)
First_name_entry = Entry(customer_info_frame, font=('Helvetica', 10), width=20)
First_name_entry.grid(row=1, column=0, padx=10, pady=5)

Phone_number_label = Label(customer_info_frame, text = 'Phone Number:', font=('Helvetica', 10), bd=2, relief='solid', width=20, anchor='w')
Phone_number_label.grid(row=0, column=1, padx=10, pady=5)
Phone_number_entry = Entry(customer_info_frame, font=('Helvetica', 10), width=20 )
Phone_number_entry.grid(row=1, column=1, padx=10, pady=5)

#A frame to create a box for the ingredients
ingredients_frame = Frame(root, bd=2, relief='solid', padx=10, pady=10)
ingredients_frame.pack(pady=20, fill='x')

ingredients_label = Label(ingredients_frame, text='Select your ingredients:', font=('Helvetica', 10))
ingredients_label.grid(row=0, column=0, columnspan=3, sticky='w', pady=(0,10))

List_of_ingredients = [ 'Pepperoni', 'Sausage', 'Ham', 'Bell Pepper', 'Onion', 'Olives', 'Pineapple', 'Mushroom', 'Extra cheese']

Ingredient_vars = []
Ingredient_buttons = []

#A for loop that will iterate through each of the ingredients of the List_of_ingredients
#To create a check box for each one.
for list, name in enumerate(List_of_ingredients):
    var = IntVar()
    button = Checkbutton(
        ingredients_frame, 
        text = name,
        variable=var,
        font=('Helvetica',10),
        padx=10,
        pady=5        
    )

    columns = 3
    row = 1 + list // columns
    col = list % columns
    button.grid(row=row, column=col, sticky='w', padx=20, pady=5)
    Ingredient_vars.append(var)

#A frame to create a box for the delivery options.
delivery_options_frame = Frame(root)
delivery_options_frame.pack(pady=10, fill='x')

delivery_label = Label(delivery_options_frame, text='Do you want to:', font=('Helvetica', 10))
delivery_label.grid(row=0, column=0, sticky='w', padx=(0,10))

pick_up_button = Button(delivery_options_frame, text='Pick Up Pizza', font=('Helvetica', 10), width=15)
pick_up_button.grid(row=10, column=1, sticky='w', padx=10)

delivery_button = Button(delivery_options_frame, text='Get Pizza Delivered', font=('Helvetica', 10), width=17)
delivery_button.grid(row=10, column=2, sticky='w', padx=10)

delivery_method = StringVar(value='pickup')

#A frame for the delivery info
address_frame = None
address1_entry = None
address2_entry = None
city_entry = None
zip_code_entry = None

#This function will show the address form fields.
def show_address_form():
    global address_frame, address1_entry, address2_entry, city_entry, zip_code_entry
    delivery_method.set('delivery')
    if address_frame is not None:
        return
    
    address_frame = Frame(root, bd=2, relief='solid', padx=10, pady=10)
    address_frame.pack(pady=10, fill='x')

    address_label = Label(address_frame, text='Enter your address details:', font=('Helvetica', 10))
    address_label.grid(row=0, column=0, columnspan=2, sticky='w', pady=(0,10))

    address1_label = Label(address_frame, text='Address 1:', font=('Helvetica', 10))
    address1_label.grid(row=1, column=0, sticky='w', pady=5, padx=(0,10))
    address1_entry = Entry(address_frame, font=('Helvetica', 10), width=50)
    address1_entry.grid(row=1, column=1, columnspan=2, sticky='ew', pady=5)

    address2_label = Label(address_frame, text='Address 2:', font=('Helvetica', 10))
    address2_label.grid(row=2, column=0, sticky='w', pady=5, padx=(0,10))
    address2_entry = Entry(address_frame, font=('Helvetica', 10), width=50)
    address2_entry.grid(row=2, column=1, columnspan=2, sticky='ew',pady=5)

    city_label = Label(address_frame, text='City:', font=('Helvetica', 10))
    city_label.grid(row=3, column=0, sticky='w', pady=5, padx=(0,10))
    city_entry = Entry(address_frame, font=('Helvetica', 10), width=50)
    city_entry.grid(row=3, column=1, columnspan=2, sticky='ew',pady=5)

    zip_code_label = Label(address_frame, text='Zip Code:', font=('Helvetica', 10))
    zip_code_label.grid(row=4, column=0, sticky='w', pady=5, padx=(0,10))
    zip_code_entry = Entry(address_frame, font=('Helvetica', 10), width=50)
    zip_code_entry.grid(row=4, column=1, columnspan=2, sticky='ew',pady=5)

#This function will hide the address form fields.
def hide_address_form():
    global address_frame, address1_entry, address2_entry, city_entry, zip_code_entry
    delivery_method.set('pickup')
    if address_frame is not None:
        address_frame.destroy()
        address1_entry = None
        address2_entry = None
        city_entry = None
        zip_code_entry = None

    messagebox.showinfo('Success', f'Noted! We will wait for you {emoji.emojize("😉")}')

    

delivery_button.config(command=show_address_form)
pick_up_button.config(command=hide_address_form)

#This function will create a Json object with all the info from
#the Tkinter form and will attempt a connection with the server
def Order_pizza() :
    First_name = First_name_entry.get()
    Phone_number = Phone_number_entry.get()
    Selected_Ingredients = [
        name for name, var in zip(List_of_ingredients, Ingredient_vars) if var.get() == 1
    ]
    Selected_deliver_method = delivery_method.get()


    New_order = {'First_name' : First_name, 'Phone_number': Phone_number, 'Ingredients' : Selected_Ingredients, 'Delivery_method': Selected_deliver_method}

    if Selected_deliver_method == 'delivery':
        New_order['address'] = {
            'Address1' : address1_entry.get(),
            'Address2' : address2_entry.get(),
            'City' : city_entry.get(),
            'Zip_code' : zip_code_entry.get()
        }
    
    Order_json_string = json.dumps(New_order)

    HOST = '127.0.0.1'
    PORT = 12345

    try: 

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(Order_json_string.encode('utf-8'))
            data = s.recv(1024)
            server_response = data.decode('utf-8')
        
        messagebox.showinfo('Order confirmation', server_response)

    except Exception as e:
        messagebox.showerror('Error', f'Order could not be processed, try again, {e}')

        print(f'Received {data!r}')

Order_button = Button(root, text='Order Pizza', font=('Helvetica', 10), width=15, command=Order_pizza)
Order_button.pack()


root.mainloop()

#TODO: add validation to the tkinter form. add an order summary to be showed before sending the order.

