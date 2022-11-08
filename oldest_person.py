def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    # """
    return f"\"{max(people)}\""
    # s=[]
    # for i in people:
    #     s.append(people[i])
    #     # print(j)
    # m=max(s)
    # for i in people:
    #     if people[i]==m:
    #         return people[i]
print(oldest({"Javohir": 22, "Sharof": 23, "Tolib": 34, "Rustam": 16}))