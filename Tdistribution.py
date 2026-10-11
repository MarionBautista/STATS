import math

def DF(n):
    return n.count-1

def TdistributionPDF(t,n):
    answer =(math.gamma((DF(n)+1)/2)/math.sqrt(DF(n)*math.pi()*math.gamma(DF(n)/2))