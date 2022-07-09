#!/usr/bin/env python
# coding: utf-8

# In[1]:


#-------------------------------------------------Question 1--------------------------------------------------------------#


# In[ ]:


#Import Pandas(For Data Analyisis), Seaborn(For the scatter plot heat map), 
#forex(Real time curreny exchange), matplotlib(Math, Exception Handling)
import pandas as pd
import seaborn as sns
from forex_python.converter import CurrencyRates
from matplotlib import rcParams
from matplotlib.axes._axes import _log as matplotlib_axes_logger
#Exception Handling for the Stars vs. Price table
matplotlib_axes_logger.setLevel('ERROR')
#Imports TELEVISON.csv from the D: drive and handles exceptions
tv=pd.read_csv('D:/TELEVISION.csv', encoding= 'unicode_escape')
#Changes the column names 
tv.columns = ['Brand Name','Stars','Ratings','Reviews','Current Price', 'MSRP', 'Services','OS','Picture Quality','Speakers','Frequency']


# In[ ]:


#Converts from Indian ruppes to USD in real time
cr = CurrencyRates()
tv['Current Price'] = cr.convert("INR","USD",tv['Current Price'])
tv['MSRP'] = cr.convert("INR","USD",tv['MSRP'])


# In[ ]:


#Makes seperate list for tv's with certain attributes
services4 = tv.loc[tv["Services"] == "Netflix|Prime Video|Disney+Hotstar|Youtube"]
services3 = tv.loc[tv["Services"] == "Netflix|Disney+Hotstar|Youtube"]
services2 = tv.loc[tv["Services"] == "Netflix|Prime Video|Youtube"]
services1 = tv.loc[tv["Services"] == "Youtube"]

picquality5 = tv.loc[tv['Picture Quality'] == "Ultra HD (4K) 3840 x 2160 Pixels"]
picquality4 = tv.loc[tv['Picture Quality'] == "Full HD 1920 x 1080 Pixels"]
picquality3 = tv.loc[tv['Picture Quality'] == "HD Ready 1366 x 768 Pixels"]

speakers5 = tv.loc[tv['Speakers'] == "60 W Speaker Output"]
speakers4 = tv.loc[tv['Speakers'] == "40 W Speaker Output"]
speakers3 = tv.loc[tv['Speakers'] == "24 W Speaker Output"]
speakers2 = tv.loc[tv['Speakers'] == "20 W Speaker Output"]
speakers1 = tv.loc[tv['Speakers'] == "10 W Speaker Output"]

rr5 = tv.loc[tv['Frequency'] == "200 Hz Refresh Rate"]                  
rr4 = tv.loc[tv['Frequency'] == "120 Hz Refresh Rate"]
rr3 = tv.loc[tv['Frequency'] == "100 Hz Refresh Rate"]
rr2 = tv.loc[tv['Frequency'] == "60 Hz Refresh Rate"]
rr1 = tv.loc[tv['Frequency'] == "50 Hz Refresh Rate"]


# In[ ]:


#Creates a empty dictonary, key = index, value = Features Score
scores = {}
for index, row in tv.iterrows():
    base = {index : 0}
    scores.update(base)


# In[ ]:


#Take the tables created above and uses their postion in the original table to assign the correct index and score
for index, row in services4.iterrows():
    scores[index] = scores[index] + 4
for index, row in services3.iterrows():
    scores[index] = scores[index] + 3
for index, row in services2.iterrows():
    scores[index] = scores[index] + 2
for index, row in services1.iterrows():
    scores[index] = scores[index] + 1
    
for index, row in picquality5.iterrows():
    scores[index] = scores[index] + 5
for index, row in picquality4.iterrows():
    scores[index] = scores[index] + 4
for index, row in picquality3.iterrows():
    scores[index] = scores[index] + 3
    
for index, row in speakers5.iterrows():
    scores[index] = scores[index] + 5
for index, row in speakers4.iterrows():
    scores[index] = scores[index] + 4
for index, row in speakers3.iterrows():
    scores[index] = scores[index] + 3
for index, row in speakers2.iterrows():
    scores[index] = scores[index] + 2
for index, row in speakers1.iterrows():
    scores[index] = scores[index] + 1
    
for index, row in rr5.iterrows():
    scores[index] = scores[index] + 5 
for index, row in rr4.iterrows():
    scores[index] = scores[index] + 4     
for index, row in rr3.iterrows():
    scores[index] = scores[index] + 3
for index, row in rr2.iterrows():
    scores[index] = scores[index] + 2
for index, row in rr1.iterrows():
    scores[index] = scores[index] + 1

#↓ Shows dictonary ↓
#print(scores) 


# In[ ]:


#Swaps the columns and rows and uses the dictonairy index for the tables index then combines the tables on the index
scores_table = pd.DataFrame.from_dict(scores, orient ='index') 
scores_table.columns = ['Features Score']
final_table = pd.concat([tv, scores_table], axis =1)


# In[ ]:


#Sorts and displays the top ten scores by Features Score from final_table_sorted
final_table_sorted = final_table.sort_values(by=['Features Score'], ascending = False)
final_table_sorted.head(10)


# In[ ]:


#-------------------------------------------------Question 2--------------------------------------------------------------#


# In[ ]:


#Creates a table where there has to be at least 1 rating then displays the top ten products with the highest stars
ratings_table = final_table.loc[final_table["Ratings"] > 0]
ratings_table_sorted = ratings_table.sort_values(by=['Stars'], ascending = False)
ratings_table_sorted.head(10)


# In[ ]:


#Scatter plot showing Current Price vs. Stars
ratings_table.plot.scatter(x = 'Stars', y = 'Current Price', figsize=(15, 8),yticks = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300])


# In[ ]:


#Scatter plot displaying Feature score vs. Stars with the density of tv's being represented by colors
plt.figure(figsize = (15,8))
counts = ratings_table.groupby(by=['Features Score','Stars']).size().to_frame('Amount of Televisions').reset_index()
sns.scatterplot(data=counts, x='Stars', y='Features Score', hue='Amount of Televisions')

