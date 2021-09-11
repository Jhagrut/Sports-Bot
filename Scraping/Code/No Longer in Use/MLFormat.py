import pandas as pd

def ifelse(boolean, ifValue, elseValue):
    if boolean:
        return ifValue
    else:
        return elseValue

def MLFormat():

    raw_data = pd.read_csv('merged.csv')

    raw_data['urls'] = raw_data['urls'].apply(lambda x: x.lstrip("[").rstrip("]"))
    raw_data['link_present'] = raw_data['urls'].apply(lambda x: ifelse(len(x) > 0, 1, 0))
    raw_data['photos'] = raw_data['photos'].apply(lambda x: x.lstrip("[").rstrip("]"))
    raw_data['photo_present'] = raw_data['photos'].apply(lambda x: ifelse(len(x) > 0, 1, 0))
    raw_data['retweet'] = raw_data['retweet'].apply(lambda x: ifelse(x, 1, 0))
    raw_data['injury_report'] = 'x'

    raw_data = raw_data[['injury_report', 'retweet', 'photo_present', 'link_present', 'replies_count', 'retweets_count',
         'likes_count', 'username', 'tweet']]

    filtered_data = pd.read_csv('filtered.csv')

    key_diff = set(raw_data.tweet).difference(filtered_data.tweet)
    where_diff = raw_data.tweet.isin(key_diff)

    filtered_data.append(raw_data[where_diff], ignore_index=True)

    filtered_data.to_csv('filtered.csv', index=False)
