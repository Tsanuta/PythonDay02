def ft_filter(function_to_apply, list_of_inputs):
    result = []
    for x in list_of_inputs:
        if function_to_apply(x) != 0:
            result.append(x)
    return iter(result)


if __name__ == "__main__":
    # a list contains both even and odd numbers.
    seq = [0, 1, 2, 3, 5, 8, 13]

    # result contains odd numbers of the list
    result = ft_filter(lambda x: x % 2, seq)
    print(list(result))

    result = filter(lambda x: x % 2, seq)
    print(list(result))

    # result contains even numbers of the list
    result = ft_filter(lambda x: x % 2 == 0, seq)
    print(list(result))

    result = filter(lambda x: x % 2 == 0, seq)
    print(list(result))
