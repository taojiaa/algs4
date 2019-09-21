def words_gen(fileobj):
    for line in fileobj:
        for word in line.split():
            yield word
