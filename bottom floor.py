# 4~5p
# users = [
#     {'id': 0, 'name': '호랑이0'},
#     {'id': 1, 'name': '호랑이1'},
#     {'id': 2, 'name': '호랑이2'},
#     {'id': 3, 'name': '호랑이3'},
#     {'id': 4, 'name': '호랑이4'},
#     {'id': 5, 'name': '호랑이5'},
#     {'id': 6, 'name': '호랑이6'},
#     {'id': 7, 'name': '호랑이7'},
#     {'id': 8, 'name': '호랑이8'},
#     {'id': 9, 'name': '호랑이9'}
# ]
#
# # print(len(users))
#
# friendship_pairs = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4),
#                     (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]
#
# friendships = {user['id']: [] for user in users}
# print(friendships)
#
# for i, j in friendship_pairs:
#     friendships[i].append(j)
#     friendships[j].append(i)
# print(friendship_pairs)
#
# for item in friendship_pairs:
#     print(item)
#
#
# a = (i for i in range(5))
# print(type(a)) # 제너레이터(생성자) 타입
#
# b = sum({4})
# print(b)
#
# #sum(리스트), sum(제너레이트)
#
# 6p
# def number_of_friends(user):
#     'user의 친구는 몇명일까'
#     user_id = user['id']
#     friend_ids = friendships[user_id]
#     return len(friend_ids)
#
# total_connection = sum(number_of_friends(user) for user in users)
# print(total_connection)
#
# num_users = len(users)
# avg_connection = total_connection = total_connection / num_users
# print(avg_connection)
#
#
# num_friends_by_id = [(user['id'], number_of_friends(user))
#                      for user in users]
#
# num_friends_by_id.sort(
#     key= lambda id_and_friends: id_and_friends[1],
#     reverse=True)
# for item in num_friends_by_id:
#     print(item)
#
#
# a = [
#     ('호랑이0', 7, 9),
#     ('호랑이1', 6, 6),
#     ('호랑이2', 4, 3),
#     ('호랑이3', 9, 7)]
#
# a.sort(key=lambda k: k[2])
# print(a)
#
#
# def foaf_ids_bad(user):
#     return [foaf_id
#             for friend_id in friendships[user['id']]
#             for foaf_id in friendships[user[friend_id]]
#             ]
# print(users[0])
# print(friendships[0])
#
# Counter, 리스트 내 단어 카운팅, 딕셔너리로 출력
# from collections import Counter
#
# a = Counter([10, 20, 30])
# print(a)
#
# a = ['호랑이', '호랑이', '코끼리', '호랑이', '코끼리', '독수리', '호랑이']
# b = Counter(a)
# print(b)
#
# c = [10, 20, 30, 10, 20, 10]
# d = Counter(c)
# print(d)
#
#
# def friends_of_friends(user):
#     user_id = user['id']
#     return Counter(foaf_id
#         for friend_id in friendships[user_id]
#         for foaf_id in friendships[friend_id]
#         if foaf_id != user_id
#         and foaf_id not in friendships[user_id])
# print(friends_of_friends(users[3]))
#
#
#
# a = [(i, j)
#      for i in range(3)
#      for j in range(4)]
# print(a)
#
#
# a = [(i, j)
#      for i in [0, 1, 2]
#      for j in [0, 1, 2, 3]]
# print(a)
#
#
# a = [(i, j)
#      for i in [7, 8, 9]
#      for j in [4, 5, 6, 7]]
# print(a)
#
#
# a = [i for i in [0,1,2,3,4,99,100]
#      if i % 2 == 0] # 짝수를 필터링
# print(a)
#
#
# print(15 in [10, 20, 30]) # 값이 리스트에 포함되어있는지 트루 폴스
# print(10 not in [10, 20, 30])
#
#
# data = [
#     (0, '호랑이'), (0, '코끼리'), (0, '독수리'),
#     (1, '호랑이'), (1, '코끼리'),
#     (2, '호랑이'),
#     (3, '코끼리'), (3, '독수리')
# ]
#
# def f1(a):
#     print(a)
#     b = [i for i, j in data
#             if j == a]
#
# print(b)
#
#
#
# def f1(a):
#     print(a)
#     return [i for i, j in data
#             if j == a]
#
# print(f1('코끼리'))
#
#
#
#
# interests = [
#     (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
#     (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
#     (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
#     (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
#     (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
#     (3, "statistics"), (3, "regression"), (3, "probability"),
#     (4, "machine learning"), (4, "regression"), (4, "decision trees"),
#     (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
#     (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
#     (6, "probability"), (6, "mathematics"), (6, "theory"),
#     (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
#     (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
#     (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
#     (9, "Java"), (9, "MapReduce"), (9, "Big Data")
# ]
#
# def data_scientists_who_like(target_interest):
#     """Find the ids of all users who like the target interest."""
#     return [user_id
#             for user_id, user_interest in interests
#             if user_interest == target_interest]
#
# print(data_scientists_who_like('Java'))
#
#
# from collections import defaultdict
# wc = {}
# a = ['사과', '바나나', '바나나', '멜론']
# wc = defaultdict(int) # 키값 콜론 뒤에 데이터가 숫자라서 int
# for i in a:
#     wc[i] += 1
# print(wc) # defaultdict(<class 'int'>, {'사과': 1, '바나나': 2, '멜론': 1}) -> 분류별 갯수
#
#
#
# a = defaultdict(list)
# a['호랑이'].append(10)
# a['호랑이'].append(20)
# a['호랑이'].append(30)
# a['코끼리'].append(10)
# a['코끼리'].append(40)
# print(a['호랑이'])  # [10, 20, 30] -> 키가 호랑이인 밸류값 모두 출력
#
#
# user_ids_by_interest = defaultdict(list)
#
# for user_id, interest in interests:
#     user_ids_by_interest[interest].append(user_id)
#
#
# interests_by_user_id = defaultdict(list)
#
# for user_id, interest in interests:
#     interests_by_user_id[user_id].append(interest)
#
# def most_common_interests_with(user):
#     return Counter(
#         interested_user_id
#         for interest in interests_by_user_id[user["id"]]
#         for interested_user_id in user_ids_by_interest[interest]
#         if interested_user_id != user["id"]
#     )
#
# print(most_common_interests_with(['java']))
#
# from collections import defaultdict
# salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
#                         (48000, 0.7), (76000, 6),
#                         (69000, 6.5), (76000, 7.5),
#                         (60000, 2.5), (83000, 10),
#                         (48000, 1.9), (63000, 4.2)]
# salary_and_tenure = defaultdict(list)
#
# for salary, tenure in salaries_and_tenures:
#     salary_and_tenure[tenure].append(salary)
#
# print(salary_and_tenure)
#
#
#
# from collections import defaultdict
#
# a = defaultdict(list)
#
# a[1].append(10)
# a[2].append(20)
# a[3].append(30)
# a[2].append(40)
# a[3].append(50)
# a[3].append(60)
#
#
# b = {
#     i: sum(j) / len(j)
#     for i in a.items()
# }
#
# print()
#
#
import enum
from collections import defaultdict
# def tenure_bucket(tenure):
#     if tenure < 2:
#         return '2보다 작음'
#     elif tenure < 5:
#         return '2와 5 사이'
#     else:
#         return '5 이상'
#
# tenure_bucket(3)
#
# from collections import Counter
# interests = [
#     (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
#     (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
#     (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
#     (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
#     (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
#     (3, "statistics"), (3, "regression"), (3, "probability"),
#     (4, "machine learning"), (4, "regression"), (4, "decision trees"),
#     (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
#     (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
#     (6, "probability"), (6, "mathematics"), (6, "theory"),
#     (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
#     (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
#     (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
#     (9, "Java"), (9, "MapReduce"), (9, "Big Data")
# ]
#
# words_and_counts = Counter(word
#                            for user, interest in interests
#                            for word in interest.upper().split())
#
# for word, count in words_and_counts.most_common():
#     if count > 2:
#         print(word, count)
#
# a = 'Tiger Lion Rabit'
# b = a.lower().split()
# print(b)
#
#
# a = '무궁화 꽃이'
# b = '무궁화\t꽃이'  # 탭
# print(a)
# print(b)
#
# a = [0,1,2,3,4,5,6]
# print(a[::2])
#
# x,y = [1,2]
# print(x,y)
#
# _,y = [1,2]
# print(y)
#
# a = [3 for _ in range(5)] # i를 제거해서 무시하고 특정 데이터를 반복해서 출력
# print(a)
#
# def f1():
#     return 1+2, 1-2, 1*2
# a = f1()
# print(a)
#
# a = {10, 20, 30} # set 타입, 딕셔너리인데 키 값이 없으면 셋 타입으로 인식
# print(type(a))
#
# a.add(40) # 셋 타입 데이터 추가
# print(a)
#
# a.add(30) # set타입은 중복된 데이터는 추가하지 않음
# print(a)
#
# assert 1 + 1 == 2
# print()
#
# def f1(a):
#     return min(a)
#
# assert f1([1,2,3,4]) == 5
# print(a)
#
#
# 33p ~ 57p
#
# a = 10
#
# a = a if a is not None else 0
#
# print(a)
#
# b = None
#
# b = b if b is not None else 0
#
# print(b)
#
# d1 = {'호랑이0': 5,
#       '호랑이1': 77,
#       '호랑이2': 52
#       }
#
# wc = sorted(d1.items(),
#             key=lambda wc: wc[1],
#             reverse=True)
#
# print(wc)
#
# a = [10 for _ in [1, 1, 1, 1, 1]]
#
# print(a)
#
# a = [(x, y)
#      for x in range(3)
#      for y in range(4)]
#
# print(a)
#
# print('-'*100)
#
# k = 0
# for i in range(3):
#     for j in range(4):
#         print(a[k], end=' ')
#         k += 1
#     print()
#
#
# class Apple:
#
#     def __init__(self,count=0):
#         self.count = count
#
#     def click(self,num_times = 1):
#         self.count += num_times
#
#     def read(self):
#         return self.count
#
#     def reset(self):
#         self.count=0
#
# a1=Apple()
# a2=Apple(100)
#
# a1.click()
# a1.click()
# print(a1.read())
#
# a2.click()
# print(a2.read())
#
# class Banana(Apple):
#
#     def reset(self):
#         pass
#
#
# b1=Banana()
#
# b1.click()
# b1.click()
# b1.click()
#
# print(b1.read())
#
# print('-'*100)
# def f1():
#     yield 10
#     yield 20
#     yield 30
#
# for i in f1():
#     print(i)
#
# def f2(n):
#     i=0
#     while i<n:
#         yield i
#         i+=1
#
#
# for i in f2(10):
#     print(i)
# def f3():
#     n=1
#     while True:
#         yield n
#         n+=1
#
# a=f3()
# for i in a:
#     print(i)
#
# b=[i for i in a if i%2==0 ]
#
# for i in b:
#     print(i)
# a=[10,20,30]
#
# for i,v in enumerate(a):
#     print(i,v)
#
# b={0:10,1:20,2:30}
#
# for i,v in b.items():
#     print(i,v)
# from random import *
#
# print(int(random()*100))
#
# print(randint(10,20))
#
# print(randrange(0,10,3))
#
# seed(10)
# for i in range(5):
#     print(random())
#
#
# a=[1,2,3,4,5]
#
# shuffle(a)
#
#
# print(a)
#
# b=choice(a)
#
# print(b)
#
# a=range(60)
# b=sample(a,3)
#
# print(b)
#
# a=[1,2,3]
# b=[4,5,6]
# c=[i for i in zip(a,b)]
#
# print(c)
#
# d,e=zip(*c)
#
# print(d)
# print(e)
#
# def f1(a: int,b: int) -> int:
#     return a+b
#
# a: list = []
#
#
#
# from typing import List
#
# b: List = []
#
# print(type(a))
# print(type(b))
#
# c: List[int] = []
#
# print(type(c))
#
# print(type(d))
import matplotlib.pyplot as plt
# plt.rc('font',family='Malgun Gothic')
#
# years=[1950,1960,1970,1980,1990,2000,2010]
# gdp=[300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]
#
# plt.plot(years,gdp,color='green',marker='o',linestyle='solid')
# plt.title('Nominal GDP')
#
# plt.ylabel('Billions of $')
# plt.show()
# movies=['Annie Hall','Ben-Hur','Casablanca','Gandhi','West Side Story']
# num_oscars=[5,11,3,8,10]
#
# plt.bar(range(len(movies)),num_oscars)
#
# plt.title('My Favorite Movies')
# plt.ylabel('#of Academy Awards')
#
# plt.xticks(range(len(movies)),movies)
# plt.show()
# from collections import Counter
# grades=[83,95,91,87,70,0,85,82,100,67,73,77,0]
#
# histogram = Counter(min((grade // 10) * 10, 90 ) for grade in grades)
#
#
# plt.bar([x+5 for x in histogram.keys()],
#         histogram.values(),
#         10,
#         edgecolor=(0,0,0))
#
# plt.axis([-5,105,0,5])
#
#
# plt.show()
# variance=[1,2,4,8,16,32,64,128,256]
# bias_squared=[256,128,64,32,16,8,4,2,1]
# total_error=[x+y for x,y in zip(variance,bias_squared)]
# xs=[i for i,_ in enumerate(variance)]
#
# plt.plot(xs, variance, 'g-',label='variance')
# plt.plot(xs, bias_squared, 'r-.',label='bias^2')
# plt.plot(xs, total_error, 'b:',label='total error')
#
# plt.legend(loc=9)
# plt.show()
# friends=[70,65,72,63,71,64,60,64,67]
# minutes=[175,170,205,120,220,130,105,145,190]
# labels=['a','b','c','d','e','f','g','h','i']
# plt.scatter(friends,minutes)
# for label,friend_count,minute_count in zip(labels,friends,minutes):
#     plt.annotate(label,
#                  xy=(friend_count,minute_count),
#                  xytext=(5,5),
#                  textcoords='offset points')
# plt.show()
#
#
# 61p
# def Apple(a,b):
#     c = []
#     c.append(a+b)
#     c.append(b+c)
#     c.append(c+a)
#     return c
# print(Apple([0,1,2], [3,4,5]))
#
#
# def f2(a,b):
#     result = [i+j for i, j in zip(a, b)]
#     return result
# # print(f2([0,1,2], [3,4,5]))
#
#
#
# def f3(a):
#     b = len(a[0])
#     return [sum(vector[i]
#             for vector in a)
#             for i in range(b)]
#
# print(f3([[1,2], [3,4], [5,6], [7,8]]))
# -->
# a = [[1, 2], [3, 4], [5, 6], [7, 8]]
# a[0] = [1, 2]  ->  b = len(a[0]) = 2
# vector = [1,2], [3,4], [5,6], [7,8]
# vector[0] = 1, 3, 5, 7   /   vector[1] = 2, 4, 6, 8
#
#
# 62p
# def f1(c, v):
#     return [c * i for i in v]
# print(f1(2, [1,2,3]))
# print(f1(0.5, [1,2,3]))
#
#
# def f2(v):
#     n = len(v)
#     return f1(1/n, f3(v))
# print(f2([[1,2], [3,4], [5,6]]))
#
#
# def f5(a, b):
#     return sum(a * b for a, b in zip(a,b))
# print(f5([1, 2, 3], [4, 5, 6]))
#
#
# import math
#
# def f6(v):
#     return math.sqrt(f2(v))
# print(f6([3, 4]))
#
#
#
#
# def f7(a,b):
#     c = (a[0]-b[0])**2 + (a[1]-b[1])**2
#     f3(c)
#     return
# print(f7([2,1], [1,2]))
#
#
# def f1(a):
#     r = len(a)
#     c = len(a[0])
#     return r, c
# print(f1([
#     [1,2,3],
#     [4,5,6]]))
#
#
# def f2(a, b):
#     return a[b]
# print(f2([
#     [1,2,3],
#     [4,5,6],
#     [1,2,3],
#     [4,5,6]],
#     0))
#
#
# def f3(a,i):
#     return a[i]
#
# def f4(a,j):
#     return [a[j]
#             for a in a]
#
# print([0,1])
#
#
#
# def f5(r, c, fn):
#     return [[fn(i,j)
#              for j in range(c)]
#             for i in range(r)]
#
# def f6(n):
#     return f5(n, n, lambda i, j: 1 if i == j else 0)
#
# for i in f6(5):
#     print(i)
#
#
#
# a = [[1, 2, 3, 4],
#      [2, 3, 1, 2],
#      [1, 2, 1, 3]]
#
# b = [[2, 1, 3],
#      [1, 2, 2],
#      [2, 3, 1],
#      [3, 4, 1]]
# result = []
#
# # 행렬의 열을 구하는 함수
# def get_column(a, b):
#     return [a_i[b] for a_i in a]
# def mul_matrix(a, b):
#     print(len(a[0]), len(b))
#     assert len(a[0]) == len(b), "행렬 a, b에 대한 곱을 위해서는 a의 열의 개수와 b의 행의 개수가 같아야 합니다."
#     for a_row in a:
#         result_row = []
#         for j in range(len(b[0])):
#             b_col = get_column(b, j)
#             result_row.append(sum(a_row_v * b_col_v
#                                   for a_row_v, b_col_v
#                                   in zip(a_row, b_col)))
#         result.append(result_row)
# mul_matrix(a, b)
# print('============')
# for rows in result:
#     print(rows)
#
#
# 69p
# from collections import Counter
#
# import matplotlib.pyplot as plt
#
# num = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#
# a = Counter(num)
# xs = range(101)
# ys = [a[x] for x in xs]
# plt.bar(xs, ys)
# plt.axis([0, 101, 0, 25])
# plt.xlabel('friends')
# plt.ylabel('people')
# # plt.show()
#
# num1 = len(num) # 데이터의 개수
# print(num1)
#
# large = max(num)
# small = min(num)
# print(large, small)
#
# sort = sorted(num)
# s_v = sort[0] # 제일 작은 값
# s_s_v = sort[1] # 두번째로 작은 값
# s_l_v = sort[-2] # 두번째로 큰 값
# print(s_v, s_s_v, s_l_v)
#
#
#
# def f1(xs):
#     return sum(xs) / len(xs) # 평균 or 중앙값, 중심경향성 파악
# print(f1(num))
#
#
# def _median_odd(xs):
#     return sorted(xs)[len(xs) // 2]
#
# def _median_even(xs):
#     sorted_xs = sorted(xs)
#     mid = len(xs) // 2
#     return (sorted_xs[mid - 1] + sorted_xs[mid]) / 2
#
# def median(v):
#     return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)
#
# print(median([1,10,2,9,5]))
# print(median([1,9,2,10])) # 중앙 값 두개를 더해서 2로 나눈 값을 출력해줌
# print(median(num))
#
#
#
# def f2():
#     return 10
# def f3():
#     return f2()
# def f4():
#     return f3()
# print(f4())  # 함수에서 함수를 계속 콜, 리턴 값 없으면 안나옴
#
#
#
# a = abs(-3)
# print(a)
#
# abs = 10   # 내장 함수나 예약어를 변수로 사용하면 오류 발생 / TypeError: 'int' object is not callable
# a = abs(-3)
# print(a)
#
#
# print(int(0.2 * 267)) # 소수점 절삭
#
# def q(xs, p):
#     p_i = int(p * len(xs))
#     return sorted(xs)[p_i]
#
# print(q(num, 0.10))  # 분위, 중앙값을 포괄, 특정 백분위보다낮은 분위에 속하는 데이터
# print(q(num, 0.90))
#
#
# def mode(x):
#     cs = Counter(x)
#     m_c = max(cs.values())
#     return [x_i for x_i, c in cs.items()
#             if c == m_c]
# print(set(mode(num))) # set, 중복값 제거
#
#
#
# a = [1, 2, 3, 4, 5] # 변위 데이터
# b = sum(a) / len(a) # 평균
#
# c = [i - b for i in a] # 편차, i: 변위 a에서 하나씩 가져온 값을 넣음
# print(c)
#
# d = [abs(j) for j in c] # 편차 절대값들의 합의 평균 -> 평균편차
# print(d)
# print(sum(d))
# print(sum(d) / b)
# print(int(sum(d) / b))
#
# # 편차 제곱합의 평균 -> 분산
# def f2(xs):
#     return max(xs) - min(xs)
#
# print(f2(num))
#
# from scratch.linear_algebra import sum_of_squares
#     x_bar = f1(xs)
#     return [x - x_bar for x in xs]
#
# def variance(xs):
#     n = len(xs)
#     deviations = f2(xs)
#     return sum_of_squares(deviations) / (n - 1)
#
# print(81.54 < variance(num) < 81.55)
#
#
#
# import math
#
# def s_d(xs):
#     return math.sqrt(variance(xs))
# print(9.02 < s_d(num) < 9.04)



