
# 1. Region and Domain
# State the region and the domain category that your data sets are about
# 1-1) the region : South Lyon, Michigan, United States
# 1-2) the domain category : weather data & used car sales data



# 2 Research Question
# state a question about the domain category and region
# I was curious about what the market price of used cars was like overseas, and especially how much the price difference was with Japanese cars.
# I was curious about how much the level of used car prices has changed compared to the past, and I was curious about the level of Korean cars abroad.
# In particular, I was curious about the correlation between weather and used car prices.



#3 Links
#You must provide at least two links to publicly accessible datasets. 
#These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.

# 3-1) weather data in South Lyon, Michigan, United States: 
#    -> https://www.wunderground.com/history/monthly/us/mi/waterford/KPTK/date/
# 3-2) used car data in South Lyon, Michigan, United State : 
#    -> https://www.cargurus.com/Cars/price-trends/



#4 Image
#You must upload an image which addresses the research question you stated. 
#In addition to addressing the question, this visual should follow 
# Cairo’s principles of truthfulness, functionality, beauty, and insightfulness.

##########################################################################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import the wheather
weather_df = pd.read_csv('C:\\cjj\\Pyhon\\coursera\\weather_data.csv')

#date variable concatenate
weather_df['date'] = weather_df['year'].astype('str') + '_' + weather_df['month'].astype('str') + '_' + weather_df['day'].astype('str')
weather_df = weather_df.drop(['year','month','day'],axis=1)

#Convert Fahrenheit to Celsius
weather_df['Temp_Avg_C'] = (weather_df['Temperature_Avg'] - 32) * 0.55

# import used car data
car_df = pd.read_csv('C:\\cjj\\Pyhon\\coursera\\used_car_data.csv')
car_df = car_df.iloc[:,:10]

#date variable concatenate
car_df['date'] = car_df['year'].astype('str') + '_' + car_df['month'].astype('str') + '_' + car_df['day'].astype('str')

#used car data & weather data merge
merge_df = pd.merge(car_df,weather_df, how='left', on = 'date')
merge_df.columns

#groupby (year, month)
group_mean = merge_df.groupby(['year','month']).mean()
group_mean.columns
group_mean = group_mean.reset_index()
group_mean['year_month'] = group_mean['year'].astype('str') + '_' + group_mean['month'].astype('str')


#car price data check for line plot
x = np.arange(len(group_mean))
y1 = list(group_mean['genesis'])
y2 = list(group_mean['hyundai'])
y3 = list(group_mean['kia'])
y4 = list(group_mean['toyota'])
y5 = list(group_mean['lexus'])

#temp data check for line plot
y6 = list(group_mean['Temp_Avg_C'])

##########################################################################################################
#1). korea car price data plotting
plt.style.use('default')
plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.size'] = 20

plt.figure(dpi=200)
plt.subplot(1, 2, 1) 
plt.plot(x, y1, color='red', marker='o', linewidth=5, markersize=10, label='genesis',alpha=.5)
plt.plot(x, y2, color='blue', marker='o', linewidth=5, markersize=10, label='hyundai',alpha=.5)
plt.plot(x, y3, color='green', marker='o', linewidth=5, markersize=10, label='kia',alpha=.5)
plt.xticks(np.arange(len(group_mean)), labels=list(group_mean['year_month']),rotation=90, fontsize = 12)

plt.title("used car prices in korea")
plt.xlabel("year_month")
plt.ylabel("price (100$)")
plt.legend()

#2). japan car price data plotting
plt.subplot(1, 2, 2) 
plt.plot(x, y4, color='black', marker='^', linewidth=5, markersize=10, label='toyota',alpha=.5)
plt.plot(x, y5, color='purple', marker='^', linewidth=5, markersize=10, label='lexus',alpha=.5)
plt.xticks(np.arange(len(group_mean)), labels=list(group_mean['year_month']),rotation=90, fontsize = 12)

plt.title("used car prices in japan")
plt.xlabel("year_month")
plt.ylabel("price (100$)")
plt.legend()
plt.tight_layout()
plt.show()


