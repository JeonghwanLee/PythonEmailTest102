# Test data
txt = open("Email Coding C102.txt")
data = txt.read()
# Define global variables and lists
start = 0
row = []
A,B,C,D,E,F,G,H,I,J = [],[],[],[],[],[],[],[],[],[]
matrices = [A,B,C,D,E,F,G,H,I,J]
mean =[]
median = []
preMedian = []

#Correct data values to float and assign them to matrices
for i in range(0, data.count('|')):
    while start < len(data):
        #Define locations for comma, semicolon and vertical bar
        commaLoc = data.find(',',start)
        semiLoc = data.find(';',start,commaLoc)
        barLoc = data.find('|',start,commaLoc)
        if semiLoc == -1 and commaLoc > 0 and barLoc == -1:
            if data[start:commaLoc] == "float('nan')" or data[start:commaLoc] == "float('inf')" or data[start:commaLoc] == "-float('inf')":
                row.append(0)
                start = commaLoc +1
            else:
                row.append(float(data[start:commaLoc]))
                start = commaLoc +1
        elif barLoc == -1 and semiLoc >0:
            if data[start:semiLoc] == "float('nan')" or data[start:semiLoc] == "float('inf')" or data[start:semiLoc] == "-float('inf')":
                row.append(0)
                matrices[i].append(row)
                start = semiLoc + 1
                row=[]
            else:
                row.append(float(data[start:semiLoc]))
                matrices[i].append(row)
                start = semiLoc + 1
                row=[]
        else:
            if barLoc == len(data)-1:
                if data[start:barLoc] == "float('nan')" or data[start:barLoc] == "float('inf')" or data[start:barLoc] == "-float('inf')":
                    row.append(0)
                    matrices[i].append(row)
                    start = len(data)
                else:
                    row.append(float(data[start:barLoc]))
                    matrices[i].append(row)
                    start = len(data)
            else:
                if data[start:barLoc] == "float('nan')" or data[start:barLoc] == "float('inf')" or data[start:barLoc] == "-float('inf')":
                    row.append(0)
                    matrices[i].append(row)
                    start = barLoc + 1
                    row=[]
                    break
                else:
                    row.append(float(data[start:barLoc]))
                    matrices[i].append(row)
                    start = barLoc + 1
                    row=[]
                    break

#Mean and Median
#Gather mean of each matrix (i,j)
subSum = 0
for y in range(0,len(A)):
    row = []
    for z in range(0,len(A[0])):
        for x in range(0,len(matrices)):
            subSum = subSum + matrices[x][y][z]
        row.append(subSum/len(matrices))
        subSum = 0
    mean.append(row)
#Gather median of each matrix (i,j)
for y in range(0, len(A)):
    row = []
    for z in range(0, len(A[0])):
        for x in range(0, len(matrices)):
            preMedian.append(matrices[x][y][z])
        if len(preMedian)%2 != 0:
            row.append(sorted(preMedian)[len(preMedian)/2])
        else:
            midavg = (sorted(preMedian)[len(preMedian)/2] + sorted(preMedian)[len(preMedian)/2-1])/2.0
            row.append(midavg)
        preMedian = []
    median.append(row)
        

print len(mean)
print len(median)