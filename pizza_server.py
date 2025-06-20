import socket
import json

HOST = '127.0.0.1'
PORT = 12345

#using "with" ensures the connection is closed after being done. 
#socket will create a new node and conn will connect with the client.
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

            #perform some simple calculations with the json data received. 
            estimated_time = 0
            minutes_per_ingredient = 3
            expected_delivery_time = 30
            
            number_of_ingredients = len(parsed_order.get('Ingredients',[]))
            estimated_time = number_of_ingredients * minutes_per_ingredient

            if parsed_order.get('Delivery_method') == 'delivery':
                estimated_time += expected_delivery_time
            
            #The response is crafted and then is sent back to the client.
            response = f"Thank you for your order {parsed_order.get('First_name')}, You selected {parsed_order.get('Delivery_method')} as your delivery method. Estimated time: {estimated_time} minutes."
            conn.sendall(response.encode('utf-8'))
            

#TODO: Add server validation rules, add other features to the server operations such as:
#dynamic ingredient times, other processing data rules.