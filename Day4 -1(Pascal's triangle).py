i = int(input())

row=[[1]]
for k in range(i-1):
    temp=[0]+row[-1]+[0]
    rows=[]
    for j in range(len(row[-1])+1):
        mp = temp[j]+temp[j+1]
        rows.append(mp)
    row.append(rows)
print(row)