#Hackerrank question : push all zeroes to the end
'''Output Format

Elements of the modified list with each element separated by a space. After the last element, there should not be any space.

Sample Input 0

0 2 3 4 6 7 10
Sample Output 0

2 3 4 6 7 10 0'''
#CODE BEGINS
l=list(input().split(" "))
a=[]
x=[]
count=0
for i in l:
    if i=='0':
        count+=1
for j in range(0,count):
    a.append(0)
for k in l:
    if k!='0':
        x.append(k)
x.extend(a)
for i in x:
    print(i,end=" ")
    


