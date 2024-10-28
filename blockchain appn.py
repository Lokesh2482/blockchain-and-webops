def my_flatten(nested_list):
    result = []
    for element in nested_list:
        if isinstance(element, list):
            result.extend(my_flatten(element))  # Recursively flatten nested lists
        else:
            result.append(element)
    return result

# Example usage
print(my_flatten([1, [2, [3, [4, 5]], 6], 7]))  # Output: [1, 2, 3, 4, 5, 6, 7]
