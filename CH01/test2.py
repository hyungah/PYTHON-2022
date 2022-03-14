# 1 ~ 10까지 더해서 값 출력
a = 0 #초기값 설정

for i in range(1, 11) :
    a += i
    print(" sum = " ,a)

# 1~ 10
sum = 0
for i in range(1, 11)  :
    sum += i
    # a = a + 1
    print(i , " + ", sum - i ,  "=" , sum)

print("total = " , sum)


# #1~ 10 짝수만 더해서 출력
sum = 0
for i in range(2, 11, 2)  : #step
    sum += i
    # a = a + 1
    print(i , " + ", sum - i ,  "=" , sum)

print("total = " , sum)

data = 'Hello ' + \
       'Good ' + \
       'morning! '
print(data)







