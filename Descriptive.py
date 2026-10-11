def mean(data):
    answer= sum(data)/len(data) 
    return (answer)

def median(data):
    count=(len(data)%2)
    data. sort()
    if count == 1:
        answer = int((len(data))/2)
        return data[answer]
    else:
        answer1 = int((len(data)/2))
        answer2 = int(len(data)/2)-1
        total = (data[answer1] + data[answer2])/2
        return total

def mode(data):
    uniquelist=set(data)
    list = []
    for countlist in uniquelist:
        counts=data.count(countlist)
        list.append(counts)
    maxlist=[]
    maxval=max(list)
    for i in data:
        if data.count(i)==maxval:
            if i not in maxlist:
                maxlist.append(i) 
            else:
                continue
        else:
            continue
    return maxlist

def range(data):
    answer=max(data)-min(data)
    return answer

def Svariance(data):
    N=len(data)
    m=mean(data)
    list=[]

    for i in data:
        ms=(i-m)*(i-m)
        list.append(ms) 
    return sum(list)/(N-1)

def Sstd(data):
    answer=Svariance(data)**(1/2)
    return answer

def ZscoreS(data,x):
    z=(x-mean(data))/Sstd(data)

def quartiles(data):
    data.sort()
    Qone=(len(data)+1)/4
    Qtwo=(len(data)+1)/2
    Qthree=(3*(len(data)+1))/4
    return Qone,Qtwo,Qthree


data=[1,2,3,4,4,4,5,5,5,6,6,6,7,8,9]

print(mode(data))

