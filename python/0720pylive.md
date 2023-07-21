# 0720 python live

## control of flow
### 제어문
실행 흐름을 제어, 조건에 따라 코드블록을 실행하거나 반복적으로 코드를 실행

### 조건문
조건실을 평가하여 해당 조건이 참인 경우에만 코드 블록을 실행하거나 건너뜀

```python
num = int(input('숫자를 입력하세요 : '))

#if statement
#num이 홀수라면 (2로 나눈 나머지가 1이라면)
if num % 2 ==1: 
  #(= num % 2 결과 같음)
  print('홀수입니다')
#numdl 홀수가 아니라면(짝수)
else:
  print('짝수입니다')

```

## 반복문
코드 블록을 여러 번 반복해서 실행하는 구문
- 특정 작업을 반복적으로 수행
- 주어진 조건이 참인 동안 반복 수행

### for
임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복
(순서 o, 길이 o)

- 반복 횟수가 명확하게 정해져 있는 경우
- 리스트, 튜플, 문자열과 같은 시퀸스 형식의 데이터를 처리할 때

``` python
# 인덱스로 리스트 순회
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
  numbers[i] = numbers[i] * 2

print(numbers)
  

```

``` python
# 중첩 반복문
outers = ['a', 'b']
inners = ['c', 'd']

for outer in outers:
  for inner in inners:
    print(outer, inner)

#A, c
#A, d
#B, c
#B, d    
# print가 호출되는 횟수 = len(outers) * len(inners)
```

``` python
# 중첩리스트 순회
 elements = [['A', 'B'], ['c', 'd']]


 for elem in elements:
  for item in elem:
    print(item)

"""
A
B
c
d
"""    
```



### while
 주어진 조건식이 참인 동안 코드를 반복해서 실행, 조건이 거짓이 될때까지 반복

 - 반복 횟수가 불명확 하거나 조건에 따라 반복을 종료해야 할 경우
 - 예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우

``` python
a =0

while a < 3:
  print(a)
  a += 1
print('끝')

'''
0
1
2
끝
'''
```

``` python
 number = int(input('양의 정수를 입력해주세요.: '))

 while number <= 0:
  if number < 0:
    print('음수를 입력했습니다.')

  else:
    print('0은 양의 정수가 아닙니다.')

  number = int(input('양의 정수를 입력해주세요.: '))    
```

## 반복 제어

### break
반복을 즉시 중지

``` python
numbers = [1, 3, 5, 6, 7, 9, 10, 11 ]
found_even =False

for num in numbers:
  if num % 2 ==0:
    print('첫번째 짝수를 찾았습니다: ', num)
    found_even = True
    break

if not found_even:
  print('짝수를 찾지 못헀습니다')

  '''
  첫번째 짝수를 찾았습니다: 6
  '''  
```

### continue
다음 반복으로 건너뜀
``` python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
  if num % 2 ==0:
    continue
  print(num)

```

### 주의사항
- 가독성을 저하 시킬수있음
- 코드의 가독성을 유지하고 코드의 의도를 명확하게 작성하도록 노력해야함


### list Comprehension
간결하고 효율적인 리스트 생성 방법

``` python 
# 1~10 요소를 가지는  리스트 만들기

# 1. 일반적인 방법
new_list= []
for i in range(10):
  if i% 2 ==1:
     new_list.apped(i)
  else:
    new_list.append(str(i))   
print(new_list)


# list comprehension
new_list_2 = [ i for i in range(10) if i % 2 ==1]
 new_list_3=[i if i%2==1 else str (i) for i in range(10)]
print(new_list_2)

```

### 리스트를 생성하는 3가지 방법 비교

1. for loop

``` python
numbers = ['1', '2', '3']
#정수 123을 가지는 새로운 리스트 만들기

new_numbers= []
for number in numbers:
  new_numbers.append(int(number))
```
2. map
```python
new_numbers_2 = list(map(int, numbers))
```

3. list comprehension

```python
new_numbers_3 = [int (number) for number in numbers]
```

### pass
아무런 동작도 수행하지 않고 넘어가는 역할
1. 코드 미완성 부분
2. 조건문에서 아무런 동작을 수행하지 않아야할때
3. 무한루프에서 조건이 충족되지않을때 루프를 계속 진행하는 방법

### enumerate
```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
  print(f'인덱스 {index} : {fruit}')

'''
인덱스 0: apple
인덱스 1: banana
인덱스 3: cherry
```