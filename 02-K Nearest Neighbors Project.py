#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # K Nearest Neighbors Project 
# 
# Welcome to the KNN Project! This will be a simple project very similar to the lecture, except you'll be given another data set. Go ahead and just follow the directions below.
# ## Import Libraries
# **Import pandas,seaborn, and the usual libraries.**

# In[51]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Get the Data
# ** Read the 'KNN_Project_Data csv file into a dataframe **

# In[52]:


df=pd.read_csv("KNN_Project_Data")


# **Check the head of the dataframe.**

# In[53]:


df.head()


# # EDA
# 
# Since this data is artificial, we'll just do a large pairplot with seaborn.
# 
# **Use seaborn on the dataframe to create a pairplot with the hue indicated by the TARGET CLASS column.**

# In[54]:


sns.pairplot(df,hue='TARGET CLASS')


# # Standardize the Variables
# 
# Time to standardize the variables.
# 
# ** Import StandardScaler from Scikit learn.**

# In[55]:


from sklearn.preprocessing import StandardScaler


# ** Create a StandardScaler() object called scaler.**

# In[56]:


scaler=StandardScaler()


# ** Fit scaler to the features.**

# In[57]:


scaler.fit(df.drop('TARGET CLASS',axis=1))


# **Use the .transform() method to transform the features to a scaled version.**

# In[58]:


scaled_features = scaler.transform(df.drop('TARGET CLASS',axis=1))


# **Convert the scaled features to a dataframe and check the head of this dataframe to make sure the scaling worked.**

# In[59]:


df_feat=pd.DataFrame(scaled_features,columns=df.columns[:-1])
df_feat.head()


# # Train Test Split
# 
# **Use train_test_split to split your data into a training set and a testing set.**

# In[60]:


from sklearn.model_selection import train_test_split


# In[61]:


X_train,X_test,y_train,y_test=train_test_split(scaled_features,df['TARGET CLASS'],test_size=0.3)


# # Using KNN
# 
# **Import KNeighborsClassifier from scikit learn.**

# In[62]:


from sklearn.neighbors import KNeighborsClassifier


# **Create a KNN model instance with n_neighbors=1**

# In[63]:


knn=KNeighborsClassifier(n_neighbors=1)


# **Fit this KNN model to the training data.**

# In[64]:


knn.fit(X_train,y_train)


# # Predictions and Evaluations
# Let's evaluate our KNN model!

# **Use the predict method to predict values using your KNN model and X_test.**

# In[65]:


predictions=knn.predict(X_test)


# ** Create a confusion matrix and classification report.**

# In[66]:


from sklearn.metrics import classification_report,confusion_matrix


# In[67]:


print(confusion_matrix(y_test,predictions))


# In[68]:


print(classification_report(y_test,predictions))


# # Choosing a K Value
# Let's go ahead and use the elbow method to pick a good K Value!
# 
# ** Create a for loop that trains various KNN models with different k values, then keep track of the error_rate for each of these models with a list. Refer to the lecture if you are confused on this step.**

# In[69]:


error_rate = []

# Will take some time
for i in range(1,40):
    
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))


# **Now create the following plot using the information from your for loop.**

# In[70]:


#plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')


# ## Retrain with new K Value
# 
# **Retrain your model with the best K value (up to you to decide what you want) and re-do the classification report and the confusion matrix.**

# In[76]:



knn = KNeighborsClassifier(n_neighbors=35)

knn.fit(X_train,y_train)
pred = knn.predict(X_test)

print('WITH K=15')
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))


# # Great Job!
