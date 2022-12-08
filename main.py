import tweepy
import keys


def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)


# make the bot follows a user


def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print("Tweeted Successfully")


if __name__ == '__main__':
    api = api()
    # tweet(api, message="This was tweeted from python", image_path="image.png")
    api.destroy_friendship(screen_name="elonmusk")
