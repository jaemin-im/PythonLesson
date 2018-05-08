# count
a = 'programming'
res = a.count('m')
print(res)
# count함수가 메소드로 지정된 변수의 문자열에서 인자(문자)의 개수를 반환한다.

# find
a = 'programming'
res = a.find('m')
print(res)
# find함수가 메소드로 지정된 변수의 문자열에서 인자(문자)의 인덱스를 반환한다.
# 없을 경우 -1을 반환한다. -1을 반환하기 때문에 연산이 가능하다. ex) if(res == -1)

# index
a = 'programming'
res = a.index('m')
print(res)
# index함수가 메소드로 지정된 변수의 문자열에서 인자(문자)의 인덱스를 반환한다.
# 없을 경우 ValueError를 반환한다.

# join
a = '_m-_-m_'
res = a.join('ABC')
print(res)
# join함수가 메소드로 지정된 변수의 문자를 인자(문자) 사이에 삽입한다.
# 한 줄씩 엔터가 되게 하고 싶을 때에는? 메소드 지정 변수의 문자를 \n으로 설정한다.
# ex) a = '\n', a.join('ABC')

# upper
a = 'programming'
res = a.upper()
print(res)
# lower
a = 'PROGRAMMING'
res = a.lower()
print(res)
# 각각 대문자, 소문자로 변환한 값을 출력한다.
# 특수문자에 대해서도 될까? => upper, lower 둘 다 안된다.

# replace
a = 'programming'
res = a.replace('gramming', 'gamer')
print(res)
# 문자열을 치환한 결과를 반환한다.
# join과 다른 점 : 공백('')을 replace할 경우 맨 처음과 끝에도 치환이 된다.
# ex) a = 'abcd', a.replace('', '1') = '1a1b1c1d1'
# 해당되는 대상 문자열(1번째 인자)이 없을 경우 결과는 바뀌지 않는다.

# split
a = '   pro gramm ing   '
res = a.split(' ')
print(res)
# 문자열을 나눈 결과를 반환한다. => 리스트 타입으로 반환
# a = 'a1p1p1l1e', res = a.split('1'), print(res[0]+res[1]+res[2]+res[3]+res[4])
# 결과가 리스트이므로 나눈 결과를 결합하려면 인덱스를 활용한다.

# lstrip
a = '   programming   '
res = a.lstrip()
print(res)
print(res + '1') # 오른쪽 공백이 제거되지 않음을 확인

# rstrip
a = '   programming   '
res = a.rstrip()
print(res) # 왼쪽 공백이 제거되지 않음을 확인
print(res + '1') # 오른쪽 공백이 제거되었음을 확인

# strip
a = '   programming   '
res = a.strip()
print(res + '1') # 왼쪽과 오른쪽 공백이 제거되었음을 확인

# type
a = 'programming'
res = a.split()
print(type(res))
res = type(a)
print(res) # type값은 변수에 들어갈 수 있고, 출력도 된다.

# str
a = 123
res = str(a)
print(res * 10) # 곱을 이용하여 str과 int 구별
# 숫자를 문자열로 바꾼다.

# int
a = '123'
res = int(a) # 실수로 바꾸려면 float(a)
print(res * 10) # 곱을 이용하여 str과 int 구별
# 문자열을 숫자로 바꾼다.

# ord
a = 'A'
res = ord(a)
print(res)
# 문자를 아스키코드(정수)로 바꾼다.

# chr
a = 65
res = chr(a)
print(res)
# 정수에 해당되는 아스키코드 문자를 반환한다.

# ================================================ #

# append
res = [1, 2, 3]
res.append(4)
print(res)
# append함수의 인자를 문자열 뒤에 추가한다.

# sort
res1 = ['e', 'a', 'h']
res2 = [1, 6, 2]
res1.sort()
res2.sort(reverse=True) # Python의 참, 거짓은 True, False
print(res1)
print(res2)
res3 = sorted(res1)
res4 = sorted(res1, reverse=True)
res3.reverse() # 옵션을 쓰지 않고 reverse()를 이용하여 내림차순 변환 가능
print(res3)
print(res4)
# Tip: sorted는 딕셔너리 정렬이 가능하다, sort는 불가능
a = {'2': 'B', '1': 'A', '3': 'C'}
a1 = sorted(a)
print(a1)

# insert
res = [100, 123, 523]
res.insert(1, 1+1)
print(res)
# 특정 인덱스의 값이 되도록 요소를 추가한다.

# remove
res = [10, 20, 30, 40, 10]
res.remove(10)
print(res)
# 함수의 인자값을 찾아서 삭제한다.
# 값이 여러개라면 가장 첫 번째 요소를 삭제한다.

# pop
res = [10, 20, 30, 40]
a = res.pop() # 반환값이 있다.
print(a)
# 마지막 요소를 삭제한다.
# 반환값이 있으므로 변수에 pop한 값을 저장할 수 있다.

# count
a = [10, 10, 101, 102, 5 + 5, 'ab']
res = a.count(10) # 3
print(res)
# 함수의 인자값을 찾아서 개수를 센다.

# ======================================================= #
# 딕셔너리 함수

# keys
a = {'a': 123, 'b': 456}
res = list(a.keys())
print(res)

# values
a = {'a': 123, 'b': 456}
res = list(a.values())
print(res)

# items
a = {'a': 123, 'b': 456}
res = list(a.items())
print(res)

# get
a = {'q': 123, 'w': 456}
res = a.get('t', 789) # None일 경우 2번째 인자를 반환
print(res)
# 대상 값이 있다면, 그 키의 value를 반환
# 대상 값이 없다면, get함수는 None을 반환(인자가 1개일 경우), a['X']는 에러 반환

# in
a = {'q': 123, 'w': 456}
print('q' in a)
# 키 값이 있다면 True, 없다면 False
