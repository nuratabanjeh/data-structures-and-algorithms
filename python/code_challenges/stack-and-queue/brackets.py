import re
def validate_brackets(input):
    value=False
    if input.count('{')==input.count('}') and input.count('(')==input.count(')') and \
        input.count('[')==input.count(']'):
        value=True
    try :
        if re.search("\(.?}", input) or re.search("\[.?}", input) or \
            re.search("\[.?)", input) or re.search("\(.?]", input) or \
            re.search("\{.?)", input) or re.search("\{.?]", input):
            value=False
    except:
        return value
    return value


print(validate_brackets('{}'))
print(validate_brackets('{}(){}'))
print(validate_brackets('()[[nura]]'))
print(validate_brackets('(){}[[]]'))
print(validate_brackets('{}{nura}[tabanjehhh](())'))
print(validate_brackets('[({}]'))
print(validate_brackets('(]('))
print(validate_brackets('{(})'))
print(validate_brackets('{'))
print(validate_brackets(')'))
print(validate_brackets('[}'))