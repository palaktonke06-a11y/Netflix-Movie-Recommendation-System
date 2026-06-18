import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="Netflix AI",
    page_icon="🎬",
    layout="wide"
)

# ====================================
# NETFLIX THEME
# ====================================

st.markdown("""
<style>

.stApp{
    background-color:#141414;
}

h1,h2,h3,h4,h5,h6,p,label{
    color:white !important;
}

.stButton > button{
    background-color:#E50914;
    color:white;
    border:none;
    border-radius:10px;
    padding:10px 20px;
    font-weight:bold;
}

.stButton > button:hover{
    background-color:#B20710;
}

</style>
""", unsafe_allow_html=True)

# ====================================
# LOAD DATA
# ====================================

@st.cache_data
def load_data():

    movies = pd.read_csv("movies.csv")
    poster = pd.read_csv("poster.csv")

    movies.columns = movies.columns.str.strip()
    poster.columns = poster.columns.str.strip()

    movies["overview"] = movies["overview"].fillna("")
    movies["genres"] = movies["genres"].fillna("")

    merged = pd.merge(
        movies,
        poster,
        on="title",
        how="left"
    )

    merged["combined_features"] = (
        merged["overview"] + " " +
        merged["genres"].astype(str)
    )

    return merged

df = load_data()

# ====================================
# TF-IDF MODEL
# ====================================

@st.cache_resource
def build_similarity():

    tfidf = TfidfVectorizer(
        stop_words="english"
    )

    matrix = tfidf.fit_transform(
        df["combined_features"]
    )

    similarity = cosine_similarity(matrix)

    return similarity

similarity = build_similarity()

# ====================================
# RECOMMENDATION FUNCTION
# ====================================

def recommend(movie):

    idx = df[
        df["title"].str.lower()
        == movie.lower()
    ].index[0]

    scores = list(
        enumerate(similarity[idx])
    )

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    scores = scores[1:7]

    movie_indices = [
        i[0]
        for i in scores
    ]

    return df.iloc[movie_indices]

# ====================================
# HEADER
# ====================================

st.markdown("""
<h1 style='text-align:center;color:#E50914'>
🎬 NETFLIX AI
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h4 style='text-align:center'>
Movie Recommendation System
</h4>
""", unsafe_allow_html=True)

# Banner
st.image(
    "https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85",
    use_container_width=True
)

st.write("")

# ====================================
# SIDEBAR
# ====================================

st.sidebar.title("📊 Dashboard")

st.sidebar.write(
    f"Total Movies : {len(df)}"
)

# ====================================
# TOP MOVIES
# ====================================

st.subheader("🔥 Top Rated Movies")

top_movies = (
    df.sort_values(
        by="vote_average",
        ascending=False
    )
    .head(10)
)

st.dataframe(
    top_movies[
        ["title", "vote_average"]
    ],
    use_container_width=True
)

# ====================================
# SEARCH MOVIE
# ====================================

movie_list = sorted(
    df["title"]
    .dropna()
    .unique()
)

selected_movie = st.selectbox(
    "🔍 Search Movie",
    movie_list
)

# ====================================
# RECOMMEND BUTTON
# ====================================

if st.button("🎬 Recommend Movies"):

    recommendations = recommend(
        selected_movie
    )

    st.subheader(
        "Recommended Movies"
    )

    for _, row in recommendations.iterrows():

        col1, col2 = st.columns([1,3])

        with col1:

            poster_url = row["poster"]

            if (
                pd.notna(poster_url)
                and str(poster_url).strip() != ""
                and str(poster_url).startswith("http")
            ):

                st.image(
                    poster_url,
                    width=220
                )

            else:

               st.image(
    "https://dummyimage.com/220x330/141414/ffffff.png&text=No+Poster+Available",
    width=220
)
        with col2:

            st.markdown(
                f"## 🎬 {row['title']}"
            )

            st.markdown(
                f"⭐ Rating: {row['vote_average']}/10"
            )

            st.markdown(
                f"📅 Release Date: {row['release_date']}"
            )

            st.write(
                row["overview"]
            )

        st.markdown("---")

# ====================================
# FOOTER
# ====================================

st.markdown("---")

st.markdown(
"""
<center>
Made with ❤️ using Streamlit & Machine Learning
</center>
""",
unsafe_allow_html=True
)
