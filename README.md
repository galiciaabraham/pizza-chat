# Overview

Hello world! For this project I decided to create a pizza delivery system. In a real life scenario, this could be used as a simple order processing system, I decided to create a GUI to make it more visual, but the networking stack is at the heart of the whole application.

As a Client-Server application, you will execute both files, the Server will listen to the Json data being sent, perform some basic calculations with the data and then send back a response. The client will simply fill out a form and send the data over the server to be processed.

This application serves as an evidence of the understanding I've gained of the Networking stack and of GUI tools such as Tkinter.

# Network Communication

For the project I followed a Client-Server architecture, in which a client will build and send an order, and a server will receive and process the order and send a response back confirming the data was received.

Since a response is received and another is sent back, this is a TCP application. Since I programmed the app on the same computer, we use 127.0.0.1 port or the loopback/local-host port.

Because the data we're sending is small, encoding the messages in 8-bits improves performance and ensures the compatibility of the data between the client and the server. 

# Development Environment

I used VS Code as my IDE while developing the application. I visualized my application using wireframe.cc. 

The application was written using Python. Socket was the library used to configure all the networking. Tkinter was used to create a simply GUI. And the json and emoji libraries were used for functionality and style purposes. 

# Useful Websites

Some uselful and awesome references: 

* [Real Python | Python Sockets](https://realpython.com/python-sockets/)
* [Medium | Towards AI | Create a Simple User Form with Python and Tkinter ](https://pub.towardsai.net/create-a-simple-user-form-with-python-and-tkinter-in-5-minutes-a-beginners-guide-bb87b86820cb)

# Future Work

Some items on my TODO list for future enhancements:

* Add validation: I need to add validation and error handling for the form fields to improve UX.
* Enhance server features: I want to add other features to the server so it can perform other type of calculations, integrate other confirmation options or messages, or a processing information function that will save the order into an ordering file or database. 
* Add order summary: An order summary can be added to the client app so the users know what they've entered and selected. This can also serve as a form of client validation.