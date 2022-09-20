import socket
import tweepy

HOST = 'localhost'
PORT = 9009

s = socket.socket()
s.bind((HOST, PORT))
print(f"Waiting for conection from port: {PORT}")

s.listen(5)
connection, adress = s.accept()
print(f"Receving solicitation from: {adress}")

token = 'AAAAAAAAAAAAAAAAAAAAALAuhQEAAAAAtzLX6YYqljdDiTvHUPpZkvE0B8A%3Dgw25ySACZ8NxA036yykRxciaWJEfflqkCiXNUlDx1TryHCbXLI'

keyword = 'flamengo'

class get_tweets(tweepy.StreamingClient):
    
    def on_tweet(self, tweet):
        print(f"{tweet.text}\n{'='*50}")
        connection.send(tweet.text.encode('latin1', 'ignore'))
        
printer = get_tweets(token)
printer.add_rules(tweepy.StreamRule(keyword))
printer.filter()

connection.close()
        
        
