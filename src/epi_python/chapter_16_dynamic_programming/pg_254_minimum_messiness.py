"""EPI Python 16.11, textbook printed page 254: The pretty printing problem.

QUESTION: Arrange words in fixed-width lines minimizing the sum of squared unused character counts.

TEXTBOOK ALGORITHM: For each ending word, try every possible starting word of the final line and cache best prefix cost.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_16_dynamic_programming.pg_254_minimum_messiness
Test: python -m pytest tests/chapter_16_dynamic_programming/test_pg_254_minimum_messiness.py -v
"""

def minimum_messiness(words: list[str], line_length: int) -> int:
    if not words:
        return 0
    if any(len(word) > line_length for word in words):
        raise ValueError('A word cannot fit on any line')
    num_remaining_blanks = line_length - len(words[0])
    min_messiness = [num_remaining_blanks ** 2] + [float('inf')] * (len(words)-1)
    for i in range(1,len(words)):
        num_remaining_blanks = line_length - len(words[i])
        min_messiness[i] = min_messiness[i-1] + num_remaining_blanks ** 2
        for j in reversed(range(i)):
            num_remaining_blanks -= len(words[j]) + 1
            if num_remaining_blanks < 0:
                break
            first_j_messiness = 0 if j == 0 else min_messiness[j-1]
            current_line_messiness = num_remaining_blanks ** 2
            min_messiness[i] = min(min_messiness[i], first_j_messiness + current_line_messiness)
    return int(min_messiness[-1])


if __name__ == '__main__':
    result=minimum_messiness(['a','b','c','d'],5)
    print('Minimum messiness:',result)
    assert result==8
