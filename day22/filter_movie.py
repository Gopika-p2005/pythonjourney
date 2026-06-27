movies={
    "kgf":10,
    "arm":9,
    "abcd":7,
    "bahubali":9,
    "vazha1":8,
    "vazha2":10
}

filter_movie=[k for k,v in movies.items() if v>8]

print(filter_movie)