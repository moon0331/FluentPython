l=[1,2,3]
print(id(l))

l *= 2
print(l)
print(id(l))

print('-'*50)

t = (1,2,3)
print(id(t))

t *= 2
print(t)
print(id(t))

'''
>>> t = (1, 2, [30, 40])
>>> t[2] += [50, 60] #extend 는 오류 안난댄다
결과는??

1) t == (1, 2, [30, 40, 50, 60])
2) TypeError : 튜플 객체는 항목 할당을 지원하지 않음
3) 둘다 틀림
4) 둘다 맞음

정답 : 4)

'''

print('-'*50)

import dis
dis.dis('s[a]+=b')