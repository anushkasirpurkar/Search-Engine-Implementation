# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs
import os

from words import get_text, words


def linear_search(files, terms):
    """
    Given a list of fully-qualified filenames, return a list of them
    whose file contents has all words in terms as normalized by your words() function.
    Parameter terms is a list of strings.
    Perform a linear search, looking at each file one after the other.
    """

    count_terms = len(terms)
    term_file_occurence = []
    for file_name in files:
        file = get_text(file_name)
        file_word_list = words(file)
        # print(file)
        found = 0
        for term in terms:
            if term in file_word_list:
                # print("Found")
                found += 1
        if found == count_terms:
            term_file_occurence.append(file_name)
        # break
    return term_file_occurence
