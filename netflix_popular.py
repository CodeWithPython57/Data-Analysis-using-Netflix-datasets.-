# In this file you will find in which year netflix becomes popular by uploading max video per year.
# In this file you will find when netflix release their first video and last video since Aug2020.

import pandas as pd 
df=pd.read_csv('netflix_titles.csv')
print(df.columns)
# import pandas for reading csv file data and df.columns show all attributes.


dates=df['date_added'].to_list()
# date_added contains information like : 9 September,2018 or 18 August,2009. We need only year not the month and date so modify the data and make some changes.

years=[]
# years list conatins each year when they upload video
from nltk.tokenize import word_tokenize
for i in range(len(dates)):
	try:
		word=word_tokenize(dates[i])		
		years.append(word[-1])		
	except:
		pass	
# Using Nltk for this . This is too simple and don't use any other option as it becomes more complex.

# when they upload their first video
# Exception : Some columns are blank that means they do'nt show the date when they upload so I reject that data.
first_show=min(years)
print(first_show)
# 2008 is the year when netflix start uploading their video.

# Let's count the actual date of first video.
value=years.index(first_show)
print(dates[value])# January 1,2008
# Let's count for 2015
second_show=years.count('2015')
print(second_show)  #90 videos are uploaded on 2015

def datawise(which_year):
	data_year=[]
	# we can make a function also which automatic do this.
	for i in range(len(years)):
		if years[i]==which_year:
			data_year.append(dates[i])
		else:
			pass
	return (data_year)		

data_2015=datawise('2015')
print(data_2015)
# Output of the list shows the dates of all 90 videos
#print(data_2015)
# If you try to find for 2016 just change the '2015' in line47

data_2016=datawise('2016')
#print(data_2016)




# Let's analysis for when they becomes more popular
# becomes simple task by creating a list of years
dummy_years=['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017',
'2018','2019','2020']

video_year=[]
for i in range(len(dummy_years)):
	value=years.count(dummy_years[i])
	video_year.append(value)

max_videos=max(video_year)


max_year=dummy_years[video_year.index(max_videos)]

print('In year '+ str(max_year)+ ' Netflix becomes popular by uploading '+str(max_videos)+' videos')
# 2019 IS the year of Neflix

# Let's plot the result using matplotlib
import matplotlib.pyplot as pt 
from matplotlib.pyplot import style
style.use('ggplot')


pt.subplot(2,2,1)
pt.xlabel('Years')
pt.ylabel('Upload_per_year')
pt.plot(dummy_years,video_year,color='black')

# Comparison of any  two years
pt.subplot(2,2,1)
pt.xlabel('Years')
pt.ylabel('Upload_per_year')
# compare : 2018,2019 : 365 days

pt.subplot(2,2,4)
pt.plot(data_2015,color='black',label='2015',linestyle='--')
pt.plot(data_2016,color='red',label='2016',linestyle=':')
#2016 wins
pt.legend()

#let's analyse the result of 2019 only. So we can check one year also



data_2019=datawise('2019')
pt.subplot(2,2,3)
pt.plot(data_2019,color='blue')
# this is all about analysis for this file.
pt.show()	