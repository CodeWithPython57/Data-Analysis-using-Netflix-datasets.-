# In movie_or_tv.py file We will find how many tv shows and movies are published by  netflix from 2008 to Aug2020
# first step to import pandas for data visualization
import pandas as pd 
# netflix_titles.csv  contains information of 4000 videos
#  read csv file Using pandas

df=pd.read_csv('netflix_titles.csv')
# df is the dataframe

print(df.columns)
# df.columns gives all columns headings

print(df['type'].head(10))
# First 10 videos are movie or tv show 
# Let's predict for all videos 

videos=df['type'].to_list()
# videos list contains movie or tvshow

movie_list=[]
# if movie than in this list.

tvshow_list=[]
#if tv show than in this list.

for i in range(len(videos)):
	if videos[i]=='Movie':
		movie_list.append('Movie')
	elif videos[i]=='TV Show':
		tvshow_list.append('TV Show')
	else:
		print('NOt a movie and not a Tv Show')

# let's count number of movie and its precentage  
print('Number of movies are '+str(len(movie_list)))
# so these are the total number of movies uploaded by Netflix since Aug 2020 			 	

percenatge1=(len(movie_list)/len(videos))*100
print(str(percenatge1)+ ' is the precentage of movies')
#Percentage1 of movies : 

# let's count number of TV show and its precentage  
print('Number of tvshow are '+str(len(tvshow_list)))
# so these are the total number of TVSHow uploaded by Netflix since Aug 2020 			 	

percenatge2=(len(tvshow_list)/len(videos))*100
print(str(percenatge2)+ ' is the precentage of TVSHow')
#Percentage1 of TVSHOw :

# Let's predict the resuls using matplotlib.
import cv2 as cv 
import matplotlib.pyplot as pt 
from matplotlib.pyplot import style
style.use('ggplot')

# x1 is the list of movies and x2 is the list of movies
# y1 and y2 are the list of numbers 
x1=[]
x2=[]
y1=[]
y2=[]
for i in range(len(videos)):
	if videos[i]=='Movie':
		x1.append(i)
		y1.append(i)
	elif videos[i]=='TV Show':
		x2.append(i)
		y2.append(i)
	else:
		print('NOt a movie and not a Tv Show')
# By using scatter you can predict what netflix mostly upload for their business

pt.subplot(2,2,1)
pt.scatter(x1,y1,color='red')
pt.scatter(x2,y2,color='black')

pt.subplot(2,2,4)
pt.xlabel('videos')
pt.ylabel('Days')
pt.plot(x1,color='red',label='Movies',linestyle='--')
pt.plot(x2,color='black',label='TV Show',linestyle='--')
pt.legend()

# Let's add a netflix image to become more beautiful
image=cv.imread('net.jpg',1)
cv.imshow('image.png',image)
cv.waitKey(0)
cv.destroyAllWindows()

pt.show()