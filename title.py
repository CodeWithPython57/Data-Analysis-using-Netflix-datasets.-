# In this file you can find the name of all the movies or TVSHOWS
# Mainly you can find : Apaches movie or TV and 6Years movie or TV show Good people MOvie or TVShow.

import cv2 as cv 
image=cv.imread('net.jpg',1)
cv.imshow('image',image)
k=cv.waitKey(0)
if k==ord('s'):
	cv.destroyAllWindows()
else:
	pass
# If you type s key than the image will remove automatically.
# this cv piece of code is used for GUI purpose only.


import pandas as pd 
df=pd.read_csv('netflix_titles.csv')
print(df.columns)
# import pandas for data visualization and read csv file and check all columns

title=df['title'].to_list()
#print(title) # Name of all the movie or TVShow 

info=df['type'].to_list()
result=[]
# modify changes according to result

for i in range(len(info)):
	if info[i]=='Movie':
		value=title[i]+' : Movie'
		result.append(value)
	elif info[i]=='TV Show':
		value=title[i]+ ' : TV Show'	
		result.append(value)
	else:
		value=title[i] + ': Not defined by Netflix'

# let's check the result one by one
from nltk.tokenize import sent_tokenize
for i in range(len(result)):
	print(sent_tokenize(result[i]))


# let's check for any particular title
# let's check for Love : Movie in Netflix
def check(text):
	if text in title:
		a=title.index(text)
		name=result[a]
		print(name)
	else:
		print('Not uploaded by Netflix ')	

check('Love') # Movie 
check('Friends') # TVshow
# Just change the text in function check to grab more results.

# This is all about information analysis in this file. We grab the information which is TV or Movie and particular title name also that this is movie or TVSHow
