"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""


def htable(nbuckets):
    """Return a list of nbuckets lists"""
    buckets = [[] for i in range(nbuckets)]
    return buckets


def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """
    h = 0
    if str(o).isnumeric():
        return int(o)

    for i in o:
        h = (h * 31) + ord(i)
    return h


def bucket_indexof(table, key):
    """
    You don't have to implement this, but I found it to be a handy function.
    Return the index of the element within a specific bucket; the bucket is:
    table[hashcode(key) % len(table)]. You have to linearly
    search the bucket to find the tuple containing key.
    """
    bucket_index = hashcode(key) % len(table)
    return bucket_index


def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value
    Find the appropriate bucket indicated by key and then append (key,value)
    to that bucket if the (key,value) pair doesn't exist yet in that bucket.
    If the bucket for key already has a (key,value) pair with that key,
    then replace the tuple with the new (key,value).
    Make sure that you are only adding (key,value) associations to the buckets.
    The type(value) can be anything. Could be a set, list, number, string, anything!
    """

    bucket_index = bucket_indexof(table, key)
    bucket = table[bucket_index]
    flag_found = False
    for i, list1 in enumerate(bucket):
        # print("IN FOR")
        # print(list1)
        if key == list1[0]:
            # print("YES")
            bucket[i] = (key, value)
            flag_found = True
    if not flag_found:
        bucket.append((key, value))


def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """

    bucket_index = bucket_indexof(table, key)
    bucket = table[bucket_index]

    for i, tup in enumerate(bucket):
        if tup[0] == key:
            return tup[1]
    return None


def htable_buckets_str(table):
    """
    Return a string representing the various buckets of this table.
    The output looks like:
        0000->
        0001->
        0002->
        0003->parrt:99
        0004->
    where parrt:99 indicates an association of (parrt,99) in bucket 3.
    """
    str_final = ""
    start, stop = "", ""

    for i, list1 in enumerate(table):
        # print(list1)
        str_line = ""
        if len(list1) == 0:
            str_final += str(i).zfill(4) + "->" + "\n"
            continue
        str_final += str(i).zfill(4) + "->"
        for k, list2 in enumerate(list1):
            str_line += str(list2[0]) + ':' + str(list2[1]) + ', '
        str_final += str_line[:-2] + '\n'

    # print(str_final)
    return str_final


def htable_str(table):
    """
    Return what str(table) would return for a regular Python dict
    such as {parrt:99}. The order should be in bucket order and then
    insertion order within each bucket. The insertion order is
    guaranteed when you append to the buckets in htable_put().
    """
    dict_str = ""
    start, stop = "{", "}"

    for i, list1 in enumerate(table):
        if len(list1) == 0:
            continue
        # print(list1[0])
        for k, list2 in enumerate(list1):
            # print(k)
            dict_str += str(list2[0]) + ':' + str(list2[1]) + ', '
    print(start + dict_str[0:-2] + stop)
    return start + dict_str[0:-2] + stop


table = htable(5)
for i in range(1, 11):
    htable_put(table, i, i)
s = htable_buckets_str(table)
# print(s)
