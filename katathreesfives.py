def solution(number):
    """
    Return the sum of all multiples of three or five below the number passed.  Assumes
    :param number: natural number
    :return: natural number
    """
    # Create a list of multiples of three or five below the number passed.
    # First, the multiples of three ...
    debug = False
    assert isinstance(number, int), 'number passed is not int'
    assert number > 0, 'number passed is not a natural number'
    terms = []
    for i in range(number):
        if i%3 == 0:
            terms.append(i)
    # ... then the multiples of five that aren't already a multiple of three
    for i in range(number):
        if i%5 == 0 and i%3 !=0:
            terms.append(i)
    if debug: print(terms)
    # Sum the list of terms
    sum = 0
    for term in terms:
        sum += term
    return sum

if __name__ == '__main__':
    debug = True
    testnum = int(input('Input test num: '))
    print(solution(testnum))