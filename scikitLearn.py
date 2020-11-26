# 붓꽃 종류 분류
# 지도학습
import pandas as pd
import sklearn
sklearn.__version__

from sklearn.datasets import load_iris  #아이리스 내장 데이터 불러오기
iris_dataset = load_iris()  # 로드아이리스 함수로 아이리스데이타셋에 딕셔너리 형식 데이터 담음
# print("Iris_dataset key: {}".format(iris_dataset.keys()))  #데이타셋의 키만 출력해서 보기
#해당 키 값들 -> ['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename']

print(iris_dataset['data'])  #데이터라는 키값의 밸류값을 모두 출력
print("shape of data: {}".format(iris_dataset['data'].shape))
#한개의 데이터별로 4가지의 특징점의 실수값 배열로 150개씩 묶여있음

# print(iris_dataset['target'])  #타겟라는 키값의 밸류값을 모두 출력
# print("shape of target: {}".format(iris_dataset['target'].shape))
# #데이터별 붓꽃의 종류, 정답 레이블, 'setosa'는 0, 'versicolor'는 1, 'virginica'는 2로 벡터 저장

# print(iris_dataset['target_names'])  #타겟라는 키값의 밸류값을 모두 출력
# print("shape of target_names: {}".format(iris_dataset['target_names'].shape))
# #저장된 붓꽃의 문자열 데이터에 의해 정의, 'setosa'는 0, 'versicolor'는 1, 'virginica'는 2로 벡터 저장

# print(iris_dataset['DESCR'])  #디스크라이브 키값의 밸류값 출력
# #전체 붓꽃 데이터에 대해서 특징들에 대해서 각각 최대 최소값, 평균에 대한 전반적 정보를 요약, sepal:꽃받침, petal:꽃잎

# print(iris_dataset['feature_names'])  #피쳐네임즈 키값의 밸류값 출력
# print("shape of feature_names: {}".format(iris_dataset['feature_names']))
# #데이터에 담긴 특징이나 단위를 알려줌

from sklearn.model_selection import train_test_split
#데이터 전처리, 트레인 데이터/ 학습데이터 분리 작업
train_input, test_input, train_label, test_label = train_test_split(iris_dataset['data'],
iris_dataset['target'], test_size = 0.2, random_state=11)
#train_test_split 함수는, 데이터 값과, 정답을 받아들이고
#test_size 인자값으로 테스트 데이터를 전체 데이터의 25%로 설정하여 이 비율로 데이터 분리
#random_state는 데이터를 무작위로 떼어낼때 사용할 랜덤값

from sklearn.tree import DecisionTreeClassifier
dt_clf = DecisionTreeClassifier(random_state=11)
dt_clf.fit(train_input, train_label)
pred = dt_clf.predict(test_input)

from sklearn.metrics import accuracy_score
print('accuracy: {0:.3%}'.format(accuracy_score(test_label, pred)))

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 1)
#사이킷런으로 KNN 분류기 객체 생성
knn.fit(train_input, train_label)
#분류기 객체를 학습시킴, 지도학습
#KNN 객체의 fit 메소드로,준비된 학습 데이터와 그와 매칭된 label을 넣어줌

predict_label = knn.predict(test_input)
# print(predict_label)
#테스트

import numpy as np
new_input = np.array([[6.1, 2.8, 4.7, 1.2]])
result_array = knn.predict(new_input)
#입력한 새로운 붓꽃 정보에 대한 밸류값을 입력하면 결과 분류

# if result_array == [0]:
#     print('* setosa *')
# elif result_array == [1]:
#     print('* nversicolor *')
# else:
#     print('* virginica *')
#기존 정답 레이블로 지정해둔 'setosa'는 0, 'versicolor'는 1, 'virginica'는 2에 따라 분류 결과 출력

###########################################
# 비지도학습

from sklearn.cluster import KMeans
k_means = KMeans(n_clusters=3)

k_means.fit(train_input)

k_means.labels_

# print("0 cluster:", train_label[k_means.labels_==0])
# print("1 cluster:", train_label[k_means.labels_==1])
# print("2 cluster:", train_label[k_means.labels_==2])

import numpy as np
new_input = np.array([[6.1, 2.8, 4.7, 1.2]])

prediction = k_means.predict(new_input)
# print(prediction)

# print('accuracy: {0:.3%}'.format(accuracy_score(test_label, pred)))