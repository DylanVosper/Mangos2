
# message = input('enter message: ')
# shift = int(input('Shift number: '))

# def shiftCypher(message):
#     word = ''
#     for i in range(len(message)):
#         current = ord(message[i])
#         current = current + shift
#         word = word + chr(current)

#     print(word)

# shiftCypher(message)

from flask import Flask
from routes.home import homeBP

app = Flask(__name__)
app.config['SECRET_KEY'] = 'THISISABADKEY'
app.register_blueprint(homeBP)
app.run(debug = True)