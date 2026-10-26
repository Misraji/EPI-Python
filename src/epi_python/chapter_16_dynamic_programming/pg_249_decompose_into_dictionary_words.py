"""EPI Python 16.7, textbook printed page 249: The bedbathandbeyond.com problem.

QUESTION: Decompose an unspaced domain-name string into dictionary words, if possible.

TEXTBOOK ALGORITHM: Track the final dictionary word length for every decomposable prefix and reconstruct backward.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_16_dynamic_programming.pg_249_decompose_into_dictionary_words
Test: python -m pytest tests/chapter_16_dynamic_programming/test_pg_249_decompose_into_dictionary_words.py -v
"""

def decompose_into_dictionary_words(domain: str, dictionary: set[str]) -> list[str]:
    if not domain:
        return []
    last_length = [-1] * len(domain)
    for i in range(len(domain)):
        if domain[:i+1] in dictionary:
            last_length[i] = i+1
        if last_length[i] == -1:
            for j in range(i):
                if last_length[j] != -1 and domain[j+1:i+1] in dictionary:
                    last_length[i] = i-j
                    break
    decompositions: list[str] = []
    if last_length[-1] != -1:
        index = len(domain)-1
        while index >= 0:
            decompositions.append(domain[index+1-last_length[index]:index+1])
            index -= last_length[index]

        # Slicing [::-1] reverses the list (the words were found back-to-front).
        decompositions = decompositions[::-1]
    return decompositions


if __name__ == '__main__':
    words = {'bed','bath','and','beyond'}
    result = decompose_into_dictionary_words('bedbathandbeyond',words)
    print(result)
    assert result == ['bed','bath','and','beyond']
