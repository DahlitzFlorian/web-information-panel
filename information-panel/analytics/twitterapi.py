"""TwitterAPI

    Makes use of the python-twitter package handling tweets
    to a given term.
"""
import twitter


class TwitterAPI:
    """Object establishing the connection to twitter
        and being the instance to use for further settings and handles.
    """
    def __init__(self,
                twitter_consumer_key,
                twitter_consumer_secret,
                twitter_access_token,
                twitter_access_secret):
        """initial parameters

            The parameters have to include key, token and secrets 
            to establish a connection to the Twitter Application 
            created before.
        """
        self.twitter_consumer_key = twitter_consumer_key
        self.twitter_consumer_secret = twitter_consumer_secret
        self.twitter_access_token = twitter_access_token
        self.twitter_access_secret = twitter_access_secret

        self.twitter_api = self.connecting()
    

    def connecting(self):
        """Connection

            Creates an instance of the twitter api and return it.
        """
        return twitter.Api(consumer_key=self.twitter_consumer_key,
                                    consumer_secret=self.twitter_consumer_secret,
                                    access_token_key=self.twitter_access_token,
                                    access_token_secret=self.twitter_access_secret)
    

    def get_tweets(self, term="Twitter", number=100, until=None, since=None, lang="en"):
        """Getting tweets 

            Returns a number of tweets to a given term based on the 
            parameters.
        """
        return self.twitter_api.GetSearch(term=term, count=number, until=until, since=since, lang=lang)
