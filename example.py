# 2 <= n <= 90    # 여름 일수
# 1 <= t <= n-1   # 스타후르츠 재배 소요 일수
# 1 <= c <= 300    # 화분 칸수
# 1 <= p <= 1000   # 단가
#
# n,t,c,p=map(int,input().split())
#
# n = int(input())
# t = int(input())
# c = int(input())
# p = int(input())
#
# print((n-1) // t * c * p)
#
#
#
#
# inputValue = input()
# x = int(inputValue.split(' ')[0])
# y = int(inputValue.split(' ')[1])
#
# for i in range((x - y)+1):
#     if x-y > 0: i = i * -1
#     for num in range(1, 10):
#         print('%2d *%2d = %2d ' % (x + i, num, ((x + i) * num)), end=' ')
#         if num % 3 == 0: print(' ', end='\n')
#     print(' ')



# 로또
import random
print('★ 로또 ★')
for i in range(1, 7):
  num = random.randint(1, 45)
  print('  ',num)