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
from collections import Counter
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.upper().split())

for word, count in words_and_counts.most_common():
    if count > 2:
        print(word, count)

a = 'Tiger Lion Rabit'
b = a.lower().split()
print(b)


a = '무궁화 꽃이'
b = '무궁화\t꽃이'  # 탭
print(a)
print(b)

a = [0,1,2,3,4,5,6]
print(a[::2])

x,y = [1,2]
print(x,y)

_,y = [1,2]
print(y)

a = [3 for _ in range(5)] # i를 제거해서 무시하고 특정 데이터를 반복해서 출력
print(a)

def f1():
    return 1+2, 1-2, 1*2
a = f1()
print(a)

a = {10, 20, 30} # set 타입, 딕셔너리인데 키 값이 없으면 셋 타입으로 인식
print(type(a))

a.add(40) # 셋 타입 데이터 추가
print(a)

a.add(30) # set타입은 중복된 데이터는 추가하지 않음
print(a)

assert 1 + 1 == 2
print()

def f1(a):
    return min(a)

assert f1([1,2,3,4]) == 5
print(a)








