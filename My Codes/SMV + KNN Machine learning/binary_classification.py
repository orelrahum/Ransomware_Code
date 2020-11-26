#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import itertools
import numpy as np


# In[ ]:


df = pd.read_csv('DATASET.csv')


# In[ ]:


X = df[['feature 1 ',' feature 2 ',' feature 3 ',' feature 4']]
y = df[' result']
X_train , X_test , y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)


# ## SVM

# In[ ]:


clf = svm.SVC()


# In[ ]:


df[' result'].value_counts()


# In[ ]:


clf.fit(X_train, y_train)


# In[ ]:


y_pred = clf.predict(X_test)


# In[ ]:


print(classification_report(y_test, y_pred))


# In[ ]:


def plot_confusion_matrix(cm, classes,
                          normalize=True,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()


# In[ ]:


plot_confusion_matrix(confusion_matrix(y_test, y_pred), classes=['Negative','Positive'], title='Confusion Matrix')


# ## KNN

# In[ ]:


knn = KNeighborsClassifier(n_neighbors=3)


# In[ ]:


knn.fit(X_train, y_train)


# In[ ]:


y_test = knn.predict(X_test)


# In[ ]:


print(classification_report(y_test, y_pred))


# In[ ]:


plot_confusion_matrix(confusion_matrix(y_test, y_pred), classes=['Negative','Positive'], title='Confusion Matrix')

