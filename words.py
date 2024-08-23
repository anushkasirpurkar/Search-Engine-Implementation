import os
import re
import string
import sys

# print(os.getcwd())
# print(sys.argv[1])
root = os.path.join(os.getcwd(), sys.argv[1])
# root = sys.argv[1]
# print(root)


def filelist(root):
    """Return a fully-qualified list of filenames under root directory"""
    final_file_list = []
    i = 0
    for i, x in enumerate(os.walk(root)):
        # print('\n',i)
        # print(x)
        for item in x[2]:
            if not item.startswith('.') and item.endswith('txt'):
                final_file_list.append(os.path.join(x[0], item))
    # print((final_file_list))
    return final_file_list


def get_text(fileName):
    f = open(fileName, encoding='latin-1')
    s = f.read()
    f.close()
    return s


def words(text):
    """
    Given a string, return a list of words normalized as follows.
    Split the string to make words first by using regex compile() function
    and string.punctuation + '0-9\\r\\t\\n]' to replace all those
    char with a space character.
    Split on space to get word list.
    Ignore words < 3 char long.
    Lowercase all words
    """
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    nopunct = regex.sub(" ", text)  # delete stuff but leave at least a space to avoid clumping together
    words = nopunct.split(" ")
    words = [w for w in words if len(w) > 2]  # ignore a, an, to, at, be, ...
    words = [w.lower() for w in words]
    # print words
    return words


def results(docs, terms):
    """
    Given a list of fully-qualifed filenames, return an HTML file
    that displays the results and up to 2 lines from the file
    that have at least one of the search terms.
    Return at most 100 results.  Arg terms is a list of string terms.
    """
    ndocs = len(docs)
    docs = docs[0:100]  # at most 100 results
    terms = set(terms)
    body = ""
    for f in docs:
        lines = get_text(f).split("\n")
        summary = ""
        n = 0
        for line in lines:
            if n>2: break # show 2 lines at most
            line_words = words(line)
            if set(line_words).intersection(terms):
                for w in line_words:
                    summary += " "
                    if w in terms:
                        # summary += f"<font color=#41b6c4>{w}</font>"
                        summary += f"<b>{w}</b>"
                    else:
                        summary += w
                summary += "<br>"
                n+=1
        result = """
        <p><a href="file://%s">%s</a><br>
        %s<br>
        """ % (f, f, summary)
        body += result
    return """
    <html>
    <body>
    <h2>Search results for <b>%s</b> in %d files</h2>
    %s
    </body>
    </html>
    """ % (" ".join(terms),ndocs,body)


def filenames(docs):
    """Return just the filenames from list of fully-qualified filenames"""
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]


(filelist(root))
# print(text)
# print(words(get_text(file_name)))
