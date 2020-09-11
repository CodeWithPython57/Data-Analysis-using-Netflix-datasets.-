# In this file you will find the following info:
#1: Which movie is listed in which category
#2: Also can check this with any title also.
# 3: Comparison of : comedies vs Dramas.

from nltk.tokenize import sent_tokenize
import pandas as pd 
df=pd.read_csv('netflix_titles.csv')
print(df.columns)
listed=df['listed_in'].to_list()
types=df['type'].to_list()
title=df['title'].to_list()

# let's start with :1
for i in range(len(types)):
	value=title[i] + ': ' + types[i] + ' : ' + listed[i]
	print(sent_tokenize(value))

# only use title name  as a parametre for positive results.
def check(heading):
	if heading in title:
		i=title.index(heading)
		values=title[i] + ': ' + types[i] + ' : ' + listed[i]	
		print(sent_tokenize(values))
	else:
		print('NO data')

check('Love')			

#3 : Now check Comparison : Comedies vs Dramas
first1=[]
second1=[]
x1=[] # if the title[0] is comedy than 1 else 0
x2=[]# if the title[0] is drama than 1 else 0

def comparison(first,second):
	if (first in listed) and (second in listed):
		for i in range(len(listed)):
			var=listed[i]
			if 'Comedies' in var:
				first1.append(1)
				x1.append(1)
				x2.append(0)
			elif 'Dramas' in var:
				second1.append(1)
				x1.append(0)
				x2.append(1)
			else:
				x1.append(0),x2.append(0)
	else:
		print('Invalid input')

comparison('Comedies','Dramas')

p1=str((sum(first1)/len(title))*100)
p2=str((sum(second1)/len(title))*100)
print(p1+' percentage of first parameter')
print(p2+' percentage of second parameter')
#print(sum(second1))	
# print(sum(first1))				
# when you print these lines you find dramas movies and tvshow affected people most.
# just change the parameter to find more results.

# let's plot the results.
import matplotlib.pyplot as pt 
from matplotlib.pyplot import style
style.use('ggplot')

ids=[]
for i in range(len(title)):
	ids.append(i)

pt.subplot(2,2,1)
for i in range(100): # 100 is randomly taken number by me . you can choose any
	pt.scatter(x1[i],ids[i],color='red')
#zoom the results and check how many comedies movie or tvshow in id : 30 to 40 (7 : Comedy,3:Others)

pt.subplot(2,2,3)
for i in range(100):
	pt.scatter(x2[i],ids[i],color='black')
# zoom the results and check how many comedies movie or tvshow in id : 30 to 40 (7 : Comedy,3:Others)
pt.show()