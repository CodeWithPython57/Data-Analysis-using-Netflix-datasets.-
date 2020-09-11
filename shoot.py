# In this file we grab following information
#1: which movie is shooted in which country
#2: Which movie is shooted in only one country not more than one country
#3: Which country is mostly used for shooting that means this is the best country for shooting movies and TVSHow 

import pandas as pd 
df=pd.read_csv('netflix_titles.csv')
types=df['type'].to_list()
country=df['country'].to_list()
title=df['title'].to_list()
# type contains data movie and Tvshow only and country data contain country name only.
x=[]
for i in range(len(types)):
	try:
		value=title[i] + ' :'+ types[i]+ ' :' + country[i] 
		x.append(value)
	except:
		x.append('no data')
	# so if the data contains blank space it will treated as no data.	

# just type the name of movie or tvshow to check the info.
def check(heading):
	if heading in title:
		print(x[title.index(heading)])
	else:
		print('NO data')	

check('Love')

# let's check which movie or tvshow is shooted in only one country.
from nltk.tokenize import word_tokenize
single=[]
double=[]
counting=[]
for i in range(len(country)):
	try:	
		value=word_tokenize(country[i])
		
# now a short trick to get this. If there are more than one country so ',' is present in list and if ',' not in list so only one country.
# just think for 5 minutes .

		if ',' in value:
			values=title[i] + ' :'+ types[i]+ ' : ' + country[i]
			double.append(values)
			counting.append(country)
		else:
			values=title[i] + ' :'+ types[i]+ ' : ' + country[i]
			single.append(values)
			counting.append(country)

	except:
		pass # if country name not given so ignore that data.
#single list contains data of movie and tvshow shooted in single country
#double list contains data of movie and tvshow shooted in more than one country
# please check the output of single and double list.
# I Choose covid19 datasets to get the name of each country
# total_cases.csv file used 
df1=pd.read_csv('total_cases.csv')
lis=df1.columns.to_list()
lis.remove('date')
lis.remove('World')
# lis list contains thre name of every country.

# this will be numeric data
final_count=[]
for i in range(len(lis)):
	number=country.count(lis[i])
	final_count.append(number)

x=max(final_count)
for i in range(len(country)):
	if country.count(country[i])==x:
		print('Country : '+ country[i] + ' is the  place where '+ str(x)+ ' movies and tvshows shoot for netflix.')
		break
	else:
		pass	

# just change the value of x to predict more results.


# plotting results 
# let's plot every country used for how many  shoot results.
import matplotlib.pyplot as pt 
from matplotlib.pyplot import style
style.use('ggplot')
pt.subplot(2,2,2)
for i in range(len(lis)):
	pt.scatter(final_count[i],lis[i])
# when you zoom out result top three country: USA,IND,UK

# let's see USA vs Ind
x1=[]
x2=[]
def comparison(country1,country2):
	for i in range(len(country)):
		try:
			if country1 in country[i]:
				x1.append(i)
			elif country2 in country[i]:
				x2.append(i)
			else:
				pass		
		except:
			pass	
comparison('United States','India')
# you can perform comparison of any two country just by changing the names.
pt.subplot(2,2,3)
pt.plot(x1,color='black',label='country1')
pt.plot(x2,color='blue',label='country2')	
pt.legend()			
pt.show()
# this is all anout this file. If there are issues please let me know.
