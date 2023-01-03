input='12341234'
output=[]
a=[]
for i in input:
    if i=='0':
        output.append(9)
    else:
        output.append(str(9-int(i)))
for i in range(len(input)):
    if int(input[i]!=int(output[i])):
        a.append(min(input[i],output[i]))
print(''.join(a))
