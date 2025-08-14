# Sentiment Analysis of Tweets 🚀

This project aims to transform raw Twitter data into a smart sentiment analysis model capable of classifying tweets as **positive** or **negative**. It showcases the end-to-end workflow of a typical NLP project, from data exploration to model deployment.

## Extended Description 💭

### Background
Social media is full of opinions, but analyzing them automatically is challenging due to noise and inconsistencies. Tweets are short, often include slang, emojis, links, mentions, and repeated words — all of which can confuse a machine learning model.  

The goal of this project was to build a robust sentiment analysis pipeline that can handle messy Twitter data and produce meaningful insights.

### Workflow

#### 1. Data Exploration 🔍
- Examined the dataset for **imbalances**: negative tweets were much more frequent than positive ones, which could bias the model.  
- Identified patterns and trends in sentiment over time.  
- Visualized the most frequent words and their sentiment associations.

#### 2. Data Cleaning 🧹
- **Removed unnecessary content**:
  - Links (`https://t.co/...`)
  - Mentions (`@username`)
  - Numbers, dates, emojis, and symbols
  - Repeated words
- Normalized text to lowercase and handled common preprocessing tasks like tokenization.  

*Fun fact:* “love” ❤ and “hate” 😡 were the most common words.

#### 3. Feature Engineering 📈
- Applied **TF-IDF vectorization** to convert text into numerical features.  
- Explored n-grams and other feature combinations to improve model performance.

#### 4. Model Building 🤖
- Chose **Logistic Regression** for classification due to its simplicity and effectiveness on sparse text data.  
- Evaluated the model using metrics such as **accuracy, precision, recall, and F1-score**.  
- Ensured minimal overfitting by splitting the dataset into training and validation sets.

#### 5. Deployment & Interaction 🌐
- Built an **interactive Streamlit app** allowing users to input their own tweets and receive sentiment predictions in real-time.  
- The app provides a simple interface for anyone to test the model without programming knowledge.

### Applications ✅
- **Brand reputation monitoring**: Detect positive or negative customer feedback quickly.  
- **Product feedback analysis**: Identify trends in user sentiment for improvements.  
- **Trend detection**: Spot spikes in positive or negative sentiment tied to events or campaigns.

### Tech Stack 🛠️
- **Python** – core programming language  
- **Pandas** – data manipulation  
- **Scikit-learn** – machine learning modeling  
- **Matplotlib** – data visualization  
- **Streamlit** – interactive app deployment  

### Key Learnings 💡
- Real-world data is messy, but careful preprocessing and cleaning unlock valuable insights.  
- Simple models with proper feature engineering can achieve impressive results.  
- Deploying interactive tools makes ML accessible and demonstrates practical value.

