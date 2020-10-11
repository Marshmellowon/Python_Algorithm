def function():
    n = 0
    while True:
        n += 1
        yield n


# mypy로 타입 힌트 오류 발견 가능
# pip install mypy
g = function()
for _ in range(0, 100):
    print(next(g))

'''-----------------'''

a = [n for n in range(10000)]
b = range(10000)
print("=------------------------=")
"""enumerate: 순서가 있는 자료형"""
# list set tuple 등에 쓰인다
a1 = [1, 2, 3, 4, 5, 6]
print(list(enumerate(a1)))

print("--------------")
a2 = 0
for i, v in enumerate(a1):
    print(i, v)
print("--------------")
'''몫을 구하는 연산자 //'''
'''print(a,b sep=',)'''
# 리스트 출력은 join()으로 한다.
oo: str = "AL"
uu: str = "kl"
print(oo, uu, sep='-')
oi = ['a', 'l']
print(','.join(oi))
print("--------------")
'''locals'''
import pprint

pprint.pprint(locals())

# TODO: page 95까지 봄
