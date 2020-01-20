def flatten(dictionary):
    """Flatten a dictionary.
    If the dict is already flat, there is nothing to do.
    For flatten a dict, we look each value of the dictionary.
        If the value is a string, we copy it in D.
        If the value is a empty dict, this must be replaced by a empty string '' in D.
        Else the value is a non empty dict, we flatten this dict value before integrate it into D.
    """
    if all(type(v) is str for v in dictionary.values()):
        return dictionary
    D = {}
    for key in dictionary.keys():
        if isinstance(dictionary[key],str):
            D[key] = dictionary[key]
        elif dictionary[key] == {}:
            D[key] = ''
        else:
            E = flatten(dictionary[key])
            for keyE in E:
                D[key+'/'+keyE] = E[keyE]
    return D
def flatten_no(dictionary):
    for i in dictionary:
        print(dictionary[i])
        if isinstance(dictionary[i],str):
            pass
            # print(dictionary[i])
        elif dictionary[i] == {}:
            print('none')
            pass
        else:
            print(dictionary[i])
            flatten(dictionary[i])


if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    # print(' Input: {}'.format(test_input))
    # print('Output: {}'.format(flatten(test_input)))

    # print(flatten({"key": "value"}))  # == {"key": "value"}, "Simple"
    # print(flatten({"key": {"deeper": {"more": {"enough": "value"}}}}))  # == {"key/deeper/more/enough": "value"}, "Nested"
    # print(flatten({"empty": {}}))  # == {"empty": ""}, "Empty value"
    print(flatten({"name": {
        "first": "One",
        "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"}}}
    ))  # == {
    # "name/first": "One",
    # "name/last": "Drone",
    # "job": "scout",
    # "recent": "",
    # "additional/place/zone": "1",
    # "additional/place/cell": "2"}
