'''
while True:
    a = input()
    if a == 'quit':
        exit()
    elif a == 'skip':
        print('rejected\n----------')
    else:
        print('{}\n----------'.format(a))
'''

# skip을 포함하는 문자열인 경우 rejected를 출력하고
# 구분선을 출력하지 않는 함수
def print_without_skip(string):
    if 'skip' in string:
        print('rejected')
        return
    else:
        print(string)
    print('-' * 10)

# quit를 입력할 때까지 반복하여 사용자 입력을 받음
user_input = ' '
while user_input != 'quit':
    user_input = input('input: ')
    print_without_skip(user_input)

