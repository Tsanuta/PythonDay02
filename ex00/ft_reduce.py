def ft_reduce(function_to_apply, list_of_inputs):
    result = list_of_inputs[0]
    x = 1
    while x < len(list_of_inputs):
        result = function_to_apply(result, list_of_inputs[x])
        x += 1
    return result


if __name__ == "__main__":
    # python code to demonstrate working of reduce()

    # importing functools for reduce()
    import functools

    # initializing list
    lis = [1, 3, 5, 6, 2]

    # using reduce to compute sum of list
    print("The sum of the list elements is : ", end="")
    print(ft_reduce(lambda a, b: a + b, lis))

    # using reduce to compute maximum element from list
    print("The maximum element of the list is : ", end="")
    print(ft_reduce(lambda a, b: a if a > b else b, lis))

    # python code to demonstrate working of reduce()
    # using operator functions

    # importing functools for reduce()
    import functools

    # importing operator for operator functions
    import operator

    # initializing list
    lis = [1, 3, 5, 6, 2]

    # using reduce to compute sum of list
    # using operator functions
    print("The sum of the list elements is : ", end="")
    print(ft_reduce(operator.add, lis))

    # using reduce to compute product
    # using operator functions
    print("The product of list elements is : ", end="")
    print(ft_reduce(operator.mul, lis))

    # using reduce to concatenate string
    print("The concatenated product is : ", end="")
    print(ft_reduce(operator.add, ["geeks", "for", "geeks"]))

    # python code to demonstrate summation
    # using reduce() and accumulate()

    # importing itertools for accumulate()
    import itertools

    # importing functools for reduce()
    import functools

    # initializing list
    lis = [1, 3, 4, 10, 4]

    # priting summation using accumulate()
    print("The summation of list using accumulate is :", end="")
    print(list(itertools.accumulate(lis, lambda x, y: x + y)))

    # priting summation using reduce()
    print("The summation of list using reduce is :", end="")
    print(ft_reduce(lambda x, y: x + y, lis))
