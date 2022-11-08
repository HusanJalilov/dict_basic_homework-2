
def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    n = list(people)
    as1 = list(people.values())
    mx = max(as1)
    ix = as1.index(mx)

    
    return n[ix]
    
print(oldest({"Javohir": 22, "Sharof": 23, "Tolib": 34, "Rustam": 16}))