##########################################################################################################
#3). temperature data plotting
plt.figure(dpi=200)
plt.plot(x, y6, color='red', marker='o', linewidth=5, markersize=10, label='temp (c)',alpha=.5)
plt.xticks(np.arange(len(group_mean)), labels=list(group_mean['year_month']),rotation=90, fontsize = 12)

plt.title("temp data in South Lyon, Michigan")
plt.xlabel("year_month")
plt.ylabel("temperature (C)")
plt.legend()

plt.tight_layout()
plt.show()

##########################################################################################################
#month data group
month_group_mean = merge_df.groupby(['month']).mean()
month_group_mean.columns
month_group_mean = month_group_mean.reset_index()
month_group_mean['korea'] = (month_group_mean['genesis'] + month_group_mean['hyundai'] + month_group_mean['kia'])/3
month_group_mean['japan'] = (month_group_mean['toyota'] + month_group_mean['lexus'])/2


##########################################################################################################
#4). temperature & car price data plotting 
x_month = np.arange(len(month_group_mean))[:-2]
y_korea = list(month_group_mean['korea'])[:-2]
y_japan = list(month_group_mean['japan'])[:-2]
y_temp = list(month_group_mean['Temp_Avg_C'])[:-2]
plt.figure(dpi=200)
fig, ax1 = plt.subplots()
ax1.set_xlabel('month')
ax1.set_ylabel('price (100$)')
ax1.set_title('temperature & car price data plotting')

line1 = ax1.plot(x_month, y_korea, color='red', marker='o', linewidth=10, markersize=12, label='korea',alpha=.5)
line2 = ax1.plot(x_month, y_japan, color='purple', marker='o', linewidth=10, markersize=12, label='japan',alpha=.5)

ax2 = ax1.twinx()
ax2.set_ylabel('temperature (C)')
line3 = ax2.plot(x_month, y_temp, color='blue', marker='o', linewidth=10, markersize=12, label='temperature (C)',alpha=.5)

lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')
plt.tight_layout()
plt.show()

##########################################################################################################
#5). boxplot 

plt.style.use('default')
plt.rcParams['figure.figsize'] = (7, 5)
plt.rcParams['font.size'] = 12
fig, ax = plt.subplots()
ax.boxplot([y_korea, y_japan], sym="bo", notch=False, whis=2.5)
ax.set_xlabel('country')
ax.set_ylabel('price (100$)')
ax.set_title('car price box plot between korea and japan')
plt.xticks([1, 2], ['korea', 'japan'])
plt.tight_layout()
plt.show()


##########################################################################################################
#6). correlation between temperature & car price
# corr plot between temp vs car price
import seaborn as sns
data = pd.DataFrame([y_korea,y_japan,y_temp]).T
data.columns = ['korea','japan','temp']

normalization_df = (data - data.mean())/data.std()

corr = normalization_df.corr()
sns.heatmap(corr,annot=True).set(title='car price vs temp')
plt.tight_layout()
plt.show()


# 5 Discussion
#You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.

# I am very interested in the level of overseas price of Korean automobile companies like Hyundai Motor Company.
# In particular, I am curious about used car price. I want to know the difference in price with Japanese cars.
# First, we checked how the current status of used car prices has changed since 2019.
# As a result of the confirmation, it was confirmed that the used car price was increasing compared to 2019, and it was confirmed that the used car price of Genesis was on the rise from the decreasing trend.
# And we compared the differences with Japanese cars. As a result of checking the overall price level with boxplot, it was confirmed that Japanese cars are slightly higher than Korean cars.
# However, in the case of Lexus, it has been confirmed that used car prices are on the decline.
# This result shows that the level of Korean cars is getting better than before.

# I think there may be a relationship between the weather and car price
# so I checked about the correlation between the weather and used car price of Hyundai Motor Company in South Lyon, Michigan, United States.
# First, check the weather in Michigan. It was an area with good weather from -5 degrees to 25 degrees.
# And the weather and car prices were summarized by month, and a double-axis graph was drawn and checked. As a result of checking, it was found that the price of used cars increased as time passed. Therefore, correlation analysis was performed additionally.
# Before the correlation analysis, normalization was performed for each variable, and when checking the analysis results, Korean cars showed a correlation with temperature, but Japanese cars did not. I think that further confirmation is needed as to why this result came out.

















