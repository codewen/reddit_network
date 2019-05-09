import csv
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt




def readTitle():
    array = []
    with open('./soc-title.tsv') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            array.append(row)
        


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
        TimeArr = list(map(lambda x:x[3][:10], array))
        sentimentArr = list(map(lambda x:x[4], array))
        # propArr = list(map(lambda x:x[5].split(',')[0], array))

        # remove heading
        fromArr.pop(0)
        toArr.pop(0)
        IDArr.pop(0)
        TimeArr.pop(0)
        sentimentArr.pop(0)
        # propArr.pop(0)

        
        df = pd.DataFrame({
            'source':fromArr,
            'target':toArr,
            'ID':IDArr,
            'Time':TimeArr,
            'sentiment':sentimentArr,
            # 'prop':propArr
        })
        
        # filter by contition

        hateArr = df[df['sentiment'] == '-1']
        # likeArr = df[df['sentiment'] == '1']

        hateArr = hateArr[hateArr['source'] == 'conspiracy ']
    
        hateArr = hateArr.filter(["source",'target'])
        # likeArr = likeArr.filter(["source",'target'])

        # group the data
        # hateArr = hateArr.groupby(['source']).count()
        # hateArr = hateArr.sort_values(by=['target'], ascending=False)

               
        print(hateArr)
        hateArr = hateArr.sort_values(by=['target'], ascending=False)

        


        return hateArr


def drawNetwork(df):
    
    G = nx.from_pandas_edgelist(df)
    pos = nx.spring_layout(G,k=0.3)
    d = nx.degree(G)
    # Plot it
    d = dict(d) 
    
    # d = {k:v for (k,v) in d.items() if v>1}

    nx.draw(G, pos, with_labels = True, nodelist=d.keys(), node_size = [v * 100 for v in d.values()])

    plt.show()




df = readBody()
drawNetwork(df)
