
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
sns.set(color_codes = True)


# In[23]:


movies = pd.read_csv("fandango_score_comparison.csv")


# In[24]:


print(movies["Metacritic_norm_round"].value_counts())


# In[25]:


mc_norm_round = sns.distplot(movies["Metacritic_norm_round"],
                             kde = False, rug = True, bins = 9)
axes = mc_norm_round.axes
axes.set_xlim(0,5)


# In[26]:


#this shows spread but have to forgive positions


# In[27]:


print(movies["Fandango_Stars"].value_counts())


# In[28]:


fnd_stars = sns.distplot(movies["Fandango_Stars"],
                             kde = False, rug = True, bins = 9)
axes = fnd_stars.axes
axes.set_xlim(0,5)


# Fandango ratings clearly higher on average whereas metacritic has a more even distribution. 

# In[29]:


mean_fnd_stars = sum(movies["Fandango_Stars"]) / len(movies["Fandango_Stars"])
mean_mc_norm_round = sum(movies["Metacritic_norm_round"]) / len(movies["Metacritic_norm_round"])
median_fnd_stars = np.median(movies["Fandango_Stars"])
median_mc_norm_round = np.median(movies["Metacritic_norm_round"])
std_fnd_stars = np.std(movies["Fandango_Stars"])
std_mc_norm_round = np.std(movies["Metacritic_norm_round"])


# In[30]:


print("Fandango mean:",format(mean_fnd_stars,'.1f'))
print("Metacritic mean:",format(mean_mc_norm_round,'.1f'))
print("Fandango median:",median_fnd_stars)
print("Metacritic median:",median_mc_norm_round)
print("Fandango standard deviation:",format(std_fnd_stars,'.1f'))
print("Metacritic standard deviation:",format(std_mc_norm_round, '.1f'))


# In terms of methodology, Fandango appears to inflate ratings and isn't transparent about how it calculates and aggregates ratings. Metacritic publishes each individual critic rating, and is transparent about how they aggregate them to get a final rating.

# In terms of values, The median metacritic score appears higher than the mean metacritic score because a few very low reviews "drag down" the median. The median fandango score is lower than the mean fandango score because a few very high ratings "drag up" the mean.
# 
# Fandango ratings appear clustered between 3 and 5, and have a much narrower random than Metacritic reviews, which go from 0 to  5.
# 
# Fandango ratings in general appear to be higher than metacritic ratings.
# 
# These may be due to movie studio influence on Fandango ratings, and the fact that Fandango calculates its ratings in a hidden way.

# As an additional comment, the questions asked rely on an assumption that there is a difference in values when really they are only rounding differences, inapproriate ones at that

# In[31]:


sns.regplot(x=movies["Fandango_Stars"], y=movies["Metacritic_norm_round"], fit_reg=False)


# In[32]:


movies["fm_diff"] = movies["Metacritic_norm_round"] - movies["Fandango_Stars"]


# In[33]:


movies["fm_diff"] = abs(movies["fm_diff"])


# In[34]:


movies.sort_values("fm_diff", ascending=False).head(5)


# In[35]:


from scipy.stats.stats import pearsonr


# In[36]:


r, p_value = pearsonr(movies["Metacritic_norm_round"], movies["Fandango_Stars"])


# In[41]:


print("r value is:",format(r, '.2f'))
print("p value is:",format(p_value, '.2f'))


# Correlation not high as shown by r value, so scores not inflated, theyre somehow fundamentally different in their ratings

# In[42]:


from scipy.stats import linregress


# In[45]:


slope, intercept, r_value, p_value, std_err = linregress(movies["Metacritic_norm_round"], movies["Fandango_Stars"])


# In[46]:


pred_3 = 3 * slope + intercept


# In[48]:


format(pred_3, '.1f')


# In[49]:


pred_1 = slope + intercept
format(pred_1, '.1f')


# In[51]:


pred_5 = 5 * slope + intercept
format(pred_5, '.1f')


# In[52]:


sns.regplot(x=movies["Fandango_Stars"], y=movies["Metacritic_norm_round"], fit_reg=True)


# In[53]:


plt.scatter(movies["Metacritic_norm_round"], movies["Fandango_Stars"])
plt.plot([1,5],[pred_1,pred_5])
plt.xlim(1,5)
plt.show()

