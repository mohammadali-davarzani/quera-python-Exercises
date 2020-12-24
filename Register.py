def check_registration_rules(**kwargs):

    confirmed_names = list()
    for i in kwargs:
        if (len(i) >= 4) and (i != "quera") and (i != "codecup") and (len(kwargs[i]) >= 6) and (kwargs[i].isdigit() == False):
            confirmed_names.append(i)

    return confirmed_names



