symbols = '각}₩|μ'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

codess = [ord(symbol) for symbol in symbols]

print(codes == codess)

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

print('='*50)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

for color in colors:
    for size in sizes:
        print((color, size))

tshirts = [(color, size) for size in sizes 
                         for color in colors]
print(tshirts)

print('='*50)

print(tuple(ord(symbol) for symbol in symbols))
import array
print(array.array('I', (ord(symbol) for symbol in symbols)))

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)