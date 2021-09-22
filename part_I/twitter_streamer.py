#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import argparse
from urllib3.exceptions import ProtocolError

#Variables that contains the user credentials to access Twitter API 
access_token = "327614869-tvLA3T1nb5kccsT6YUHaTH3g9pJdVrLlhgGMxB7p"
access_token_secret = "W502RqeJSwjyKSu0ebP6u4OlM5093g7XL4ThDo9qnS5im"
consumer_key = "CkCl5EM7i3fK2ARwNh3tYkPyM"
consumer_secret = "cbLC8eCQXVXAcBesoUTbkGhwTSQnBQwOc4sdW4UOT30wSlMiZm"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        with open(filename,'a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    my_parser = argparse.ArgumentParser(prog='python twitter_streamer.py',
                                        usage='%(prog)s [options] --file_name',
                                        description='Get Twitter streaming data')
    my_parser.add_argument('--file_name', action='store', type=str, required=True)
    args = my_parser.parse_args()
    filename = args.file_name
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l,tweet_mode='extended')

    while True:
        try:
            ## Creates content filters
            stream.filter(languages=["pt"], track=['bolsonaro', 'vacina', 'butantan', 'pfizer', 'coronavac', 'nba', 'brasil', 'politica','economia','festa','gremio','inter','nerd'])
        except (ProtocolError, AttributeError):
            continue