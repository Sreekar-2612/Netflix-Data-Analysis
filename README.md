🎬 Netflix Data Analysis & Visualization using Python
✨ Overview

This project explores and visualizes Netflix’s Movies and TV Shows dataset to uncover insights about content production trends, genre diversity, country contributions, and audience ratings.
The goal is to transform raw data into a storytelling-driven analysis through data cleaning, visualization, and exploration.

⚙️ Tech Stack

🐍 Python 3

📊 Pandas, NumPy

🎨 Matplotlib, Seaborn

☁️ WordCloud

📈 Plotly Express (for interactive visuals)

📁 Dataset

Netflix Movies and TV Shows dataset (from Kaggle):
netflix_titles.csv

Rows: 8807
Columns: 12
Includes: title, director, cast, country, release year, rating, genre, and description.

🔍 Project Workflow

🧹 1. Data Cleaning

Handled missing data (country, rating, date_added)

Extracted new features: year_added, month_added

Standardized and parsed date_added with flexible format detection

📊 2. Exploratory Data Analysis (EDA)

Movies vs. TV Shows distribution

Top 10 producing countries

Content growth trend (by year)

Top 10 genres

Ratings distribution

Word cloud of Netflix titles

Interactive scatter plot → Release Year vs. Rating (by content type)

📈 Visual Highlights
Visualization	Description

🟦 Movie vs TV Show Count	Shows the ratio and dominance of content type
🌍 Top 10 Countries	Highlights global production diversity
📈 Content Growth	Tracks Netflix’s expansion year-over-year
🎭 Genre Popularity	Identifies top-viewed and produced genres
☁️ Word Cloud	Captures the most frequent words in Netflix titles
⭐ Ratings Spread	Visualizes the distribution of ratings

🧠 Key Insights
Movies dominate Netflix’s catalog, but TV shows have grown sharply in recent years.
United States, India, and United Kingdom contribute the majority of Netflix content.
The Drama and International Movies genres are the most common.
Content addition peaked around 2019, before stabilizing.

💻 Sample Visuals
📁 images/
├── type_distribution.png
├── top_countries.png
├── content_growth.png
├── genres.png
├── wordcloud.png
├── ratings.png

#Python #DataAnalysis #Visualization #NetflixDataset #Plotly #EDA #WordCloud #Seaborn
