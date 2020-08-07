def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # need to sort index descending or just use max and min
    dictionary = {idx: value for idx, value in enumerate(weights)}
    for i in range(length):
        for j in range(i + 1, length):
            if dictionary[i] + dictionary[j] == limit:
                return (max(i,j), min(i,j))

