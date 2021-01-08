def decorator(validator):
    def type_checker(func):
        def ret(*args):
            if validator(*args) != True:
                return "error"
            else:
                return func(*args)
        return ret
    return type_checker
