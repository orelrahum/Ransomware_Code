#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import itertools
import numpy as np


# In[2]:


df = pd.read_csv('DATASET.csv')


# In[3]:


X = df[['feature 1 ',' feature 2 ',' feature 3 ',' feature 4']]
y = df[' result']
X_train , X_test , y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)


# ## SVM

# In[4]:


clf = svm.SVC()


# In[5]:


df[' result'].value_counts()


# In[6]:


get_ipython().run_cell_magic('time', '', 'clf.fit(X_train, y_train)')


# In[7]:


get_ipython().run_cell_magic('time', '', 'y_pred = clf.predict(X_test)')


# In[14]:


print(classification_report(y_test, y_pred))


# In[13]:


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


# In[15]:


plot_confusion_matrix(confusion_matrix(y_test, y_pred), classes=['Negative','Positive'], title='Confusion Matrix')


# ## KNN

# In[28]:


knn = KNeighborsClassifier(n_neighbors=3)


# In[29]:


get_ipython().run_cell_magic('time', '', 'knn.fit(X_train, y_train)')


# In[30]:


y_test = knn.predict(X_test)


# In[31]:


print(classification_report(y_test, y_pred))


# In[32]:


plot_confusion_matrix(confusion_matrix(y_test, y_pred), classes=['Negative','Positive'], title='Confusion Matrix')