# 86p

# class Color(enum.Enum):
#     RED = 0
#     BLUE = 1
#     GREEN = 2
#
# print(random.random(Color))

import random
from enum import Enum

# class Kid(enum.Enum):
#     BOY = 0  # enum 문법, 변수를 숫자로 표현해서 간소화, 편의성
#     GIRL = 1
#
# ct0 = 0
# ct1 = 0
# ct2 = 0
#
# for _ in range(1000):
#     a = random.choice([Kid.BOY, Kid.GIRL])
#     b = random.choice([Kid.BOY, Kid.GIRL])  # a,b 조합, 4가지 경우의 수 제공 // 남/남, 남/여, 여/여, 여/남
#
#     if a == Kid.BOY:                    # 50%, a가 남자인 경우는 둘 중 하나
#         ct0 += 1
#     if a == Kid.BOY and b == Kid.GIRL:  # 25%, a와 b가 남자이거나 여자인 경우 넷 중 하나
#         ct1 += 1
#     if a == Kid.BOY or b == Kid.GIRL:   # 75%, a가 남자인것과 b가 여자인 것 모든 경우
#         ct2 += 1
#
# print(ct0, ct1, ct2)
# print(ct1 / ct0)
# print(ct1 / ct2)  # 조건부 확률 공식
#
#
#
#
#
#
# a = []
# b = random.randint(1, 10)
# for c in range(2):
#     while b in a:
#         b = random.randint(1, 10)
#     a.append(b)
# c = sorted(a)
# count = 0
# count1 = 0
# for i in range(100000):
#     while True:
#         x = []
#         y = random.randint(1, 10)
#         for z in range(2):
#             while y in x:
#                 y = random.randint(1, 10)
#             x.append(y)
#         z = sorted(x)
#         if c == z:
#             break
#         else:
#             count += 1
#     sum = count + count1
#     count1 = sum
#     count = 0
# print(count1 / 100000)
#
#
#
import math
import matplotlib.pyplot as plt

SQRT_TWO_PI = math.sqrt(2 * math.pi)

def f1(x, mu=0, sigma=1):
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs,[f1(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
plt.plot(xs,[f1(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
plt.plot(xs,[f1(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
plt.plot(xs,[f1(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
plt.legend()
plt.title("Various Normal pdfs")
plt.show()






