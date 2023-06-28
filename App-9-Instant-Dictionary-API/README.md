
# What does the program do?
The program is written in Python. It is a REST API. The purpose of the API is to receive API requests
that contain an english word as parameter. The API processes the requests and returns a resppnse
in JSON format. The response contains the English definition of the word sent via the request.
# How to run the program
1. Either clone this repo or download all these files by going to _Code -> Download ZIP_.
2. Create a PyCharm (or other IDE) project and configure a Python interpreter for the project.
3. Open the terminal and install the required packages by running:
   `pip install -r requirements.txt`
6. Run _main.py_ with Python.
3. Go to http://127.0.0.1:8000 in your internet browser to see documentation of the API.
4. Try the API by making a request. For example, go to http://127.0.0.1:8000/api?w=moon
   in your internet browser and you will see the English definition of "moon".
