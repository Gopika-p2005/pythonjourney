movies = [
    {"title": "ABCD", "language": "Malayalam", "rating": 9, "year": 2011, "runtime": 120},
    {"title": "Vazha", "language": "Malayalam", "rating": 9, "year": 2022, "runtime": 140},
    {"title": "Kumbalangi Nights", "language": "Malayalam", "rating": 9, "year": 2019, "runtime": 135},
    {"title": "Super Deluxe", "language": "Tamil", "rating": 9, "year": 2019, "runtime": 176},
    {"title": "Jai Bhim", "language": "Tamil", "rating": 9, "year": 2021, "runtime": 164},
    {"title": "Parasite", "language": "Korean", "rating": 10, "year": 2019, "runtime": 132},
    {"title": "Spirited Away", "language": "Japanese", "rating": 10, "year": 2001, "runtime": 125},
    {"title": "The Godfather", "language": "English", "rating": 10, "year": 1972, "runtime": 175},
    {"title": "Inception", "language": "English", "rating": 9, "year": 2010, "runtime": 148},
    {"title": "Tumbbad", "language": "Hindi", "rating": 9, "year": 2018, "runtime": 104},
    {"title": "Dangal", "language": "Hindi", "rating": 9, "year": 2016, "runtime": 161},
    {"title": "Kantara", "language": "Kannada", "rating": 9, "year": 2022, "runtime": 148},
    {"title": "RRR", "language": "Telugu", "rating": 9, "year": 2022, "runtime": 187},
    {"title": "City of God", "language": "Portuguese", "rating": 10, "year": 2002, "runtime": 130},
    {"title": "Anatomy of a Fall", "language": "French", "rating": 9, "year": 2023, "runtime": 151}
]


all_title=[m["title"] for m in movies ]

print("movie title",all_title)

print("==============================")

all_language={m.get("language") for m in movies }#set comprehension

print("movie language",all_language)

print("=========================================")

all_malayalam_movies=[m["title"] for m in movies if m["language"]=="Malayalam" ]

print("malayalam movies",all_malayalam_movies)

print("==========================================================")

#movies released after 2005
movie_after_2005=[m["title"] for m in movies if m["year"]>2005 ]

print("movie released after 2005",movie_after_2005)

print("=============================================================")