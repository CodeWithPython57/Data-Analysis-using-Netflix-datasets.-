# In this file we will analyse the following points:
# 1: mostly movie or tv shows of which year ?
#2: 2018 movies vs 2019 movies example.
import pandas as pd 
df=pd.read_csv('netflix_titles.csv')
print(df.columns)
lis=df.columns.to_list()
lis.remove('show_id')
# import pandas for data visualization and reading csv file in that case and df.columns give the name of each columns

release=df['release_year'].to_list()
mini=min(release)
x=release.index(mini)
# 1925 : that means movie or tvshow which released in 1925 is the most oldest movie uploaded by netflix
# Let's find that movie or tvshow ?
# Also find title? Director? Country?  Description?When they upload?
for i in range(len(lis)):
	print(df.loc[x,lis[i]])
# this time I used pandas built in method just to get reult.
years_list=[]
for i in range(min(release),max(release)+1):
	years_list.append(i)

output=[]
x=[]
for i in range(len(years_list)):
	var=release.count(years_list[i])
	value=str(release.count(years_list[i])) +' video : ' + str(years_list[i])
	if var==0:
		x.append(0)
	else:
		output.append(value)
		x.append(var)
print(output)
# mostly videos which relase in 2018 and 2019 are uploaded by netflix this is the reason of success of Netlfix today.
# Why Netflix becomes popular ? I think Now you can find the answer.

# let's do some analysis using matplotlib.
import matplotlib.pyplot as pt 
from matplotlib.pyplot import style
style.use('ggplot')
# Let's check the first result: Netflix mostly upload old or new movies?
# if you wish to get more info than use code of 17,18 line.
pt.subplot(2,2,1)
pt.plot(x,years_list,color='black',linestyle='--')


# let's check 2019,2018 ,2017 vs 2016,2015,2014
# y1 is the list of number of videos in  2019,2018,2017 and y2 is the 2019,2018,2017 years
y1=[x[-2],x[-3],x[-4]]
y2=[years_list[-2],years_list[-3],years_list[-4]]
a1=[x[-5],x[-6],x[-7]]
a2=[years_list[-5],years_list[-6],years_list[-7]]
pt.subplot(2,2,4)
pt.plot(y1,y2,linestyle='--',color='black',label='2019 -2018 -2017')
pt.plot(a1,a2,linestyle=':',color='red',label='2017 -2016 -2015')
pt.legend()
pt.show()
# this is all about this file .Any Issue or any more addition please reply.


