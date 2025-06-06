import socket
from tkinter import *
from tkinter import messagebox
import json

root = Tk()
root.title('Pizza order')
root.geometry('300x300')

Last_name_label = Label(root, text = 'Last Name:')
Last_name_label.pack()
Last_name_entry = Entry(root)
Last_name_entry.pack()

Phone_number_label = Label(root, text = 'Phone Number:')
Phone_number_label.pack()
Phone_number_entry = Entry(root)
Phone_number_entry.pack()

def Order_pizza() :
    Last_name = Last_name_entry.get()
    Phone_number = Phone_number_entry.get()

    New_order = {'Last_name' : Last_name, 'Phone_number': Phone_number}
    
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



# Refactor code to send a JSON data with an order
# Include a Tkinter GUI with a form that asks for
# a name, phone number, pizza size and ingredients
# the ingredients will be selected using a 
# select menu where they can check a box 
# if they want that ingredient in their pizza
# an option for delivery and pickup will release
# a second form to enter the address.
# add validation to the tkinter form.

