import pandas as pd

# 출력되는 내용을 10 rows 만 출력
pd.options.display.max_rows = 10

# users.dat , ratings.dat , movies.dat 파일을 읽어서 각 변수에 저장
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('users.dat', sep='::',
                      header=None, names=unames, engine='python')

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat', sep='::',
                        header=None, names=rnames, engine='python')

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movies.dat', sep='::',
                       header=None, names=mnames, engine='python')

# 테이블들 출력
# print(users)
# print(ratings)
# print(movies)

# users 는 유저들의 정보 (user_id, gender, age)
# ratings 는 유저들의 영화별 평점 정보 (user_id, movid_id, rating)
# movies 는 영화 정보 (movie_id, 제목, 장르)

# 3 개의 데이터 병합
data = pd.merge(pd.merge(ratings, users), movies)
# print(data)
# print(data.iloc[0])

# 성별에 따른 각 영화의 평점 구하기, pivot_table 메소드
mean_ratings = data.pivot_table('rating', index='title',
                                columns='gender', aggfunc='mean')
# print(mean_ratings[:5])
#
# # 3개의 데이터를 병합한 data 에서 title 별로 그룹화한 후, 영화 제목별 평점 내린 사람 수를 size() 메소드로 row 수를 셈
# # row 는 한 사람이 한 영화에 대한 내린 평가
ratings_by_title = data.groupby('title').size()
# print(ratings_by_title[:10])
#
# # 평점을 내린 사람 수가 250 이상인 영화 제목들
active_titles = ratings_by_title.index[ratings_by_title >= 250]
print(active_titles)
#
# # active_titles 는 평점을 내린 사람 수가 250 이상인 영화 제목들
# # 그 영화들의 평점 평균을 출력
mean_ratings = mean_ratings.loc[active_titles]
print(mean_ratings)
#
# # 여성에게 높은 평점을 받은 영화 목록 출력, ascending=False 은 내림차순 옵션
top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
# print(top_female_ratings[:10])

# 평점 평균에서 남자의 평점에서 여자의 평점을 빼서 'diff' col 이름으로 mean_ratings 에 추가
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']

# mean_ratings 를 남녀 평점 차이가 심한 순으로 정렬하여 출력
sorted_by_diff = mean_ratings.sort_values(by='diff')
# print(sorted_by_diff[:10])

# 뒤에서 10개의 로우를 출력
# print(sorted_by_diff[::-1][:10])

# 평점의 표준편차가 큰 영화 10개 까지 출력
# Standard deviation of rating grouped by title
rating_std_by_title = data.groupby('title')['rating'].std()
# Filter down to active_titles
rating_std_by_title = rating_std_by_title.loc[active_titles]
# Order Series by value in descending order
# print(rating_std_by_title.sort_values(ascending=False)[:10])
