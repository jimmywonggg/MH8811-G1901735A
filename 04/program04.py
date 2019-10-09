n_list=[9,41,12,3,74,15]
min_value=None
for i in n_list:
    if min_value==None:
         min_value=i
         continue
    if i<min_value:
        min_value=i
print('The list containing',n_list,'has:')
print('min',min_value)

#C2
print('The list containing',n_list,'has')
def my_min(ls):
    min_value=None
    for i in ls:
        if min_value==None:
            min_value=i
            continue
        if i<min_value:
            min_value=i
    return min_value
print('Min:',my_min(n_list))

def my_max(ls):
    max_value=None
    for i in ls:
        if max_value==None:
            max_value=i
            continue
        if i>max_value:
            max_value=i
    return max_value
print('Max:',my_max(n_list))

def my_average(ls):
    total_sum=0
    for i in ls:
        total_sum+=i
    average_value=total_sum/len(ls)
    return average_value
print('Average:',my_average(n_list))

def my_median(ls):
    ls.sort()
    i =int(len(ls)/2)
    if len(ls)%2 is 1:
        median_value=ls[i]
    else:
        median_value=(ls[i-1]+ls[i])/2     
    return median_value
print('median:',my_median(n_list))

def my_range(ls):
    range_value=max(ls)-min(ls)
    return range_value
print('range:',my_range(n_list))

#C3 against .csv files
def getFileLines(fname):
    fhandle = open(fname)
    lines =[]
    for line in fhandle:
        line =line.rstrip()
        if line:
            lines.append(line)
    return lines
my_list= getFileLines("MH8811-04-Data.csv")
my_list= list(map(float,my_list))
print("min:",my_min(my_list))
print("max:",my_max(my_list))
print("average:",my_average(my_list))
print("median:",my_median(my_list))
print("range:",my_range(my_list))

#Homework

def variance(my_list):
    average=my_average(my_list)
    total_sum=0
    for value in my_list:
        total_sum+=(value-average)**2
    variance=total_sum/(len(my_list)-1)
    return variance
print('sample variance:',variance(my_list))

