# 타이타닉
# 해봐야함!!!

import sklearn
sklearn.__version__

from sklearn.datasets import load_iris  #아이리스 내장 데이터 불러오기
iris_dataset = load_iris()  # 로드아이리스 함수로 아이리스데이타셋에 딕셔너리 형식 데이터 담음
# print("Iris_dataset key: {}".format(iris_dataset.keys()))  #데이타셋의 키만 출력해서 보기
#해당 키 값들 -> ['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename']

from sklearn.cluster import KMeans
k_means = KMeans(n_clusters=3)

k_means.fit(train_input)

k_means.labels_