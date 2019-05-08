import csv
import pandas as pd

def readBody():
    array = []
    # with open('./soc-body.tsv') as tsvfile:
    with open('./redditData/soc-body.tsv') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            array.append(row)

        # select the colum
        toArr = list(map(lambda x:x[2], array))
        sentimentArr = list(map(lambda x:x[4], array))

        toArr.pop(0)
        sentimentArr.pop(0)

        
        df = pd.DataFrame({'to':toArr,'sentiment':sentimentArr})
        
        is_minus_1 =  df['sentiment']=='-1'

        df = df[is_minus_1]
        df = df.groupby(['to']).count()
        df = df.sort_values(by=['sentiment'], ascending=False)


        print(df.head(300))
        print(df.shape)



        


def readTitle():
    array = []
    with open('./soc-title.tsv') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            array.append(row)
        print(array)

readBody()