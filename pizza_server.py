import socket
import json

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            received_string = data.decode('utf-8')
            parsed_order = json.loads(received_string)
            print (f'Order data:{parsed_order}')
            conn.sendall('What should I send here?')
            

#Refactor server to send back a tkinter confirmation
# page containing the JSON info of the order
# and the estimated time for pick up which will be 
# calculated by the number of ingredients picked
# if delivery was selected, 25 minutes will be added
# to the calculated time