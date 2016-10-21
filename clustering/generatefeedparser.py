import feedparser
import re

def getwordcounts(url=None):
    if url == None:
        return None
    WordCounter = {}
    channel = feedparser.parse(url)
    for replay in channel.entries:
        if 'summary' in replay:
            summary = replay.summary
        else:
            summary = replay.descript
        words = getwords(replay.title+' '+summary)
        for word in words:
            WordCounter.setdefault(word,0)
            WordCounter[word] +=1
    return channel.feed.title,WordCounter

def getwords(html):
    txt = re.compile(r'<[^>]+>').sub('',html)
    words = re.compile(r'[^А-Я^а-я]+').split(txt)
    return [word.lower() for word in words if word !='']
    
def DataGenerate(InputFille='chennel.txt',OutputFille='clustering.txt'):
    apcount = {}
    wordcounts = {}
    for feedurl in open(InputFille,'r').readlines():
        print(feedurl)
        try:
            title,WordCounter = getwordcounts(feedurl)
        finally:
            pass
        wordcounts[title] = WordCounter
        for word,count in WordCounter.items():
            apcount.setdefault(word,0)
            if count > 1:
                apcount[word] += 1
    wordlist = []
    for w,bc in apcount.items():
        frac = float(bc) / len(InputFille)
        if frac > 0.1 and frac < 0.5:
            wordlist.append(w)
    out = open(OutputFille,'w')
    out.write('Blog')
    for word in wordlist:
        out.write('\t%s' % word)
    out.write('\n')
    for blog,wc in wordcounts.items():
        out.write(blog)
        for word in wordlist:
            if word in wc:
                out.write('\t%d' % wc[word])
            else:
                out.write('\t0')
        out.write('\n')
def LoadData(FileName='clustering.txt'):
    FileData = open(FileName,'r')
    Lines = [line for line in FileData.readlines()]
    ColumnName = Lines[0].strip().split('\t')[1:]
    BlogData = {}
    for line in Lines[1:]:
        record = line.strip().split('\t')
        BlogName = record[0]
        RowsData = [float(data) for data in record[1:]]
        CounterWord = {key: value for (key, value) in zip(ColumnName,RowsData)}
        BlogData[BlogName] = CounterWord
    return BlogData
    
if __name__ == '__main__':
    #DataGenerate()
    Data = LoadData()
    print(Data)
    print(Data['Яндекс.Новости: Главные новости'])
    #iter = 0
    #for feedurl in open('chennel.txt','r').readlines():
    #    print(iter, feedurl)
    #    try:
    #        title,WordCounter = getwordcounts(feedurl)
    #    finally:
    #        pass
    #    iter += 1
    #print(getwordcounts('http://www.aif.ru/rss/realty.php'))
    #print(getwordcounts('http://www.gazeta.ru/export/gazeta_rss.xml'))
            