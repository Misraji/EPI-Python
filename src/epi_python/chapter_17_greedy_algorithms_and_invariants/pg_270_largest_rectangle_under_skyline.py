"""EPI 17.8: Compute the largest rectangle under the skyline, printed page 270.

Educational reconstruction, not a verbatim transcription. Algorithm: Monotone increasing stack tracks unresolved bar spans. Each index is pushed/popped once.
The corresponding chapter's exercise Markdown retains the PDF text-layer
explanations, question and variants (with known OCR mistakes).

Run: python -m epi_python.chapter_17_greedy_algorithms_and_invariants.pg_270_largest_rectangle_under_skyline
Tests: python -m pytest tests/chapter_17_greedy_algorithms_and_invariants/test_pg_270_largest_rectangle_under_skyline.py -v
"""

def largest_rectangle_under_skyline(heights: list[int]) -> int:
    """Largest axis-aligned rectangle below an integer-height histogram."""
    stack=[]
    best=0
    extended=heights+[0]
    for index,height in enumerate(extended):
        while stack and extended[stack[-1]]>height:
            popped=stack.pop()
            width=index if not stack else index-stack[-1]-1
            best=max(best,extended[popped]*width)
        stack.append(index)
    return best

if __name__ == "__main__":
    # Executable demonstration cases; pytest has the full set.
    result=largest_rectangle_under_skyline([])
    print('largest_rectangle_under_skyline', result)
    assert result == 0
    result=largest_rectangle_under_skyline([1])
    print('largest_rectangle_under_skyline', result)
    assert result == 1
    result=largest_rectangle_under_skyline([2, 1, 5, 6, 2, 3])
    print('largest_rectangle_under_skyline', result)
    assert result == 10
    result=largest_rectangle_under_skyline([2, 2, 2])
    print('largest_rectangle_under_skyline', result)
    assert result == 6
