import socket
import time

HOST = 'localhost'
PORT = 3000

s = socket.socket() # default
s.bind((HOST, PORT))
print(f'Waiting conection in port ... {PORT}')

s.listen(5)
conn, adress = s.accept()

print(f'Receving solicitation from {adress}')

messages = [
    'Mensagem A',
    'Mensagem B',
    'Mensagem C',
    'Mensagem D',
    'Mensagem E',
    'Mensagem F',
    'Mensagem G',
    'I am exicited with this course'
]

for msg in messages:
    msg = bytes(msg, 'utf-8')
    conn.send(msg)
    time.sleep(3)
    
conn.close()