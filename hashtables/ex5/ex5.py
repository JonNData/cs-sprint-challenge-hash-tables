# Your code here. huh??

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # TOOO SLOW!!!
    # put each into a dict and compare if query is in the filepath
    # file_dict = {}
    # for x in files:
    #     file_dict[x] = None

    # query_dict = {}
    # for query in queries:
    #     query_dict[query] = None

    # result = []

    # for query in query_dict:
    #     for x in file_dict:
    #         if query in x:
    #             result.append(x)

    # how abouts we just but the filenames from the full path into a dict
    # and then we can query that dict
    filepaths = {}
    for idx, value in enumerate(files):
        filename = value.rpartition("/")[2] # everything to the right of the slash
        filepaths[filename] = idx
    
    result = []
    for query in queries:
        if query in filepaths:
            idx = filepaths[query]
            result.append(files[idx])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
