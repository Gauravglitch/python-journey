from sklearn import tree

# feature consisting of height, weight, shoe_size
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
     [166, 65, 40], [190, 90, 47]]

#labels
y = ['male','male','female','female','female','male']

#initialize the classifier
clf = tree.DecisionTreeClassifier()
#fit the classifier with the features and labels
clf = clf.fit(X, y)
#make a prediction
prediction = clf.predict([[188,74,39]])
print(prediction)