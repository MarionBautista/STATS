import math

def factorial(n):
    answer=1
    for i in range(n):
        answer=answer*(i+1) 
    return answer

def permutation(n,r):
    answer=factorial(n)/factorial(n-r)
    return answer

def Combination (n,r):
    answer=factorial(n)/factorial(r)*factorial(n-r)
    return answer

def BasicProbability(f,t):
    return f/t

def ComplementRule(p):
    return 1-p

def AdditionRule(a,b,c):
    return a+b-c

def it(a,b):
    return a*b

def IndependentEvents(a,b):
    return a*b

def ConditionalProbability(a,b):
    return a/b

def ExpectedValue(v,p):
    total=0
    zip=zip(v,p)
    for a,b in zip:
        total=total+(a*b) 
    return total

def DiscreteProbability(a):
    count=len(a)
    unique=set(a)
    probabilities=[]
    for x in unique:
        percent=a.count(x)/count
        probabilities.append(percent)
        
    return probabilities
  
 
def binomial(a,b,c):
    answer=Combination (a, b) * c**b * ComplementRule(c)**(a-b)
    return answer

#much efficient if we use math.erf

def ErrorFunction(x,steps):
    sum=0
    t=x/steps
    for i in range(steps):
        sum=sum+math.e**(-(t*i)**2)*t
    return 2/math.sqrt(math.pi)*sum
    
def NormalPDF(x, mean, sd):
    answer=(1/(sd*(math.sqrt(2*math.pi))))*math.e**(-((x-mean)**2)/(2*sd**2))
    return answer

def NormalCDF(x,mean,std):
    answer=(1/2)*(1+math.erf((x-mean)/(std*math.sqrt(2))))
    return answer

def ContinuesProbability(upper,lower,mean,sd):
    answer=NormalCDF(upper,mean, sd)-NormalCDF(lower,mean, sd) 
    return answer

