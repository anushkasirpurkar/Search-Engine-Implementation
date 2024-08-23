# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from htable import *
from words import get_text, words


def myhtable_create_index(files):
    """
    Build an index from word to set of document indexes
    This does the exact same thing as create_index() except that it uses
    your htable.  As a number of htable buckets, use 4011.
    Returns a list-of-buckets hashtable representation.
    """
    n = 4011
    buckets = htable(n)

    for file_name in files:
        file = get_text(file_name)
        file_word_list = words(file)

        for word in file_word_list:

            if htable_get(buckets, word) is None:
                htable_put(buckets, word, {files.index(file_name)})
            else:
                tup1 = htable_get(buckets, word)
                tup1.add(files.index(file_name))
                if files.index(file_name) in tup1:
                    # print("YES")
                    continue
                htable_put(buckets, word, {files.index(file_name)})
                # break
        # break
    # print(buckets)

    return buckets


def myhtable_index_search(files, index, terms):
    """
    This does the exact same thing as index_search() except that it uses your htable.
    I.e., use htable_get(index, w) not index[w].
    """
    term_file_occurence = []
    term_indexes = []

    found = 0
    flag_found = False
    for term in terms:
        if htable_get(index, term) is None:
            return []
        else:
            tup = htable_get(index, term)
            term_indexes.append(list(tup))
            # print(term_indexes)

    common_files = (set.intersection(*map(set, term_indexes)))

    for i in common_files:
        term_file_occurence.append(files[i])
    # print((term_file_occurence))
    return term_file_occurence
