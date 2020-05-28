def ft_map(function_to_apply, list_of_inputs):
    result = []
    for x in list_of_inputs:
        result.append(function_to_apply(x))
    return iter(result)


if __name__ == "__main__":
    text = ['Le', 'Lorem', 'Ipsum', 'est',
            'simplement', 'du', 'faux', 'texte.']
    test = list(ft_map(list, text))
    print(test)

    text = ['Le', 'Lorem', 'Ipsum', 'est',
            'simplement', 'du', 'faux', 'texte.']
    test = list(map(list, text))
    print(test)

    numbers = (1, 2, 3, 4)
    test = ft_map(lambda x: x + x, numbers)
    print(list(test))

    numbers = (1, 2, 3, 4)
    test = map(lambda x: x + x, numbers)
    print(list(test))
