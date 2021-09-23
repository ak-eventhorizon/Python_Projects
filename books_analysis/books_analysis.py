def words_count_in_book(filename: str):
    """Counts words and words statistics in book"""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        print(f'File {filename} is not found')

    else:
        words = contents.split()
        num_words = len(words)
        print(f'Total words in {filename} is about {num_words}')

        words_analytic = {}

        for word in words:
            if word not in words_analytic:
                words_analytic[word] = 1
            else:
                words_analytic[word] += 1

        sorted_words_analytic = {}
        sorted_keys = sorted(words_analytic, key=words_analytic.get, reverse=True)

        for w in sorted_keys:
            sorted_words_analytic[w] = words_analytic[w]

        print(sorted_words_analytic)


if __name__ == '__main__':
    words_count_in_book('./books/alice.txt')
