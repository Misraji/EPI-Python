"""EPI Python 15.10, textbook printed page 232: Compute a Gray code.

QUESTION: Generate a cyclic n-bit Gray code with adjacent bit patterns differing in exactly one bit.

TEXTBOOK ALGORITHM: The book gives a backtracking search and a shorter recursive-reflection solution; retain and test both.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_15_recursion.pg_232_gray_code
Test: python -m pytest tests/chapter_15_recursion/test_pg_232_gray_code.py -v
"""

def gray_code_backtracking(num_bits: int) -> list[int]:
    """Directed search implementation from the printed textbook."""
    if num_bits < 1:
        return [0]

    def differs_by_one_bit(x: int, y: int) -> bool:
        bit_difference = x ^ y
        return bool(bit_difference and not (bit_difference & (bit_difference - 1)))

    result = [0]
    history = {0}

    def directed_gray_code() -> bool:
        if len(result) == 1 << num_bits:
            return differs_by_one_bit(result[0], result[-1])
        for bit in range(num_bits):
            candidate = result[-1] ^ (1 << bit)
            if candidate not in history:
                history.add(candidate)
                result.append(candidate)
                if directed_gray_code():
                    return True
                history.remove(candidate)
                result.pop()
        return False

    assert directed_gray_code()
    return result


def gray_code(num_bits: int) -> list[int]:
    """Reflection-based construction from the second textbook solution."""
    if num_bits == 0:
        return [0]
    prev = gray_code(num_bits - 1)
    leading_bit_one = 1 << (num_bits - 1)
    return prev + [leading_bit_one | value for value in reversed(prev)]


if __name__ == '__main__':
    print('3-bit Gray code:', gray_code(3))
    assert len(gray_code(3)) == len(gray_code_backtracking(3)) == 8
