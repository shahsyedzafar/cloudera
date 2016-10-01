def KMP_Algorithm(text, list):
    #converting list into pattern string
    pattern = ''
    for x in list:
        for y in x:
            pattern += y

    '''Yields all starting positions of copies of the pattern in the text.
    Calling conventions are similar to string.find, but its arguments can be
    lists or iterators, not just strings, it returns all matches, not just
    the first one, and it does not need the whole text in memory at once.
    Whenever it yields, it will have read the text exactly up to and including
    the match that caused the yield.'''

    # allow indexing into pattern and protect against change during yield
    pattern = list(pattern)

    # build table of shift amounts
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos - shift]:
            shift += shifts[pos - shift]
        shifts[pos + 1] = shift

    # do the actual search
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == len(pattern) or \
                                matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(pattern):
            yield startPos



def euclidean_distance(str, ch):
    sum=0
    for i in str:
        difference = str-ch
        sum += difference ** 2
    sum = sum ** (0.5)


# In this algorithm we get take string x, Observed CPU Workload Time series and after calculations get String z.
#cpu_workload = [3, 15, 16, 18, 19, 15, 20, 15, 15, 12, 14, 16, 19, 14, 14, 22, 16, 16, 13, 15]
cpu_workload = [3, 15, 18]

#print (cpu_workload)
cpu_workload_time_diff = []
i=0
for index in range(len(cpu_workload) - 1):
    y =  cpu_workload[index+1] - cpu_workload[index]
    cpu_workload_time_diff.insert(i, y)
    i += 1
s=[]
print (cpu_workload_time_diff)
l=0
#building s
for index in range(len(cpu_workload_time_diff)):
    if (cpu_workload_time_diff[index] == 0):
        s.insert(l,'i')
    elif (cpu_workload_time_diff[index] == 1):
        s.insert(l, 'k')
    elif (cpu_workload_time_diff[index] == 2 or cpu_workload_time_diff[index] == 3):
        s.insert(l, 'l')
    elif (cpu_workload_time_diff[index] == 4 or cpu_workload_time_diff[index] == 5):
        s.insert(l, 'm')
    elif (int(cpu_workload_time_diff[index]) > 5):
        s.insert(l, 'n')
    elif (cpu_workload_time_diff[index] == -1 or cpu_workload_time_diff[index] == -2):
        s.insert(l, 'g')
    elif (cpu_workload_time_diff[index] == -3 or cpu_workload_time_diff[index] == -4):
        s.insert(l, 'f')
    elif (cpu_workload_time_diff[index] <= -5):
        s.insert(l, 'e')
    l += 1


# s[1..l] is the output of pre-processing step
print (s)
C_his_pattern_list=[[ 'e', 'f', 'g'], ['i', 'k', 'l'], ['m', 'n', 'f']]
num = len(C_his_pattern_list) - 1

#ing = ''.join(s)
C_his_pattern_string = ''
for x in C_his_pattern_list:
    for y in x:
        C_his_pattern_string += y

#converting to strings
print (C_his_pattern_string)

#s and C_his_pattern_string are input to 2nd step

dis=[]
for index in range(num):
    dis.insert(0)

s_size = len(s)-1

while(num!=0):
   length = len(C_his_pattern_list[num])

   tag = KMP_Algorithm(s, C_his_pattern_list[num-1])
   if(tag != -1):
       print (C_his_pattern_list[num])
   else:

       dis[num] = float('inf')
   for i in range(0,length-s_size):
       dis_l = euclidean_distance(s, C_his_pattern_list[num][i])
       if dis_l<dis_num:
           dis_num = dis_l

min=dis[0]
min_index=0
for index in range(len(dis)):
    print (index)
    if dis[index]<min:
        min=dis[index]
        min_index=index

print (min)
print (min_index)
print (C_his_pattern_list[num])







