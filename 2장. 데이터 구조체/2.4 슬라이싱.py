l = [10, 20, 30, 40, 50, 60]
print(l[:2])
print(l[2:])
print(l[:3])
print(l[3:])

s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])

#예제 2-11 생략

l = list(range(10))
print(l)
l[2:5]=[20,30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11,22]
print(l)
# l[2:5]=100 
# 할당문의 대상이 슬라이스인 경우, 
# 항목 하나만 할당하는 경우에도 
# 할당문 오른쪽에는 반복 가능한 객체가 와야 한다.
l[2:5] = [100]
print(l)