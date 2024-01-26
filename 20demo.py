# 20demo.py by Christina Chen

import math
import sys

## Math

print('hello, again') # greeting

print(1 + 1)
print("1" + "1") # this means the "1" is  an integer, not a numeric
print(2 ** 3)
print(5 // 2)
print(5 % 2)
print(5 * (2 + 1))

print(abs(-42))
print(pow(4, 3))
print(round(123.3423413, ndigits = 3))

print(math.sqrt(64))

print(math.pi)
print(round(math.pi, ndigits=4))
print(math.inf)
print(math.nan)

print(0.1 * 1)
print(0.1 * 3)

## Variables

a = 3						# side of triangle
b = 4						#side of triangle
c = math.sqrt(a**2 + b**2)	# hypotenuse
print(c)

print(type(a), type(b), type(c), sep=', ')

## Functions

def	greeting():
	print('hello yourself')

greeting()
	
def pythagora(a, b):
	assert(a > 0)
	assert(b > 0)
	return math.sqrt(a**2 + b**2)
	
def pythagoras(a, b):
	if a <= 0: sys.exit('error: a must be greater than 0')
	if b <= 0: sys.exit('error: b must be greater than 0')
	return math.sqrt(a**2 + b**2)

x = pythagora(3, 4)
print(x)

print(pythagoras(1, 1)) # if this was "-1, 1", then the error would appear

## Practice

def negpos(a):
	return a * -1

print(negpos(3))
print(negpos(-4))

def areas(a, b):
	assert(a > 0)
	assert(b > 0)
	return a * b

print(areas(5, 10))

def midpoint(x1, y1, x2, y2):
	mx = (x1 + x2) / 2
	my = (y1 + y2) / 2
	return mx, my

print(midpoint(1, 1, 3, 3))

s = 'hello world'
print(s, type(s))

## Conditionals

a = 2
b = 2
if a == b:
	print('a equals b')
print(a, b)

c = a == b
print(c)
print(type(c))

if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')

if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

a = 0.3
b = 0.1 * 3

if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')

print(abs(a - b))
if abs(a - b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

a = 1
s = 'G'
#if a < s: print('a < s')

