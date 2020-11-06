# ex) 01 메시지 출력 / 한줄 주석 #, 단축키 ctrl + /
# print(10)
#
# ex) 02 전체 주석, ''' ''' or """ """
# '''
# print(10)
# print(20)
# '''
#
# ex) 03 문자열(싱글 코텐션), 숫자열 출력
# '''
# print('호랑이')
# print(12345)
# '''
#
# ex) 04 문자열+숫자열 출력, 변수간 붙여도 콤마는 알아서 스페이스로 한칸띄움
# print(10,'호랑이',20,'독수리',3.14)
#
# ex) 05 true, false 출력시 헤드 무조건 대글자, boolean 타입 시
# print(True, False)
#
# ex) 06 세미콜론, 코드만 한줄 처리 출력
# print(10) ; print(20)
#
# ex) 07 디폴트 값 입력, 한줄 처리 출력
# print(10, end=" ")
# print(20)
#
# ex) 08 세퍼레이트, 구분선 출력
# print('-------------------')
#
# ex) 09 세퍼레이트를 곱한 숫자만큼 출력, 특수문자 대부분 가능
# print('*' * 50)
# print('-' * 50)
#
# ex) 10 %s %d 는 뒤와 대치
# print('코끼리%s' % '어카') # %s는 문자열 가능, 뒤 문자를 땡겨옴
# print('코 %d %d %s 끼리' % (10, 20, '호랑이'))
#
# ex) 11 sep, 기본 디폴트 값을 원하는 문자로 채우고자 할때, 그리고 end로 한줄처리까지
# print(10,20,30,40)
# print(10,20,30,40,sep=(',')) # 콤마 넣어서 출력
# print(10,20,30,40,end=(' '))
# print(10,20,30,40)
#
# ex) 12 type(), 변수의 타입을 확인
# print(type('호랑이'), type(10), type(3.14), type(True))
#
# ex) 13 클래스 타입 : 'list'-> [], 'dict'->{}, 'tuple'->()
# print(type([]), type(()), type({}))
#
# ex) 14 int(' ') / str(' '), 문자열 <-> 숫자열 변환
# print(10+20)
# print(10+'호랑이') # 숫자열+문자열, 문법 성립 불가
# print('호랑이'+10) # 문자열+수자열, 문법 성립 불가
# print('호랑이' , '독수리') # 문자열+문자열, 성립 가능
# print(10+int('123')) # 문자열 -> 숫자열
# print('호랑이'+str('10')) # 숫자열 -> 문자열
#
# ex) 15 변수 선언 유형
#  유형1. 변수를 선언하는 타입 없음, int a (X)
# a = 10
# b = 20
# print(a,b)
#
#  유형2. 변수 중복 및 간략 표기 가능
# a = 30; b = 40; # 세미콜론으로 구분하여 한줄 입력
# print(a,b)
#
# a = 10, b = 20 # 변수 간 콤마 구분은 불가
# print(a,b)
#
# a,b = 50,60 # 최종 선언 변수만 출력
# a,b,c = 1,2,3
# print(a,b,c)
#
# a= b= 70
# print(a,b)
#
# ex) 16 스왑 프로그램, 데이터 교환
# a = 10
# b = 20
# b, a = a, b
# print(a,b)
#
# tip) 문장 블록 씌우고 코텐션 3번 누르면 블럭 주석
#
# ex) 17 다항 연산자
# a = 100; a++ # 다항연산자, 불가
# print(a)
#
# a = 100 # 다항연산자, 가능
# a = a + 1
# a += 1
# print(a)
#
# ex) 18 id, 변수의 고유 식별번호
# a = 10; b = 20; c = 10; # a와 c의 변수가 같으므로 id도 동일, 메모리 절감
# print(id(a), id(c))
#
# a = '호랑이'; b = '코끼리'; c = '호랑이';
# print(id(a), id(c))
#
# ex) 19 16진수, 8진수 출력
# a = 0x20
# print(a)
# b = 0o376
# print(b)
#
# ex) 20 복소수, 상수는 상수끼리 계산
# a = 1 + 2j
# b = 3 + 4j
# print(a + b)
#
# ex) 21 나누기, 나머지, 몫 구하기
# a = 10; b = 3;
# print(a/b, a%b, a//b)
#
# ex) 22 제곱 값 구하기, 2의 8 제곱
# print(2**8)
#
# ex) 23 round, 소수점 절삭
# print(round(3.1415, 2))
#
# ex) 24 배열, 문자의 순서 위치 파악
# str = 'apple'
# print(str[2])
#
# str = '무궁화 꽃이 피었습니다.'
# print(str[4])
#
# 배열   1 23 4 56 7 8910
# str = '무궁화꽃이피었습니다'
# print(str[2:5]) #인덱스 2에서 시작, 5-2개를 가져온다.
#
# str = '무궁화꽃이피었습니다.'
# print(str[:5]) # 첫 인덱스 생략시 처음부터
#
# str = '무궁화꽃이피었습니다'
# print(str[5:]) # 지정 인덱스 부터 끝까지
#
# str = '무궁화꽃이피었습니다'
# print(str)
# print(str[:]) # 동일한 출력 코드, 병행 사용 하는 경우 있음
#
# ex) 25 배열 바꾸기 불가한 문법
# str = 'apple'
# a = str[0]
# b = str[:2]
# str[0] = 'B' # 스펠 교체 문법 불가, 변수가 상수화되어서 갱신은 불가
# print(str)
#
# str = 'apple'
# c = 'B' + str[1:] # 스펠 교체 가능,
# 문자열 더하기 변수 일부
# print(c)
#
# ex) 26 %d, %s
# print('호%d랑%s이' % (10 , '코끼리'))
# print('호%d랑이' % 10) #대입 변수가 한개면 괄호 생략
#
# ex) 27 format 함수, 대입, 인덱스 넣어서 원하는 위치에 대입 가능
# print('무궁화{2}꽃이{0}피었습니다{1}호랑이'.format(10,'코끼리',20))
#
# s = '무궁화꽃이{0}피었습{1}니다'
# print(s)
#
# s.format(10,'호랑이')
# print(s)
#
# t = s.format(10,'호랑이')
# print(t) # s를 포맷하여 대입한후 t로 출력
#
# t = s.format(10,'호랑이')
# print(s)
#
# ex) 28 문자열 글자수 확인, 해당 단어 카운팅
# s = '무궁화꽃이피었습니다'
# print(len(s))
#
# s = '무궁화꽃이무궁화피었무궁화습니다무궁화'
# print(s.count('무궁화'))
#
# print('무궁화꽃이무궁화피었무궁화습니다무궁화'.count('무궁화')) # 위 문장과 동일
#
# s = '무궁화꽃이꽃이피었습니다'
# print(s.find('피엇')) # 문자 배열의 인덱스 번호를 알려줌, 결과 없으면 -1로 리턴
#
# ex) 29 문자 치환, 대소문자 변경
# s = 'Apple'
# t = s + 'Orange'
# s = s + 'Banana'
# print(s.lower()) # 모두 소문자로 변경
#
# print(s)
# t = (s.lower())
# print(t)
# print(s.upper()) # 모두 대문자로 변경
# print(s.replace('Banana', 'Orange')) # 바나나를 오렌지로 치환
# print(s.replace('banana', 'ORANGE'))
# #
# ex) 30 문자열 쪼개기 -> 결과 : ['무궁화', '꽃이', '피었습니다'] -> 리스트(배열)프레임을 통해 결과 3개를 줌
# s = '무궁화 꽃이 피었습니다'
# print(s.split())
# t = s.split()
# print(t)
# print(len(t)) # 리스트의 크기(개수) 카운팅
# print(t[0], t[1]*3, t[2]) # 리스트니까 리스트 구분하여 출력, 반복 출력 가능
# print(s.split(':')) # 콜론으로 특정 단어들을 구분가능
#
# ex) 31 산술, 관계, 논리 연산 / 복합 연산 우선순위는 산술>관계>논리
# print(16+3, 16-3, 16*3, 16/3, 16//3, 16%3, 16**3) # 산술 연산
# print(3<2, 3 >= 3 ) # 관계 연산, 자바와 동일
# print(3 <= 3)
# print(3 == 3)
# print(3 != 3)
#
# print(False and False) # 논리 연산
# print(False and True)
# print(True and False)
# print(True and True) # false 있으면 false
#
# print(False or False)
# print(False or True)
# print(True or False)
# print(True or True) # True 있으면 True
#
# print(not(3 > 2)) # 부정 연산, 코드 변경 없이 반대 결과 확인 하고싶을때
#
# print(3+2 > 4 and 6 < 2*4)
# print(5 > 4 and 6 < 8)
# print(True and True)
# print(((3+2) > 4) and (6 < (2*4))) # 위와 같은 문장, 산술이 우선, 우선순위 잘 볼 것
#
# ex) 32 import
# from random import *
# print(random()) # 0.0 ~ 1.0 값 랜덤 추출, 시뮬레이션 데이터 활용 가능
# print(randint(3,5)) # 3 <= x <= 5, 3~5
# print(randint(3,100))
# print(randrange(2, 20, 3)) # 2~20 중 3씩 증가하는 숫자중에 랜덤 추출
#
# ex) 33 input, output, 제곱 값 구하기
# a = input("입 력 하 세 요")
# print(a, type(a)) # 숫자를 입력해도 문자로 처리
#
# a = input('입력하세요')
# print(type(a))
# print(int a * int a)
# print(int a ** 2)
#
# a = int(input('입력'))
# print(a, a ** 2) # 10 * 10 = 100
#
# ex) 34 if 제어문
# if 3 > 2 :
#     print(1) # 괄호 사용 가능하지만 없는게 정석, 제어문 끝에 콜론 사용, 조건 실행 출력 문장은 반드시 탭 처리
# else :
#     print(2)
# print(3) # 탭처리 안하면 별도의 문장으로 인식
#
# if 3 > 2 :
#     print(1)
# else :
#     print(2)
#     print(3) # 탭처리 하면 함께 인식
#
# ex) 35 elif, else, 성적 입력 산출 프로그램
# print('점수를 입력하세요')
# a = int(input(''))
# if a >= 90:
#     print('성적 A')
# elif a >= 80:
#     print('성적 B')
# elif a >= 70:
#     print('성적 C')
# elif a >= 60:
#     print('성적 D')
# else:
#     print('성적 F')
#
# ex) 36 랜덤 홀짝 예제
# from random import *
# a = randint(10, 99)
#
# print(a)
# b = a / 10
# c = a % 10
# if b % 2 == 0 and c % 2 == 0:
#     print("탕수육")
# elif b % 2 != 0 and c % 2 == 0:
#     print("짜장면")
# elif b % 2 == 0 and c % 2 != 0:
#     print("냉면")
# else:
#     print("우동")
#
# ex) 37 if, else, split 응용
# if not(''):  # if문 false판단 : False, {}, [], (), None(널과 같음), ''
#     print('호랑이')
# else:
#     print('코끼리')
#
# if 19 in[10, 20, 30, 40]:
#     print('있음')
# else:
#     print('없음')
#
# s = '무궁화 꽃이 피었습니다'
# t = s.split()
# print(t)
# if '무궁화' in t:  # t 자체가 배열이므로 대괄호 X
#     print('있음')
# else:
#     print('없음')
#
# ex) 38 while
# a = 0
# while a > 10:
#       a += 1
# print(a)
# print('호랑이')
#
# a = 0
# while a < 10:
#     a += 1
#     if(a == 3):
#         continue
#     if(a == 6):
#         break
#     print(a)
# print('호랑이')
#
# a = 23
# while(True):
#     if (a % 2 == 1):
#         a = (a * 3) + 1
#     else:
#         a = a / 2
#     if (a == 1):
#         break
#     print(a)
# print(a)
#
# ex) 39 삼항연산
# num = 23
# num // 2 if (num % 2 == 0) else (num * 3 + 1)
# print(num)
#
# ex) 40 range 함수, 클래스 타입, 단독사용 불가
# a = list(range(0, 10)) # 리스트(배열)화 / 0 <= x < 10
# print(a)
# print(list(range(5, 10))) # 바로 출력 가능
# print(list(range(3, 20, 2))) # 2씩 증가, 인수 3개 가능, 오버라이딩
#
# ex) 41 for 제어문
# for i in [0, 1, 2, 3, 4]: # 루팡 반복 출력
#     print(i)
# print() # 줄바꿔줘서 구분
# for i in [0, 1, 2, 3, 4]: # 루팡 반복 출력
#     print(i, end=' ') # 한줄 출력으로 가독성
# for i in ['월', '화', '수', '목', '금']: # 문자열 관리
#     print(i)
# for i in range(0, 10): # 기본 반복문, 꼭 기억!
#     print(i, end=' ')
# for x in range(2, 10):   # 구구단 출력, 다시 해봐야함
#     print('[' + str(x) + '단]')
#     for y in range(1, 10):
#         print(x, 'X', y, '=', x * y)
#
# for i in range(1, 10):  # 1~10 더하기
# a = 0     # 해봐야함
# for 10 in range(1, 10+1):
#     a += b
# print(b)
#
# for i in range(0, 3):   # 중첩 for문
#     for j in range(0, 4):
#         print(i, '+', j)
#
# ex) 42 중첩 for문으로 격자 만들기
# i = 0
# for i in range(3): # 0부터 시작하면 생략 가능
#     for j in range(4):
#         print(i, j, end='  ', sep='')
#     print()
#
# ex) 43
# from random import *
# for i in range(3):
#     print()
#     for j in range(4):
#         x = randint(26)
#         print('%s ', 'A'+x)
#
# ex) 44 chr,ord / 아스키코드 출력
# print(65)
# print(chr(65))
# print(ord('B'))
#
# ex) 45 Create / list, 배열타입, 출력결과에 대괄호
# a = [10, 20, 30, 40]
# print(a)
#
# b = ['호랑이', '코끼리', '독수리']
# print(b)
#
# c = [10, '호랑이', 3.14, True]
# print(c) # 자바의 링크드리스트 컨테이너와 다르게 여러타입의 데이터를 멤버로 설정 가능
#
# ex) 46 Reading /
# a = [10, 20, 30, 40]
# print(a[0], a[1], a[3])
# print(a[4]) # list index out of range 에러, 데이터 범위를 벗어남
#
# for i in a:
#     print(i, end=' ')
# print()
# for value in a:
#     print(value, end=' ') # 변수i 를 value, item, data 라고도 함
#
# ex) 47 Update / 단순 데이터 삽입이 아닌 기존데이터 삭제하고 새로운 데이터 갱신
# a = [10, 20, 30, 40]
# a[0] = 50
# print(a)
# print(id(a[0]), id(a[1]))
# a[0] = 60
# print(id(a[0]), id(a[1]))
#
# ex) 48 Delete /
# a = [10, 20, 30, 40]
# del(a[0])
# print(a)
# print(len(a))
#
# ex) 49 리스트 중첩
# a = [10, '호랑이', [20, '코끼리']]
# print(a[2][0])
#
# a = 'Apple'
# b = ['A','p','p','l','e']
# # print(a['A']) # 문자열 직접 갱신 불가
# b[1] = 'b'
# print(b)
#
# ex) 50 데이터 인덱스 치환, 삭제
# a = ['a', 'b', 'c', 'd', 'e']
# print(a[1:3]) # 인덱스 1번부터 3-1개를 출력
# a[1:3]=['F', 'G'] # 데이터 치환
# a[1:3]=['H', 'I', 'J', 'K', 'L'] # 기존 내용 우선 삭제후 원하는 데이터 수만큼 대입 가능
# print(a)
#
# a = ['a', 'b', 'c', 'd', 'e']
# a[1:3]=[] # 특정 부분만 삭제하고 추가된 값 없음
# print(a)
#
# ex) 51 append, 맨 끝 데이터 붙이기, 데이터 추가시 주로 사용
# a = ['o', 'r', 'a', 'n', 'g', 'e']
# a.append('f') # 리스트 내 맨 뒤에 데이터(인덱스) 추가
# a.append(10) # 숫자 등 다른 타입도 추가 가능
# print(a)
#
# ex) 52 insert, 원하는 위치에 데이터 넣기, 굳이 끼워넣기 케이스는 별로 없어서 잘 안씀
# a = ['o', 'r', 'a', 'n', 'g', 'e']
# a.insert(0, 10) # 원하는 위치에 데이터 삽입
# print(a)
#
# ex) 53 pop, 맨 뒤 데이터 삭제
# a = ['o', 'r', 'a', 'n', 'g', 'e']
# a.pop(3) # 원하는 인덱스 삭제도 가능
# print(a)
#
# ex) 54 remove, 해당 문자열 검색해서 삭제하며 여러개면 맨앞에 하나만
# a = ['o', 'r', 'a', 'n', 'r', 'e']
# a.remove('f')
# print(a)
#
# ex) 55 except, 예외 처리
# a = ['o', 'r', 'a', 'n', 'r', 'e']
# try:     # 데이터 없을 경우 익셉션(예외) 처리 -> 오류를 삭제하는 것
#     a.remove('f')
# except:
#     print('예외가 발생하였습니다.')
#     pass
# print('호랑이')
#
# ex) 56 index, 위치 확인
# a = ['o', 'r', 'a', 'n', 'g', 'e']
# b = a.index('b')
# print(b)
#
# ex) 57 sort / 알파벳 순 순차
# a = ['a', 'c', 'e', 'f', 'd', 'b']
# a.sort() # 메모리 많이 할당, 작업 시간도 걸림 = 비용 많이 듬 / 메모리 or 속도 -> 메모리를 선택하는 편
# print(a)
#
# ex) 58 reverse, 스왑, 역순정렬 아님
# a = ['a', 'c', 'e', 'f', 'd', 'b']
# a.reverse()
# print(a)
#
# a = ['a', 'c', 'e', 'f', 'd', 'b']
# a.sort(reverse=True)  # 역순 정렬
# print(a)
#
# ex) 59 extend
# a = [1, 2, 3]
# a.append(4)
# print(a)
#
# a = [1, 2, 3]
# a.append([4,5]) # 리스트를 1개 추가
# print(a)
#
# a = [1, 2, 3]
# a.extend([4,5,6]) # 리스트 3개를 추가, 기존 배열과 합성
# print(a)
#
# a = [1, 2, 3]
# a = a + [4,5,6] # extend와 동일, 연산자로도 가능
# print(a)
#
# ex) 60 tuple / U,D 불가 / 수정하지 않을 데이터
# a = 10, # 콤마가 붙어야 튜플 형태, 괄호 생략가능
# print(a, type(a))
# b = (10, ) # 괄호 생략 가능하지만 튜플 타입 가독성을 위해 입력
# print(type(b))
#
# c = 10
# d = (10)
# print(type(c), type(d))
#
# a = (10, 20, 30) # 튜플 언패킹 / 튜플로 변수와 값을 한번에 여러개 할당 가능, 리스트도 가능
# b, c, d = a
# print(a, b, c, d)
#
# a = 10  # 데이터 치환
# b = 20
# a, b = b, a
# print(a)
# print(b)
#
# a = [10, 20, 30]
# b = tuple(a) # 리스트 -> 튜플로 변환 함수, 특정 데이터를 묶고 싶을때
# print(type(a)) # 타입은 아직 그대로 리스트
# print(type(b)) # 튜플화 확인
#
# a = (10,) + (20, 30) # 튜플 병합
# print(a)
#
# a = (1, 2, 3, 4, 5)
# b = (1, 2, 3)
# print(a == b)
# print(a > b) # 개수 비교
#
# a = (10, 20, 30) # 데이터 갱신 불가
# b = [10, 20, 30] # 데이터 갱신 가능
# print(a[1]) # 튜플의 개별 값을 추출할때 리스트 사용
#
# a = [10, '호랑이', [20, 30], (40, '코끼리', [50, 60], [70, 80])] # 튜플과 리스트 중첩 사용 가능
# print(a)
#
# a = []
# b = list() # 리스트 함수를 콜한것이다.
# c = ()
# d = tuple()
# e = ['Apple']
# f = list('Apple')
# print(type(a), type(b), type(c), type(d), e, f)
#
# a = []
# b = tuple(a)
# c = list(b)
# print(type(a), type(b), type(c))
#
# ex) 61 split, 문자를 분할하여 저장, 저장 시 리스트로 저장
# a = '호 랑 이'
# b = a.split(' ')
# print(b)
#
# ex) 62 off set? 기준점으로부터 상대적으로 떨어진 거리, 배열 인덱스!
# a = [10, 20, 30]
# print(a[-3]) # 음수 인덱스는 끝 부터 배열 시작, 테크니컬
#
# ex) 63 dictionary, 구조: a = {k(키,고유값):v(밸류),k:v,k:v, ...}, 키를 기준으로 값을 추출하기 때문에 인덱스가 없음
# a = {}
# print(type(a))
#
# a = {1:10, 2:20, 5:40}
# print(a)
#
# a = {10:'호랑이', 20:'코끼리', 30:'독수리'}
# print(a)
#
# a = {1:10, 2:20, 2:30, 5:40} # 키가 중복되면 가장 최근 입력값으로 갱신
# print(a)
#
# a = {1:[10,20], 2:[30,40], 3:[50,60]} # 리스트 삽입 가능
# print(a)
#
# a = {1:(10,20), 2:(30,40), 3:[50,60]} # 튜플 삽입 가능
# print(a)
#
# a = {1:(10,20), 2:('어흥'), 3:[50,60], 4:(80,90), 5:{10:50}}
# print(a)
#
# a = {'호랑이':10, '코끼리':20, '독수리':30}
# print(a)
#
# a = {10:'호랑이', '코끼리':20} # 키 값을 문자와 숫자 복합사용 가능하나 보통 일관되게 사용
# print(a)
#
# a = {'name':'홍길동', 'age':20, 'salary':300} # JSON 문법과 구조가 같음
# print(a['name'])
# a['height'] = 180 # a 변수에 height 키를 넣고 그 값에 180을 주겠다
# print(a)
#
# ex) 64 CRUD
# a = {'name':'이순신', 'age':50} # Create
# b = a['name', 'age']
#
# print(b) # Reading
#
# a['name'] = '독수리' # Update
# a['age'] = 100
# print(a)
#
# del(a['name']) # Delete
# print(a)
# del a['name'] # 위와 결과는 같지만 예약어 사용과 함수 사용
# print(a)
#
# ex) 65 데이터 추출
# a = {'name': '홍길동', 'age': 20, 'salary': 300}
# b = a['name']
# print(b)
# c = a.get('name') # 위와 동일
# print(c)
# print(a.keys()) # 사용중인 모든 키 보여줌
# c = range(0, 10)
# print(c.get('name'))
#
# for item in a.keys(): # a 변수 튜플에서 키값만 추출
#     print(item)
#
# for item in a.items():
#     print(item[0], item[1]) # 리스트로 개별 데이터 추출
#
# for value in a.values(): # 값만 추출
#     print(value)
#
# ex) 66 copy: 객체a, 변수a, b 데이터 공유 / deep copy: 객체 -> a, b 변수 -> a, b 별도의 데이터
# a = [1, 2, 3]
# b = a   # 얕은 복사
# a[0] = 4
# b[0] = 2
# print(id(a)) # 동일 id
# print(id(b))
# a.append(99)
# print(a)
# print(b)
#
# a = [1, 2, 3]
# b = a[:]   # 깊은 복사
# a[0] = 4
# b[0] = 2
# print(id(a))
# print(id(b))
# a.append(99)
# print(a)
# print(b)
#
# a = {1:100, 2:200, 3:300}
# b = a
# a[4] = 400
# print(b)
#
# a = {1:100, 2:200, 3:300}
# b = a.copy()
#
# print(id(a)) # 깊
# print(id(b))
#
# print(id(a[1])) # 얕
# print(id(b[1]))
#
# import copy
# a = {1:100, 2:200, 3:300}
# b = copy.deepcopy(a)
# print(id(a))
# print(id(b))
#
# print('-'*30)
#
# a = {1:100, 2:200, 3:300}
# b = copy.copy(a)
# print(id(a))
# print(id(b))
#
# ex) 67 함수
# def func01(): # 1. 함수 선언, 특정 코드를 백업해놓은거, 아래서 호출
#     print(1)
#     print(2)
#     print(3)
#     print(4)
#
# print(99)
# func01()
# print(100)
#
# def func02(a): # 2. 함수에 인수를 전달하는 경우
#     print(a)
#     print(a*a)
#
# func02(10)
#
# def func03(): # 3. 리턴이 있는 경우
#     print('03 call')
#     return 100
#
# a = func03()
# print(a)    # 리턴 값을 변수로 받아줌
#
# print(func03()) # 바로 직접 출력
#
# print(func03()*7) # 리턴 값 직접 사용의 예
#
# print(func01()) # 주의! 리턴 값이 없으니 사용 불가
#
# 1 전달인수 없고 리턴 없다
# def func01():
#     print('func01 call')
#     print(10)
#     print(20)
#     print(30)
# func01()
#
#
# #2 전달인수 있고 리턴 없다
# def func02(a):
#     print('func02 call')
#     print(a)
#     print(a*a)
# func02(25)
#
#
# #3 전달인수 없고 리턴 있다
# def func03():
#     print('func03 call')
#     print(100)
#     return 200
# a = func03()
# print(a)
#
# #4 전달인수 있고 리턴 있다
# def func04(b):
#     print('func04 call')
#     print(b)
#     print(b*b)
#     return 1000
# b = func04(50)
# print(b)
#
# ex) 68 함수 인수전달 1개 이상
# def func05(a,b,c):
#     print('05 call')
#     sum = a * b + c
#     print(sum)
#     print(a * a + b * b + c * c)
#
# func05(2,3,4)
#
# def func06():
#     print('06 call')
#     return;  # 언리치드 코드, 리턴 값에서 올스탑
#     print(2)
#
# func06()
#
# def func07(a,b):
#     print('07 call')
#     print(a, b)
#     print(type(a), type(b))
#
# func07(10, '호랑이')
#
# def func08(a, b, c = 10, d = 20):  # 함수 인수 초기값 지정 가능
#     print('08 call')
#     print(a,b,c,d)
#
# func08(1, 2)
# func08(1, 2, 3, 4)  # 인수 초기화 가능, 순차적 초기화
# func08(1)  # 인수 1개 호출은 불가
#
#
# def func09(*args):  # 가변인수전달(<->고정인수전달), 함수 인수 전달에 제한없음
#     print('09 call')
#     for data in args:
#         print('호랑이')
#
#
# func09()
# func09(10, 2)
# func09(1, '호랑이')
#
#
# def func10(a, b, *args):
#     print('10 call')
#     print(a, b)
#     for data in args:
#         print(data)
#
#
# func10(10, 20, 30, 40, 50)
#
#
# def func11(a, b, *, color, data): # bare문법 / * 뒤쪽 변수는 마지막 함수에서 반드시 변수 명시
#     print('11 call')
#     print(a, b, color, data)
#
#
# func11(1, 2, color = 3, data = 4) # 가독성 최우선, 코드분석을 용이하게
#
#
# def func12(**star): # **로 딕셔너리 타입으로 출력
#     print('12 call')
#     print(star)
#     for value in star.values():
#         print(value)
#
# func12(a= 10, b = 20)
#
# def func13(**star): # **로 딕셔너리 타입으로 출력
#     print('13 call')
#     print(star)
#     for k, v in star.items():
#         print(k, v)
#
# func13(a= 10, b= 20)
#
# ex) 68 class
# class Apple:  # 생성자 함수 기본형태
#     def __init__(self):  # init, 이니셜라이즈, 초기화 / 셀프는 디폴트 값으로 필수
#       print('생성자 call')
#
# a = Apple()  # 생성자 생성
#
#
# ex) 69 class, 함수
# class Apple:
#     def __init__(self):
#         pass
#     def func01(self):
#         print("func01 호출")
#         print(1)
# a = Apple()
# a.func01()
#
# class 04번
# class Apple:
#     def __init__(self):
#         pass
#     def func02(self, a):
#         print("func02 호출")
#         print(a*a)
# a = Apple()
# a.func02(10)
#
#
# class 05번
# class Apple:
#     def __init__(self):
#         pass
#     def func03(self):
#         print("func03 호출")
#         return 100
# a = Apple()
# a.func03()              # 호출방법01 -> return값 없이
# print(a.func03())       # 호출방법02 -> return 값이랑 같이
# result = a.func03()     # 호출방법03 -> return 값이랑 같이
# print(result)
#
#
# class 06번
# class Apple:
#     def __init__(self):
#         pass
#     def func04(self, a):    # self 꼭 넣어줘야 함 (변수입력은 따로 안해줘도 됨)
#         print("func04 호출")
#         return 100+a
# a = Apple()
# a.func04(50)            # 호출방법01 -> return값 없이
# print(a.func04(50))     # 호출방법02 -> return 값이랑 같이
# result = a.func04(50)   # 호출방법03 -> return 값이랑 같이
# print(result)
#
#
# class Apple:
#     def __init__(self):
#         print(id(self))
#         pass
#
#
# a = Apple()
# print(id(a))
#
#
# ex) 69 필드
# Field
# class Apple:
#     num = 10
#
#     def __init__(self):
#         pass
#
# a = Apple()
# print(a.num)
#
# Field 자동 생성
# class Apple:
#
#     def __init__(self, num):
#         self.num = num    # 필드 선언 안해도 필드 자동 생성 : 동적
#
#     def func(self, num):    # 필드 선언을 안했기에 바로 num 을 사용 할 수 없다.
#         print(num)
#
# a = Apple(20)
# print(a.num)
# a.func(30)
# 동적(Dynamic) : 필요할 때 만들어 쓰는 것
# 정적(Static : 처음부터 만들어져 있는 것
#
# class Apple:
#     a1 = 10
#     def __init__(self, a2):
#         self.a2 = a2
#     def f1(self):
#         a3 = 30
#         print(self.a1, self.a2, a3)
# a = Apple(20)
# a.f1()
#
# ex) 70 상속
# class Apple:
#     def __init__(self):
#         pass
#     def func01(self):
#         print(1)
#     def func03(self):
#         print("부모3")
#
# class Orange(Apple):
#     def __init__(self):
#         pass
#     def func02(self):
#         print(self.func01())
#     def func03(self):
#         print("자식3")
#     def func04(self):
#         print(self.func02())
#     def func05(self):
#         super().func03()  # 부모 호출
#
# a = Orange()
# a.func03()
# a.func04()
# a.func05()
#
# print(Orange.mro()) # 해당 클래스의 상속관계, 속성 확인
#
# a1 = Apple() # 상속은 있지만 업캐스팅의 개념이 없음. 변수 타입 자체가 확인이 불가하기때문에
# 
# ex) 71 업캐스팅, for 활용
# class Dog():
#     def __init__(self):
#         pass
#     def cry(self):
#         print("멍멍")
#
# class Cat():
#     def __init__(self):
#         pass
#     def cry(self):
#         print("야옹")
#
# class Tiger():
#     def __init__(self):
#         pass
#     def cry(self):
#         print("어흥")
#
# a1 = Dog()
# a2 = Cat()
# a3 = Tiger()
#
# a1.cry()
# a2.cry()
# a3.cry()
#
# print()
#
# a4 = [Dog(), Cat(), Tiger()]
#
# for animal in(a4):
#     animal.cry()
#
# ex) 72 함수, 대입연산으로 객체와 주고 받기
# class Apple:
#     def func01(self):
#         print(1)
#         pass
#
# def func02(a):
#      print(2)
#      a.func01()
#
#
# func02(Apple())
#
# ex) 73 다형성,
# class Zoo():
#     def __init__(self,animal):
#         self.animal = animal
#
#     def cry(self):
#         self.animal.cry()
#
#
# class Dog():
#     def cry(self):
#         print('멍멍')
#
#
# class Cat():
#     def cry(self):
#         print('야옹')
#
#
# t1 = Zoo(Dog())
# t2 = Zoo(Cat())
#
# t1.cry()
# t2.cry()
#
# ex) 74 exception 예외 처리 // 다시해봐야함
# try:
#     print(0)
#     a = 4//0 # ZeroDivisionError Exception
# except:
#     print('예외가 발생하였습니다.')
# finally:
#     print('finally')
# print(2)
# Exception 내용이 궁금할 때.
# e.printStackTrace();  ==  except Exception as e: print(e)
# try:
#     print(0)
#     a = 4//0 # ZeroDivisionError Exception
# except Exception as e: # Exception 내용이 궁금할때.
#     print(e)
# print(2)
# try:
#     print(0)
#     a = 4//0 # ZeroDivisionError Exception
# except Exception as e: # Exception 내용이 궁금할때.
#     print(e)
# finally:
#     print(9)
# print(2)
# a = [10, 20, 30]
# b = a.index(30)
# print(b)
# try:
#     c = a.index(100)
# except Exception as e:
#     print(e)
#     print('Index를 찾지 못했습니다.')
# print('본 프로그램은 정상 진행')
#
# ex) 75 파일 입출력, hdd에 파일 생성 및 리딩
# file = open('sample.txt', 'w', encoding='utf-8')
# file.write('호랑이')
# file.write('사자')
# file.close()  # 두줄은 한쌍이며 이 사이에 내용 들어감, 생성되면 좌측 라이브러리에 확인
#
# ex) 76
# for i in range(5):
#     print(i)
#
# for i in range(2,7): # 2~7까지 출력
#     print(i)
#
# for i in range(1,10,2): # 스탭 2
#     print(i)
#
# file = open('sample.txt', 'w', encoding='utf-8') # for문 반복 활용 파일 내용 작성 가능
# for i in range(5):
#     file.write('호랑이 ')
# file.close()
#
# file = open('sample.txt', 'w', encoding='utf-8')
# for i in range(5):
#     file.write(str(i)) # 문자열을 숫자열로 변환하여 반복 출력
# file.close()
#
# file = open('sample.txt', 'w', encoding='utf-8')
# for i in range(5):
#     file.write('호랑이'+str(i)+'\n') # 호랑이0~4 출력 하면서 줄바꿈
# file.close()
#
# with open ('sample.txt', 'w', encoding='utf-8') as file:  # with ~ as, close를 생략하는 파일생성 문법
#     for i in range(5):
#         file.write('호랑이'+str(i)+'\n')
#
# ex) 77 파일 리딩
# file = open('sample.txt', 'r', encoding='utf-8') # r 로 리딩 /
# data = file.readline() # 파일 리드라인 함수로 읽을 준비하고 변수줘서 아래 출력
# print(data)
#
# if data:
#     print(10)
#
# data = file.readline()
# print(data)
#
# if data:
#     print(20)
#
# file.close()
#
# file = open('sample1.txt', 'r', encoding='utf-8')
# while True:
#     data = file.readline()
#     print(data)
#     if not data:
#         break
# file.close()
#
# ex) 78 데이터를 리스트로 출력 후 포인 문장으로 분리하고 줄바꿈 제거
# file = open('sample1.txt', 'r', encoding='utf-8')
# data = file.readlines()
# print(data)
# file.close()
#
# for i in data:
#     print(i, end='')
#
# a = ['호랑이1\n', '호랑이2\n', '호랑이3\n', '호랑이4\n', '\n']
# a[0] = a[0].replace('\n','') # 리스트 0번의 줄바꿈을 삭제
# for i in a:
#     print(i)
#
# for i in range(0, len(a)):
#     a[i] = a[i].replace('\n','')
# print(a)
#
# a = ['호랑이1\n', '호랑이2\n', '호랑이3\n', '호랑이4\n', '\n']
# print(a)
# a[0] = a[0].replace('\n','')
# for i in a:
#     print(i)
#
# for index, value in enumerate(a): # 데이터 뽑고 인덱스 갯수 출력
#     print(index, value)
#
# a[0] = value.replace('\n','')
# print(a)
#
# file = open('sample1.txt', 'r', encoding='utf-8')
# data = file.read()
# file.close()
# print(data)
#
# ex) 79 import, 파일 땡겨오기
# import Tiger #방법1. 해당 함수를 임포트
# Tiger.f1()
#
# from Tiger import * #방법2. 파일명으로 임포트
# Tiger.f1()
#
# import Tiger as t # 방법3. 별칭으로 임포트
# t.f1()
#
# import A as B # A를 B라고 사용하겠다. A의 파일명이나 소스가 길면 B로 간략히
#
# ex) 80 main 확인
# print(__name__) # 알트 + 시프트 + f10 메인 변경
#
# import Tiger as t
# t.f2() # Tiger를 메인으로 설정하면 타이거의 함수를 임포트 해도 파일명으로 출력
#
# if __name__ == '__main__':
#     print(1)
#
# import Tiger as t
# if __name__ == '__main__':
#     print('f1')
#
# t.f2()  # 메인
#
#
# def main():
#     print(1)
#
# if __name__ == '__main__':
#     main()
#
# ex) 81 딕셔너리, 제이슨 형식 잊지말기
# apple = {'n1':'호랑이', 'n2':'코끼리', 'n3':'독수리'}
# print(apple['n2'])
#
# orange = {10:20, 20:'독수리', 30:True}
# print(orange[10], orange[20], orange[30])
#
# kiwi = {
#     '이름':'홍길동',
#     '나이':20,
#     '특기':['독서', '무술', '프로그래밍'],
#     '가족':{'아버지':'아빠', '어머니':'엄마'}
# }
# print(kiwi['이름'], kiwi['나이'])
# print(kiwi['특기'], kiwi['특기'][0]) # 리스트 중복
# print(kiwi['가족'], ['어머니'])
#
# data = {
#     "response":
#         {"body":
#              {"items":
#                   [{"addr":1234,"name":"홍길동"},"득템"]},
#          "page":100},
#     "header":{"result":200,"msg":"OK"}}
#
# print(data["response"])
# print(data["response"], data["header"])
# print(data["response"], ["body"])
# print(data["response"], ["body"], ["items"])
#
# apple = {'n1':'호랑이', 'n2':'코끼리', 'n3':'독수리'}
# print(apple['n1'])
# print(apple.get('n1'))
# try:
#     apple['n4'] # 익셉션 발생
# finally:
#     pass
#     print('n3')
#
# num = apple.get('n4') # 익셉션 노 발생
# print(num)
# if None == num:
#     print(nnnnnn)
#
# ex) 82 sum
# a = [10, 20, 30, 40]
# print(sum(a))   # a의 인수 합
# # print(sum(a[1]))
# a = sum([3,4,5,6])
#
# ex) 83
# def f1(a):
#     return a > 0
# print(filter(f1, [-2,-1,0,1,2]))
# print(list(filter(f1, (-2,-1,0,1,2))))
#
# def f1():
#     print(1)
# f1()
# a = f1 # 함수1번을 a로 참조
# a() # a가 함수1을 참조하면서 호출하여 f1() 과 동일
#
# def f2():
#     print(2)
# f2()
#
# def f3(tt):
#     tt()
#     print(3)
# f3(f2)
#
# def f4():
#     return 999
#
# def f5(tt):
#     print(tt)
# f5(999)  # 단순히 함수5번을 콜하면서 tt인수에 999를 받아서 출력
# f5(f4()) # 함수5번을 콜했지만 인수가 함수4번을 호출하면서 함수 4번의 리턴값인 999를 출력
#
# ex) 84 파이썬에 없는 switch의 대안
# def f1(num):
#     t = {10:'호랑이', 20:'독수리', 30:'앵무새'}
#     return t[num]
# print(f1(10))
#
# a = [10, 20, 30]
# print(a*2) # 리스트를 두번 출력, 한묶음
#
# ex) 85 컴프리헨션, 반복문과 조건문을 이용한 list를 생성하는것
# a = [i for i in range(5)]
# print(a)
#
# a = [i*3 for i in range(5)] # for문의 실행문장을 for문 앞으로 빼는것
# print(a)
#
# a = [10, 20, 30, 40]
# b = [i*5 for i in a] # a의 리스트 들에 5씩 곱해서 출력
# print(b)
#
# a = [10, 20, 30, 40]
# b = [i + 2 for i in a if i > 25]
# print(b)
#
# print(dir({})) # 딕셔너리 관련 함수 목록을 보여줌
# print(dir([])) # 리스트 관련 함수 목록을 보여줌
# print(dir(())) # 튜플 관련 함수 목록을 보여줌
#
# ex) 86 복습
# a = [10, 20, 30, 40]
# a.insert(3, 99)  # 리스트 지정위치에 데이터 삽입
# print(a)
#
# a = [10, 20, 30, 40]
# a.append('호랑이')
# a.append(100) # 리스트 맨뒤에 데이터 삽입
# print(a)
#
# a = [10, 20, 30, 40]
# a.insert(len(a), 99) # 어펜드와 동일하지만 맨끝에 넣고싶을떄
# print(a)
#
# a = [10, 20, 30, 40]
# a += [50, 60]   # 위와 동일
# print(a)
#
# a = [10, 20, 30, 40]
# a.extend([50, 60])   # 위와 동일
# print(a)
#
# a = [10, 20, 30, 40]
# b = a  # 동일 객체 참조
# c = a.copy()  # 새로운 객체를 복사
# print(a, b, c) # 결과는 동일
# print(id(a), id(b), id(c))
#
# a[0] = 99
# print(a[0], b[0], c[0]) # 위 결과 재 확인
#
# a = [10, 20, 30, 40]
# a.clear() # 리스트 삭제 청소, 종종 쓰임
# print(a)
#
# a = [10, 20, 30, 40, 10]
# a.remove(10) # 만약 검색 실패시 인셉션 발생하고 중복된 데이터는 첫 데이터만 제거
# print(a)
#
# a = [10, 20, 30, 40]
# print(a[2])
# del(a[2]) # 지정 인덱스 삭제
# print(a)
#
# a = [10, 20, 30, 40]
# b = a.pop(2) # 지정 인덱스 추출해서 삭제
# print(b)
# print(a)
#
# 뭐만 뽑겟다, 뭐만 빼고 뭘 뽑겟다 등 조건은 필터다
# a에서 6을 제외하고 출력
# def f1(b):
#     return b != 6
#
# a = [0, 3, 6, 9, 0, 3, 6, 9]
# print(list(filter(f1, a)))
#
# ex) 87 내장 함수
# a = 10
# print(id(a)) # 고유값 확인
# print(type(a)) # 데이터 타입 확인
# print(abs(-10)) # 절대값 구하기
#
# a = [10, 20, 30]
# for i in a:
#     print(i)
#
# for index,value in enumerate(a): # enumulate, 리스트의 인덱스와 키 값을 얻고 싶을때, key를 index로 쓸수도 있음
#     print(index, value)
#
# a = 'print(10+20)'
# eval(a) # 문자열도 코드로 해석, 데이터 주고받기 할때 문자열로 전송해야하고 수신자는 코드로 컴파일해서 다시 보내야하기때문
#
# print(min([3, 5, 7]))
# print(max([3, 4, 5, 6])) # 최소값, 최대값을 리스트로 바로 출력걸어서 구하기
#
# a = [1, 2, 3, 4]
# print(max(a)) # 최소값, 최대값을 인수로 줘서 구하기
#
# print(bin(200)) # 바이너리, 입력 숫자의 2진수 출력, 컴퓨터의 언어
# print(oct(200)) # 입력 숫자의 8진수 출력, 0o-로 출력됨, 거의 안씀
# print(hex(200)) # 입력 숫자의 16진수 출력, 컴퓨터의 2진법을 사람이 읽을수있도록 4자리씩 끊어서 해독 / 10진법(사람)과 2진법(컴퓨터)의 절충 해독법
# 
# a = int('123') # 문자열을 숫자로 변환
# print(type(a))
#
# a = str(123) # 숫자열을 문자로 변환
# print(type(a))
#
# a = list('apple') # 문자열을 리스트 타입으로 변환하여 출력
# print(type(a))
# print(a)
#
# a = list(range(5)) # 리스트 내용을 범위로 보고 순차 출력
# print(a)
#
# a = divmod(7, 3) # 나누기해서 구해지는 몫과 나머지 출력
# print(a, type(a)) #  튜플로 출력, 데이터 삭제 불가
# print(a[0], a[1]) # 몫과 나머지 리스트로 별도 확인
#
# print(True and True) # and, 모두가 참이어야 참
# print(all([True, True, True])) # all, 위와 동일한 문장, 리스트를 사용해야함
# print(False or False or True) # or, 트루가 하나라도 있으면 트루
# print(any([False, False, True])) # any, 위와 동일
#
# a = [9, 6, 3, 7, 2]
# a.sort() # 내부 값 갱신, 정렬
# print(a)
#
# b = a
# b.sorted()
# print(b)
#
# import time  # 시간,요일,날짜 정보
# a = time.localtime(time.time())
# b = ['월', '화', '수', '목', '금', '토', '일']
# print(a)
# print(a.tm_year,'년 ', a.tm_mon,'월 ', a.tm_mday,'일 ', sep='')
# print(b[a.tm_wday],'요일 ', sep='')
# print(a.tm_hour,'시 ', a.tm_min,'분 ', a.tm_sec,'초 ', sep='')
#
# import datetime # 위 정보 간략히 한줄 출력
# print(datetime.datetime.now())
#
# for i in range(5):
#     print(i)
#     time.sleep(1) # 1초씩 지연하며 반복 출력
#
#
# ex) 88 lambda
# def f1():
#     print(1)
# f1()
#
# def f1():
#     print(10)
#
# f2 = lambda: print(2)
# f2()
# print(type(f2))
#
# f2 = lambda: print(2)
# f2
#
#
# f3 = lambda x: print(x*x)
# f3(9)
#
#
# f4 = lambda x, y: print(x+y)
# f4(10,20)
#
#
# f5 = lambda: 99
# print(f5())
#
#
# f6 = lambda x, y: x+y
# print(f6(3,4))
#
#
def f1(ff):
    ff()

def f2():
    print('호랑이')
f1(f2)


f1(lambda : print('코끼리'))
def f3(ff):
    ff(10,20)
f3(lambda x,y : print(x+y))


def f4(a):
    return a > 0
a = filter(f4, [-2,-1,0,1,2])
print(list(a))

def f4(a):
    return a > 0
lambda a: filter([-2,-1,0,1,2])
print(list(a))



















