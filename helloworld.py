# 주석

# Hello World를 출력하는 코드
print('Hello, World!')

a, b = 100, 200
a, b = b, a + b

print(a, b)

text = 'Hello, World!'

print(text)

# 변수의 이름은 문자, 숫자, 밑줄(_), (!,@ 포함 X)
# 변수의 이름은 숫자로 시작 X, 공백을 포함할 수 없음

name = "강민준"
phone_number = "01052022508"
adress = "서울시 관악구"

print(name)
print(phone_number)
print(adress)

a = 5
b = -5

print(type(a), type(b))

d = 5.5
e = -5.5
f = 0.0

print(type(d), type(e), type(f))

g = 1.234567e5

print(g)

# 파이썬에서는 문자, 문자열 둘다 string으로 처리

text = "String \"Data\" Type"

# 탈출문자
# \', \", \\, \n, \r, \t

text1 = "Python is easy\n"
text2 = '''Python
is
easy'''

print(3 * text1)
print(text2)

a = 10
b = 20

print(a, b, sep='과')
print(a, b, end='\t')
print("3번째 라인")

# print() : 내장함수
# str.upper() : 메서드

# bool형 (참, 거짓)
True
False

# 거짓인 경우
# False, 0에 해당하는 값, 빈 문자