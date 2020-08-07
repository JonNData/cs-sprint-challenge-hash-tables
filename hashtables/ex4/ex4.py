def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # hmm what if we just make a dictionary with a positive version of each,
    # compare and list differences 
    signtionary = {}
    pos_only = {}
    for number in a:
        signtionary[number] = 1 # doesn't matter what value
    for i in a:
        pos_only[abs(i)] = 1
    
    result = []
    for pos in pos_only: # look through pos numbers and compare to all.
        if pos != 0: # 0 breaks pos and negatives
            if -1*pos in signtionary and pos in signtionary:
                result.append(pos)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
