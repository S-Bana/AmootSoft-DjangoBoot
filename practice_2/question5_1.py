def generate_all_subsets(input_list, current_index=0):
    """
    This function uses recursion to generate all subsets of the input list.
    It includes both the subsets that contain the current element and those that don't.

    Args:
    input_list (list): The list for which to generate subsets.
    current_index (int): The current index being processed (used for recursion).

    Returns:
    list: A list of all possible subsets, where each subset is represented as a list.

    Example:
    in:
    [1, 2, 3]
    out:
    [[1, 2, 3], [1, 2], [1, 3],[2, 3], [1], [2], [3], []]
    """
    if current_index == len(input_list):
        return [[]]
    
    # Generate subsets without the current element
    subsets_without_current = generate_all_subsets(input_list, current_index + 1)
    
    # Generate subsets with the current element
    subsets_with_current = [
        [input_list[current_index]] + subset 
        for subset in subsets_without_current
    ]
    
    # Combine and return all subsets
    return subsets_with_current + subsets_without_current


# Example usage
sample_list = [1, 2, 3]
print(f"input: {sample_list}")
all_subsets = generate_all_subsets(sample_list)
print(f"output: {all_subsets}")

        