"""EPI 24.28: Compute the maximum subarray sum in a circular array, printed page 390.

Educational reconstruction, not a verbatim transcription. Algorithm: Max of normal Kadane subarray sum and total minus minimum subarray sum, except all-negative case.
The corresponding chapter's exercise Markdown retains the PDF text-layer
explanations, question and variants (with known OCR mistakes).

Run: python -m epi_python.chapter_24_honors_class.pg_390_max_subarray_sum_in_circular_array
Tests: python -m pytest tests/chapter_24_honors_class/test_pg_390_max_subarray_sum_in_circular_array.py -v
"""

def max_subarray_sum_in_circular_array(values: list[int]) -> int:
    """Maximum sum of a nonempty subarray, including circular wraparound."""
    if not values:
        return 0
    total=0
    max_end=max_so_far=values[0]
    min_end=min_so_far=values[0]
    for index,value in enumerate(values):
        total+=value
        if index:
            max_end=max(value,max_end+value)
            max_so_far=max(max_so_far,max_end)
            min_end=min(value,min_end+value)
            min_so_far=min(min_so_far,min_end)
    if max_so_far<0:
        return max_so_far
    return max(max_so_far,total-min_so_far)

if __name__ == "__main__":
    # Executable demonstration cases; pytest has the full set.
    result=max_subarray_sum_in_circular_array([])
    print('max_subarray_sum_in_circular_array', result)
    assert result == 0
    result=max_subarray_sum_in_circular_array([1, 2, -4, 3])
    print('max_subarray_sum_in_circular_array', result)
    assert result == 6
    result=max_subarray_sum_in_circular_array([-2, -1, -5])
    print('max_subarray_sum_in_circular_array', result)
    assert result == -1
    result=max_subarray_sum_in_circular_array([5, -3, 5])
    print('max_subarray_sum_in_circular_array', result)
    assert result == 10
