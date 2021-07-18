"""
Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}

You can assume keys do not contain dots in them, i.e. no clobbering will occur.

"""

test = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

# Recursively flatten a dictionary
def flatten(parent_key, child_dict, result):
    for nkey, nval in child_dict.items():
        new_key = ".".join([parent_key, nkey])
        if isinstance(nval, dict):
            flatten(new_key, nval, result)
        else:
            result[new_key] = nval


def main():
    result = {}
    # Iterate and flatten the dictionary
    for key, val in test.items():
        if isinstance(val, dict):
            flatten(key, val, result)
        else:
            result[key] = val
    print (result)


if __name__ == '__main__':
    main()