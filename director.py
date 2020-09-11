# In this file you can find  Each and every director name  with movie or TVshow director. Example: Brad Anderson : Movie
# YOu can find for all and also for any particular director.
# Mainly you can find : Example: How many TvShows and Movie  are published by Brad Anderson  on Netflix or any director. 


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

title=df['director'].to_list()
#print(title) # Name of all the movie or TVShow 

info=df['type'].to_list()
result=[]
# modify changes according to result

for i in range(len(info)):
	try:
		if info[i]=='Movie':
			value=title[i]+' : Movie director'
			result.append(value)
		else:
			value=title[i]+ ' : TV Show director'	
			result.append(value)
	except:
		result.append('No name')
# According to csv file if director name not given WE will reject that using no name.

# let's check the result one by one
from nltk.tokenize import sent_tokenize
for i in range(len(result)):
	print(sent_tokenize(result[i]))


def check(director_name):
	if director_name in title:
		value=title.index(director_name)	
		print(result[value])
	else:
		print('No data with this name')

check('Brad Anderson')

#let's check which director mostly directed movie or TVShow more or director with more than one.

def output(director):
	if director in title:
		count=title.count(director)
		value=title.index(director)
		print(result[value],end=':')
		print('With '+ str(count)+ ' shows on Netflix')
	else:
		print('No data found')


output('Brad Anderson')			


# so this is all analysis fot this dataset. NO plotting results. IF you think any plotting result. Than please reply.
