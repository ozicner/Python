from sklearn.feature_selection.tests.test_base import feature_names
from sklearn.tree import plot_tree, DecisionTreeClassifier
from matplotlib import pyplot as plt


plt.figure(figsize=(15,15))


def model(args):
    pass


tree = plot_tree(model, feature_names = feature_names, fontsize=10,filled=True)

model = DecisionTreeClassifier(max_depth = 8,random_state=42,)