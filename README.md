# 🎬 Netflix AI Movie Recommendation System

A Netflix-inspired Movie Recommendation System built using **Streamlit**, **Machine Learning**, and **Content-Based Filtering**. The application recommends similar movies based on movie descriptions and genres using **TF-IDF Vectorization** and **Cosine Similarity**.

## 🌐 Live Demo

**Live Project:** [https://netflix-movie-recommendation-system-zchaznts7bmkncwbsfpgjy.streamlit.app/]

---

## 📸 Project Preview

![Netflix AI Dashboard](Screenshot%202026-06-18%20223045.png)

---

## 🚀 Features

| Feature                  | Description                              |
| ------------------------ | ---------------------------------------- |
| 🎬 Movie Recommendations | Recommends similar movies instantly      |
| ⭐ Ratings                | Displays movie ratings                   |
| 🖼️ Movie Posters        | Shows movie posters with recommendations |
| 📅 Release Date          | Displays release year/date               |
| 📝 Movie Overview        | Brief movie description                  |
| 🌙 Netflix Theme         | Professional Netflix-inspired dark UI    |
| 🤖 Machine Learning      | TF-IDF + Cosine Similarity Algorithm     |

---

## 🛠️ Tech Stack

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python            | Programming Language      |
| Streamlit         | Web Application Framework |
| Pandas            | Data Processing           |
| Scikit-Learn      | Machine Learning          |
| TF-IDF            | Feature Extraction        |
| Cosine Similarity | Recommendation Engine     |

---

## 📂 Project Structure

```text
NetflixAI/
│
├── app.py
├── movies.csv
├── poster.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📊 Dataset Information

| File       | Description                              |
| ---------- | ---------------------------------------- |
| movies.csv | Movie details, ratings, genres, overview |
| poster.csv | Movie poster URLs                        |

---

## 🎯 Recommendation Logic

1. Movie Overview & Genres Combined
2. TF-IDF Vectorization Applied
3. Cosine Similarity Calculated
4. Top Similar Movies Recommended

---

## 🔗 Repository

```bash
git clone [https://github.com/palaktonke06-a11y/Netflix-Movie-Recommendation-System.git]
```

Open the project folder:

```bash
cd Netflix Movie Recommendation System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

