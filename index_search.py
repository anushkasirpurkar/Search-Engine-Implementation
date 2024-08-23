from collections import defaultdict  # https://docs.python.org/2/library/collections.html

from words import get_text, words


def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document IDs. A document ID is just the index into the
    files parameter (indexed from 0) to get the file name. Make sure that
    you are mapping a word to a set of doc IDs, not a list.
    For each word w in file i, add i to the set of document IDs containing w
    Return a dict object mapping a word to a set of doc IDs.
    """

    indexes = [files.index(file) for file in files]
    dict1 = {}

    for file_name in files:
        file = get_text(file_name)
        file_word_list = words(file)

        for word in file_word_list:
            if word not in dict1.keys():
                dict1[word] = {files.index(file_name)}
            else:
                dict1[word].add(files.index(file_name))
    return dict1


def index_search(files, index, terms):
    """
    Given an index and a list of fully-qualified filenames, return a list of
    filenames whose file contents has all words in terms parameter as normalized
    by your words() function.  Parameter terms is a list of strings.
    You can only use the index to find matching files; you cannot open the files
    and look inside.
    """

    count_terms = len(terms)
    term_file_occurence = []
    term_indexes = []

    found = 0
    for term in terms:
        if term not in index.keys():
            return []

        term_indexes.append(index[term])

    # print(term_indexes)
    common_files = (set.intersection(*map(set, term_indexes)))

    for i in common_files:
        term_file_occurence.append(files[i])
    # print(len(term_file_occurence))
    return term_file_occurence
