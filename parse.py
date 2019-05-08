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
        fromArr = list(map(lambda x:x[0], array))
        toArr = list(map(lambda x:x[1], array))
        IDArr = list(map(lambda x:x[2], array))
        TimeArr = list(map(lambda x:x[3], array))
        sentimentArr = list(map(lambda x:x[4], array))
        propArr = list(map(lambda x:x[5].split(',')[0], array))

        fromArr.pop(0)
        toArr.pop(0)
        IDArr.pop(0)
        TimeArr.pop(0)
        sentimentArr.pop(0)
        propArr.pop(0)

        
        df = pd.DataFrame({
            # 'from':fromArr,
            # 'to':toArr,
            'ID':IDArr,
            # 'Time':TimeArr,
            # 'sentiment':sentimentArr,
            'prop':propArr
        })
        print(df.shape)
        
        is_minus_1 =  df['ID']=='3yj2ee'


        df = df[is_minus_1]
        print(df)
        # df = df.groupby(['to']).count()
        # df = df.sort_values(by=['sentiment'], ascending=False)

        # print(df.shape)



        


def readTitle():
    array = []
    with open('./soc-title.tsv') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            array.append(row)
        print(array)

readBody()