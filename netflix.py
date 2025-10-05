import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import plotly.express as px

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette('Set2')

df = pd.read_csv("netflix_titles.csv")
print("Dataset shape: ",df.shape)
df.head()

#now data cleaning
print(df.isnull().sum())
# if there are any country names missing , fill with unknomw
df['country'].fillna('Unknown',inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce', format='mixed')



df.dropna(subset=['rating','duration'],inplace=True)

print("Total titles: ",len(df))
print("Movies:",len(df[df['type'] == 'Movie']))
print("TV shows:",len(df[df['type']=='TV Show']))
print("\nData Range:",df['release_year'].min(),"to",df['release_year'].max())

sns.countplot(data = df,x='type',palette = 'coolwarm',legend=False)
plt.title('Distribution of Movies and Tv shows on netflix',fontsize = 14)
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

#production of netflix content

country_data = df['country'].value_counts().head(10)
plt.figure(figsize=(8,5))
sns.barplot(x=country_data.values,y=country_data.index,palette='magma')
plt.title('Top ten countries contributing to the majority of Netflix content')
plt.xlabel('No of contributions')
plt.show()

df['year_added'] = df['date_added'].dt.year
content_trend = df['year_added'].value_counts().sort_index()

plt.figure(figsize = (10,5))
sns.lineplot(x=content_trend.index,y=content_trend.values,marker='o')
plt.title('Netflix Content growth over the years')
plt.xlabel('Year added to Netflix')
plt.ylabel('No of productions')
plt.show()

genres = df['listed_in'].str.split(',').explode().str.strip()
top_genres = genres.value_counts().head(10)

plt.figure(figsize=(8,5))
sns.barplot(y=top_genres.index,x=top_genres.values,palette='viridis')
plt.title('Top 10 genres on netflix')
plt.xlabel('Count')
plt.show()

title_words = ' '.join(df['title'])
wordcloud = WordCloud(width=1200,height=600,background_color='black',colormap='plasma').generate(title_words)

plt.figure(figsize=(12,6))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.title('Netflix Titles')
plt.show()

plt.figure(figsize=(10,5))
sns.countplot(data=df, x='rating', order=df['rating'].value_counts().index, palette='cool')
plt.title('Distribution of Ratings on Netflix')
plt.xticks(rotation=45)
plt.show()

fig = px.scatter(df, x='release_year', y='rating', color='type',
                 hover_data=['title', 'country'],
                 title="Netflix Content Distribution by Release Year and Rating")
fig.show()
