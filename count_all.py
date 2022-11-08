def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    h=0
    s=0
    for i in txt:
        if i.isdigit():
            s+=1
        if i.isalpha():
            h+=1
    return {"LETTERS":h,"DIGITS":s}
print(count_all("Hel22lo World"))