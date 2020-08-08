# 튜플은 불변 리스트로 사용할 수도 있지만 필드명이 없는 레코드로 사용할 수도 있다.

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP','XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

print('-'*50)

lattitude, longitude = lax_coordinates # tuple unpacking
print(lattitude)
print(longitude)

print('-'*50)

x, y = 20, 8
print(divmod(x, y))
t=(x, y)
print(divmod(*t))
quotient, remainder = divmod(*t)
print(quotient, remainder)

print('-'*50)

import os
dirname, filename = os.path.split('/Users/kjmoon/Dropbox/FluentPython/2장. 데이터 구조체/2.3 튜플은 단순한 불변 리스트가 아니다.py')
print(dirname)
print(filename)

for val in (5,3,2):
    a, b, *rest = range(val)
    print(a, b, rest, sep=' | ')

print('-'*50)

a, *body, c, d = range(5)
print(a, body, c, d, sep=' | ')

print('-'*50)

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.4333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635888)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

print('-'*50)

from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])

print('-'*50)

print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi)
print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ':', value)

print('-'*50)

