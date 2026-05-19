# 📊 Netflix Data Web App

A full-stack data-driven web application built with Django that demonstrates end-to-end data engineering, analytics, and machine learning. The project includes a data pipeline, interactive dashboards, REST API integration, and an XGBoost-based churn prediction model.

---

## 🚀 Features

## 📥 Data Pipeline
- Automated data transformation pipeline built with Python
- Imports, cleans, and structures raw datasets
- Loads processed data into a SQLite database using Django ORM

## 🧩 Full CRUD System
- Create, Read, Update, and Delete functionality
- Built using Django views, models, and templates
- Efficient database interaction through Django ORM

## 📊 Analytics Dashboard
- Interactive visualizations using Chart.js
- Displays churn statistics, user behavior, and system insights
- Dynamic charts driven by real database queries

## 🎬 TMDB API Integration
- Fetches Top Movies of the Week using The Movie Database (TMDB) API
- Displays real-time trending movie data
- Enhances the dashboard with external live content

## 🤖 Machine Learning (XGBoost Model)
- Churn prediction model built with XGBoost
- Predicts user churn based on:
  - Age
  - Country
  - Subscription type
  - Monthly fee
  - Device usage
  - Account age
- Integrated into Django for real-time predictions

---

## 🛠️ Tech Stack

### Backend
- Python
- Django
- SQLite
- Django ORM

### Data & Machine Learning
- Pandas
- NumPy
- Scikit-learn
- XGBoost

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js

### External APIs
- TMDB API (The Movie Database)

---

## 🔄 Data Pipeline

1. Raw data ingestion
2. Data cleaning & transformation (Pandas)
3. Feature engineering
4. Storage in SQLite via Django ORM
5. Model training (XGBoost)
6. Integration into Django prediction endpoint

---

## 📈 Dashboard Insights

- Churn rate by country
- User distribution across regions
- Subscription behavior trends
- Interactive pie and bar charts (Chart.js)

---

## 🎬 TMDB Integration

- Fetches weekly trending movies
- Displays live movie rankings
- Enhances user experience with external API data

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/manwillerc/Netflix-Data-Web-App.git
cd Netflix-Data-Web-App
