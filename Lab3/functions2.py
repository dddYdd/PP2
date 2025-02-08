movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

#1
def is_imdb_above_5_5(movie):
    return movie["imdb"] > 5.5

#2
def get_movies_above_5_5():
    return [movie for movie in movies if is_imdb_above_5_5(movie)]

#3
def get_movies_by_category(category):
    return [movie for movie in movies if movie["category"] == category]

#4
def average_imdb_score():
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)

#5
def average_imdb_score_by_category(category):
    category_movies = get_movies_by_category(category)
    if not category_movies:
        return 0
    total_score = sum(movie["imdb"] for movie in category_movies)
    return total_score / len(category_movies)

print("Movies with IMDB above 5.5:", get_movies_above_5_5())
print("Movies in Romance category:", get_movies_by_category("Romance"))
print("Average IMDB score of all movies:", average_imdb_score())
print("Average IMDB score of Romance movies:", average_imdb_score_by_category("Romance"))
