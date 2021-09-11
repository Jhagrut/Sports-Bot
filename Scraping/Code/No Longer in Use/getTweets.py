import twint
import nest_asyncio
import os
import pandas as pd

nest_asyncio.apply()

def getTweets():

    file = open('accountList.txt')
    text = file.readlines()
    file.close()
    userids = [userid.rstrip('\n') for userid in text]
    os.chdir(os.getcwd() + '\\TweetData')

    for usernames in userids:

        c = twint.Config()
        c.Username = usernames
        c.Limit = 100
        c.Store_csv = True
        c.Output = usernames + ".csv"
        c.Hide_output=True

        twint.run.Search(c)
        
    os.chdir(os.getcwd()[:-10])

    dataList = [pd.read_csv(os.getcwd()  + '\\TweetData\\' + files) 
                for files in os.listdir(os.getcwd()  + '\\TweetData')]

    data = pd.read_csv('merged.csv')

    for i in range(len(dataList)):
        data = data.append(dataList[i])
        
    data = data.drop_duplicates()
    data.to_csv('merged.csv', index=False)
