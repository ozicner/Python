# import pandas as pd
# from matplotlib import pyplot as plt
# import numpy as np
# # 파일명의 년도를 list 로 생성
# years = range(1880, 2011)
#
# pieces = []
# columns = ['name', 'sex', 'births']
#
# # years 로 년도별 yob____.txt 파일을 읽어옴
# # 파일 내용은 name, sex, births 열 이고,
# # year 열을 새로 추가해서 DataFrame 을 생성함, 년도 별 DataFrame이 생성됨
# # 그 DataFrame 들을 pieces list에 추가함
# for year in years:
#     path = 'myTXT/babynames/yob%d.txt' % year
#     frame = pd.read_csv(path, names=columns)
#
#     frame['year'] = year
#     pieces.append(frame)
#
# # pieces 리스트에 있는 DataFrame 들을 하나로 합침
# names = pd.concat(pieces, ignore_index=True)
# # print(names)
#
# # 태어난 여성과 남성의 수 (births) 를 각 년도 별로 sum 을 구함
# total_births = names.pivot_table('births', index='year',
#                                  columns='sex', aggfunc=sum)
# # print(total_births.tail())
# #
# # total_births.plot(title='Total births by sex and year')
# # plt.show()
#
#
# # 각 이름이 전체 출생수에서 차지하는 비율을 계산
# def add_prop(group):
#     group['prop'] = group.births / group.births.sum()
#     return group
#
#
# names = names.groupby(['year', 'sex']).apply(add_prop)
#
# # 각 이름별 비율을 전부 합해서 1이 되는지 확인하는 print 문
# # print(names.groupby(['year', 'sex']).prop.sum())
#
#
# # 각 연도별/성별에 따른 선호하는 이름 1000개 추출
# def get_top1000(group):
#     return group.sort_values(by='births', ascending=False)[:1000]
#
#
# grouped = names.groupby(['year', 'sex'])
# top1000 = grouped.apply(get_top1000)
# # Drop the group index, not needed
# top1000.reset_index(inplace=True, drop=True)
#
#
# boys = top1000[top1000.sex == 'M']
# girls = top1000[top1000.sex == 'F']
#
# total_births = top1000.pivot_table('births', index='year',
#                                    columns='name',
#                                    aggfunc=sum)

# print(total_births.info())
# subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
# subset.plot(subplots=True, figsize=(12, 10), grid=False,
#             title="Number of births per year")
# plt.show()

# table = top1000.pivot_table('prop', index='year',
#                             columns='sex', aggfunc=sum)
# table.plot(title='Sum of table1000.prop by year and sex',
#            yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))
# plt.show()
#
# df = boys[boys.year == 2010]
# print(df)

# prop_cumsum = df.sort_values(by='prop', ascending=False).prop.cumsum()
# print(prop_cumsum.values.searchsorted(0.5))

# df = boys[boys.year == 1900]
# in1900 = df.sort_values(by='prop', ascending=False).prop.cumsum()
# print(in1900.values.searchsorted(0.5) + 1)

# def get_quantile_count(group, q=0.5):
#     group = group.sort_values(by='prop', ascending=False)
#     return group.prop.cumsum().values.searchsorted(q) + 1
#
# diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
# diversity = diversity.unstack('sex')
#
# print(diversity.head())
# diversity.plot(title="Number of popular names in top 50%")
# plt.show()
#
# # extract last letter from name column
# get_last_letter = lambda x: x[-1]
# last_letters = names.name.map(get_last_letter)
# last_letters.name = 'last_letter'
#
# table = names.pivot_table('births', index=last_letters,
#                           columns=['sex', 'year'], aggfunc=sum)
#
# subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
# subtable.head()
#
# subtable.sum()
# letter_prop = subtable / subtable.sum()
# letter_prop
#
# import matplotlib.pyplot as plt
#
# fig, axes = plt.subplots(2, 1, figsize=(10, 8))
# letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
# letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female',
#                       legend=False)
#
# plt.subplots_adjust(hspace=0.25)
#
# letter_prop = table / table.sum()
# dny_ts = letter_prop.loc[['d', 'n', 'y'], 'M'].T
# dny_ts.head()
#
# plt.close('all')
#
# fig = plt.figure()
#
# dny_ts.plot()
#
#
#
# class Apple:
#     def f1(self):
#         print(1)
#         return self
#
#     def f2(self, func):
#         print(2)
#         num = func(100)
#         return num * 3
#
# def f3(group):
#      print(group)
#      return group * 2
#
#
# a = Apple()
# b = a.f1().f2(f3)
# print(b)

class Apple:
    def f1(self):
        print(1)
        return self

    def f2(self, func):
        print(2)
        num = func(100)
        return num * 2

def f3(group):
    print(group)
    return group * 2

a = Apple()
a.f2(f3)




#
#
# class Apple:
#     def groupby(self):
#         print(1)
#         return self
#
#     def apply(self, func):
#         print(2)
#         num = func(100)
#         return num * 3
#
# def add_prop(group):
#      print(group)
#      return group * 2
#
#
# names = Apple()
# b = names.groupby().apply(add_prop)
# print(b)











