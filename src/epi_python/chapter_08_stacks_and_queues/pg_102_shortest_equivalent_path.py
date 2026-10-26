"""EPI 8.4: Normalize pathnames — printed page 102.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Normalize pathnames
Algorithm: Use a stack of path components, removing redundant periods and parent-directory traversals.
Read the corresponding `pg_102_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_08_stacks_and_queues.pg_102_shortest_equivalent_path
Test: python -m pytest tests/chapter_08_stacks_and_queues/test_pg_102_shortest_equivalent_path.py -v
"""

def shortest_equivalent_path(path: str) -> str:
    """Simplify a UNIX pathname by removing . and resolving .. segments."""
    if not path:
        raise ValueError('Empty pathname')
    absolute = path.startswith('/')
    pieces = []
    for part in path.split('/'):
        if part in ('', '.'):
            continue
        if part == '..':
            if pieces and pieces[-1] != '..':
                pieces.pop()
            elif absolute:
                raise ValueError('Cannot traverse above root')
            else:
                pieces.append(part)
        else:
            pieces.append(part)
    if absolute:
        return '/' + '/'.join(pieces)
    return '/'.join(pieces) or '.'


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = shortest_equivalent_path('/usr/./bin/../lib')
    print("shortest_equivalent_path:", observed)
    assert observed == '/usr/lib'
    observed = shortest_equivalent_path('a/b/../c')
    print("shortest_equivalent_path:", observed)
    assert observed == 'a/c'
    observed = shortest_equivalent_path('/')
    print("shortest_equivalent_path:", observed)
    assert observed == '/'
    observed = shortest_equivalent_path('a/./b')
    print("shortest_equivalent_path:", observed)
    assert observed == 'a/b'
