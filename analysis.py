"""
analyze_movielens.py
---------------------------------
Preliminary analysis for MovieLens 25M dataset
Project: Optimizing Diversity in Recommendation Systems with Privacy-Safe Content Modeling
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ===========================
# Basic Config
# ===========================
DATA_PATH = "Dataset/ml-25m"
OUTPUT_PATH = "results"
os.makedirs(OUTPUT_PATH, exist_ok=True)

sns.set(style="whitegrid")

# ===========================
# Load Data
# ===========================
print("📥 Loading MovieLens 25M dataset...")

ratings = pd.read_csv(os.path.join(DATA_PATH, "ratings.csv"))
movies = pd.read_csv(os.path.join(DATA_PATH, "movies.csv"))
tags = pd.read_csv(os.path.join(DATA_PATH, "tags.csv"))

print("✅ Data loaded successfully!")
print(f"Ratings shape: {ratings.shape}")
print(f"Movies shape:  {movies.shape}")
print(f"Tags shape:    {tags.shape}")

# ===========================
# Basic Stats
# ===========================
n_users = ratings["userId"].nunique()
n_movies = ratings["movieId"].nunique()
print(f"\n📊 Basic Statistics:")
print(f" - Unique users:  {n_users:,}")
print(f" - Unique movies: {n_movies:,}")
print(f" - Total ratings: {len(ratings):,}")

# ===========================
# Rating Distribution
# ===========================
plt.figure(figsize=(6, 4))
sns.histplot(ratings["rating"], bins=9, kde=False, color="skyblue")
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "rating_distribution.png"))
plt.close()

# ===========================
# Movie Popularity
# ===========================
movie_stats = (
    ratings.groupby("movieId")["rating"]
    .agg(["mean", "count"])
    .reset_index()
    .merge(movies, on="movieId", how="left")
)

plt.figure(figsize=(6, 4))
sns.histplot(movie_stats["count"], bins=100, color="salmon")
plt.xscale("log")
plt.title("Movie Popularity (Ratings per Movie)")
plt.xlabel("Number of Ratings (log scale)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "movie_popularity.png"))
plt.close()

# ===========================
# Genre Diversity per User
# ===========================
movies["genres"] = movies["genres"].fillna("(no genres listed)")
movies["genres_list"] = movies["genres"].apply(lambda x: x.split("|"))

user_movie = ratings.merge(movies[["movieId", "genres_list"]], on="movieId", how="left")
user_genre = user_movie.explode("genres_list")

user_genre_counts = (
    user_genre.groupby(["userId", "genres_list"])
    .size()
    .reset_index(name="count")
)

def shannon_entropy(counts):
    probs = counts / counts.sum()
    return -np.sum(probs * np.log2(probs))

user_entropy = (
    user_genre_counts.groupby("userId")["count"]
    .apply(shannon_entropy)
    .reset_index()
)
user_entropy.columns = ["userId", "genre_entropy"]

plt.figure(figsize=(6, 4))
sns.histplot(user_entropy["genre_entropy"], bins=40, color="seagreen")
plt.title("User Genre Diversity (Shannon Entropy)")
plt.xlabel("Entropy")
plt.ylabel("Number of Users")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "user_genre_entropy.png"))
plt.close()

avg_entropy = user_entropy["genre_entropy"].mean()
print(f"\n🎭 Average user genre entropy: {avg_entropy:.3f}")

# ===========================
# Global Genre Distribution
# ===========================
genre_counts = user_genre["genres_list"].value_counts()
genre_distribution = genre_counts / genre_counts.sum()

plt.figure(figsize=(8, 5))
sns.barplot(x=genre_distribution.index, y=genre_distribution.values, color="cornflowerblue")
plt.xticks(rotation=45, ha="right")
plt.title("Global Genre Distribution")
plt.ylabel("Proportion of Ratings")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "global_genre_distribution.png"))
plt.close()

# ===========================
# Save Summary
# ===========================
summary = {
    "n_users": n_users,
    "n_movies": n_movies,
    "total_ratings": len(ratings),
    "average_genre_entropy": avg_entropy,
}

summary_df = pd.DataFrame([summary])
summary_df.to_csv(os.path.join(OUTPUT_PATH, "summary_stats.csv"), index=False)

print("\n✅ Analysis complete! Results saved in 'results/' folder.")
