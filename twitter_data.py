__author__ = '@insidertech'

import requests
import os
import json

from tokens import tokens


def auth():
    xcode = tokens()
    return xcode


def create_url():
    #query = "from:twitterdev -is:retweet"    
    query = "Tidur"
    
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    tweet_fields = "tweet.fields=id,author_id,geo,created_at,source,text,withheld,possibly_sensitive,lang"
    max_results = "max_results=10"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}&{}".format(
        query, tweet_fields, max_results
    )
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    #print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    json_response = json.dumps(json_response['data'], indent=4, sort_keys=True)
    print(json_response)

def tw_data():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    json_response = json.dumps(json_response['data'], indent=4, sort_keys=True)
    return json_response


#if __name__ == "__main__":
#    main()