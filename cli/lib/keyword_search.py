
def keyword_search(movies, query):
    result = []
    for movie in movies["movies"]:
        if query in movie["title"]:
            result.append(movie["title"])

    return result
