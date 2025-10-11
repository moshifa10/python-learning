

# Challange 10

''''
    Challange 10B: Movie Rating Analyzer
    Goal:
        Analyze movie ratings from multiple viewers and find insights like:
            1. Which movie has the highest average rating
            2. Which users gave the most ratings
            3. And a summary of how many ratings each movie received
    Example:
        Input:
            data = [
                {"user": "Njabulo", "movie": "Inception", "rating": 8.5},
                {"user": "Alice", "movie": "Inception", "rating": 9.0},
                {"user": "Bob", "movie": "Matrix", "rating": 8.7},
                {"user": "Njabulo", "movie": "Matrix", "rating": 9.1},
                {"user": "Alice", "movie": "Avatar", "rating": 7.5},
                {"user": "Bob", "movie": "Avatar", "rating": 8.0},
                {"user": "Njabulo", "movie": "Avatar", "rating": 8.2}
            ]
        Output:
                {
                "average_ratings": {
                    "Inception": 8.75,
                    "Matrix": 8.9,
                    "Avatar": 7.9
                },
                "most_rated_movie": "Avatar",
                "top_rated_movie": "Matrix",
                "most_active_user": "Njabulo"
                }

'''
data = [
    {"user": "Njabulo", "movie": "Inception", "rating": 8.5},
    {"user": "Alice", "movie": "Inception", "rating": 9.0},
    {"user": "Bob", "movie": "Matrix", "rating": 8.7},
    {"user": "Njabulo", "movie": "Matrix", "rating": 9.1},
    {"user": "Alice", "movie": "Avatar", "rating": 7.5},
    {"user": "Bob", "movie": "Avatar", "rating": 8.0},
    {"user": "Njabulo", "movie": "Avatar", "rating": 8.2}
]
def movie_analyzer(data: list[dict]) -> dict:
    data_analyzer = {}
    names = []
    top_rated = 0
    top_rated_movie = ""
    movie_ratings = {}
    average_rating = {}
    movies_names = []
    for i in data:
        user, movie, rating = i["user"], i["movie"], i["rating"]
        names.append(user)
        if rating > top_rated:
            top_rated = rating
            top_rated_movie = movie
        if movie not in movie_ratings.keys():
            movie_ratings[movie] = rating
        else:
            movie_ratings[movie] += rating
        movies_names.append(movie)
 
    count = 0
    most_active_user = ""
    for i in names:
        if names.count(i) > count:
            count = names.count(i)
            most_active_user = i
    movie_count =0
    most_rated= ''
    for movie, value in  movie_ratings.items():
        if value > movie_count:
            movie_count = value
            most_rated = movie
        if movie in average_rating.keys():
            continue
        else:
            count = movies_names.count(movie)
            average_rating[movie] = round((value / count), 2)
        
    data_analyzer["avarage_ratings"] = average_rating
    data_analyzer["most_rated_movie"] = most_rated
    data_analyzer["top_rated_movie"] = top_rated_movie
    data_analyzer["most_active_user"] = most_active_user
    print(data_analyzer)

    # print(top_rated_movie)
    print(movie_ratings)
        
    return data_analyzer

movie_analyzer(data)