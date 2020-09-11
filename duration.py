# In this file we will analyse the following points:
# 1: anlaysis of movie timing or duration. Mostly movie are of x duration .so we find x
#2: Compare the results of movie duration mostly vs minimum 


import pandas as pd 
from nltk.tokenize import word_tokenize
df=pd.read_csv('netflix_titles.csv')
print(df.columns)
x=df['duration'].to_list()
types=df['type'].to_list()
#print(x)
movie_time=[]
tv_time=[]
for i in range(len(types)):
	value=word_tokenize(x[i])
	if types[i]=='Movie':
		movie_time.append(int(value[0]))
	elif types[i]=='TV Show':
		tv_time.append(int(value[0]))
# if you are printing movie_time list you can find mostly movie of which time
# if you print tv_time you can find tvshow mostly of which seasons
# this is the first analysis you can do now.

# Let's discuss how many movies are less than 80 min or how many graater than 80
less_than=[]
greater_than=[]
def movie_comparison(compare_time):
	try:
		for i in range(len(movie_time)):
			if movie_time[i]>=compare_time:
				less_than.append(movie_time[i])
			else:
				greater_than.append(movie_time[i])	
	except ValueError:
		print('Invalid Input')

movie_comparison(80)
# just change the parametre to compare diff results.
#let's check the percentage
# percentage1 : less than 80 min 
# percentage2: greater than 80 min
percentage1=(len(less_than)/len(movie_time))*100
percentage2=(len(greater_than)/len(movie_time))*100
print(percentage1,percentage2)
# almost 81% of movies are less than 82 minutes.


# Tv shows comparison :1 tvshow vs more than 1 tvhow
less=[]
greater=[]
def tv_comparison(time):
	try:
		for i in range(len(tv_time)):
			if tv_time[i]>time:
				less.append(tv_time[i])
			else:
				greater.append(tv_time[i])	
	except ValueError:
		print('Invalid Input')

tv_comparison(1)
# change the parametre and shows more results.
# less list shows that how many tvshows only have 1 season
# greater list shows that how many tvshows have more than 1 season
# p1 : percentage of 1 season and p2 : percentage of more than 1 season
p1=(len(less)/len(tv_time))*100
p2=(len(greater)/len(tv_time))*100
print(p1,p2)


import matplotlib.pyplot as pt 
from matplotlib.pyplot import style
style.use('dark_background')

pt.subplot(2,2,1)
pt.plot(less_than,color='blue',label='Less than 80 min')
pt.plot(greater_than,color='red',label='greater than 80 min')
# subplot 1 shows comparison results.

pt.subplot(2,2,2)
pt.plot(movie_time,linestyle='--',color='red',linewidth=0.8)
# subplot 2 shows movie_time results.

pt.subplot(2,2,3)
pt.plot(tv_time,linestyle='--',color='blue')
#subplot 3 shows tv_time results.

pt.subplot(2,2,4)
pt.plot(less,color='blue',label='Less than 1 Season ')
pt.plot(greater,color='red',label='greater than 1 Season')
# subplot 4 shows comparison results.

pt.show()