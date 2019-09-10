def FrequencyCounter(file_name, st, min_len=8):
    with open(file_name, 'r') as file:
        for line in file:
            for word in line.split():
                if len(word) < min_len:
                    continue
                if st.contains(word):
                    st.put(word, st.get(word) + 1)
                else:
                    st.put(word, 1)
    max_word = ''
    st.put(max_word, 0)
    for key in st.keys():
        if st.get(key) > st.get(max_word):
            max_word = key
    print(f'The frequency of {max_word} is {st.get(max_word)}')
