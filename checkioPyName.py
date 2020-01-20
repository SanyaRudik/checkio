def from_camel_case(name):
    s = ''
    for i in name:
        if name.index(i):
            if i.isupper():
                s += '_' + i.lower()
            else:
                s += i
        else:
            s += i.lower()
    return s


if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("MyFunctionName"))
    print(from_camel_case("IPhone"))
    print(from_camel_case("ThisFunctionIsEmpty"))
    print(from_camel_case("Name"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
