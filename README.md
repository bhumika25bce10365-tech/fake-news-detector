## Version 1.0
# Fake News Detector

## Problem
Fake news spreads misinformation and is difficult to identify manually.

## Solution
This project uses Machine Learning (TF-IDF + Logistic Regression) to classify news as fake or real.

## Features
- Input news text
- Predict fake or real
- Simple web interface

## Tech Stack
- Python
- Scikit-learn
- Flask

## How to Run
1. Install dependencies
2. Run train.py
3. Run app.py

## Results
Achieved ~95% accuracy

## Future Work
- Improve NLP model
- Add deep learning

## Version 2.0
# Fake News Detection System

## Overview

This project focuses on detecting whether a news article is **real or fake** using basic machine learning techniques. The goal was to take a real-world problem — the spread of misinformation — and build a simple, usable solution around it.

The model is trained on a labeled dataset of news articles and then integrated into a web application where users can input text and get predictions instantly.

---

## Problem Statement

With the increasing use of social media, fake news spreads quickly and can influence public opinion. Manually verifying news is time-consuming, so this project attempts to automate that process using machine learning.

---

## Approach

### 1. Data Processing

* Used a dataset containing real and fake news articles
* Cleaned and combined text data
* Converted text into numerical form using **TF-IDF Vectorization**

### 2. Model Building

* Trained a **Logistic Regression** model
* Focused on simplicity and interpretability rather than complexity

### 3. Web Application

* Built a simple interface using **Flask**
* Users can input news content and get predictions in real time

---

## Project Structure

```
fake-news-detector/
│
├── data/                # Dataset files (not included in repo due to size)
├── model/               # Saved model and vectorizer
├── templates/           # HTML files for UI
├── app.py               # Flask application
├── train.py             # Model training script
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/bhumika25bce10365-tech/fake-news-detector.git
cd fake-news-detector
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

### 4. Open in browser

Go to:

```
http://127.0.0.1:5000/
```

---

## Features

* Predicts whether news is **Real or Fake**
* Simple and clean user interface
* Fast predictions using a trained model
* Easy to run locally

---

## Challenges Faced

* Handling large dataset files and GitHub size limits
* Cleaning text data effectively
* Connecting the ML model with the web interface

---

## What I Learned

* Basics of text preprocessing and vectorization
* How machine learning models work in real-world applications
* Building and deploying a simple Flask app
* Managing a project using Git and GitHub

---

## Future Improvements

* Use more advanced models (like LSTM or Transformers)
* Improve accuracy with better preprocessing
* Deploy the app online for public use

---

## Conclusion

This project demonstrates how machine learning can be applied to a real-world problem in a simple and practical way. While the model is basic, it provides a foundation that can be improved and expanded further.

---
