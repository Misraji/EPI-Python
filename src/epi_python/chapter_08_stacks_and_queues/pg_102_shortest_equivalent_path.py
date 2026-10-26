"""EPI Python — Exercise 8.4: Normalize Pathnames

Chapter 8: Stacks and Queues
Textbook: pages 102–103 (printed page numbers; the problem starts at the
bottom of page 102, the solution and program are on page 103).

PROBLEM (from the textbook)
---------------------------
"A file or directory can be specified via a string called the pathname. This
string may specify an absolute path, starting from the root, e.g.,
/usr/bin/gcc, or a path relative to the current working directory, e.g.,
scripts/awkscripts.

The same directory may be specified by multiple directory paths. For
example, /usr/lib/../bin/gcc and scripts//./../scripts/awkscripts/././
specify equivalent absolute and relative pathnames.

Write a program which takes a pathname, and returns the shortest equivalent
pathname. Assume individual directories and files have names that use only
alphanumeric characters. Subdirectory names may be combined using forward
slashes (/), the current directory (.), and parent directory (..)."

HINT (from the textbook)
------------------------
"Trace the cases. How should . and .. be handled? Watch for invalid paths."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Process the string from left to right, breaking it apart at each forward
slash, and keep the directory and file names that are seen.

  * A ".." means "go up one level", so it cancels the most recently kept
    name. Names are therefore removed in last-in, first-out order, which
    makes a stack the natural place to keep them.
  * A single "." (current directory) changes nothing and is skipped.
  * If the path begins with "/", it is absolute, and it is impossible to go
    above the root; the book records the leading "/" on the stack to mark
    this (a ".." that would pop it is an error).
  * If the path is relative, a ".." may arrive when no name is available to
    cancel. That means the path starts at an ancestor of the current working
    directory, and the ".." must be kept (recorded on the stack) so that the
    result is still equivalent.
At the end, the contents of the stack, joined by slashes, are the shortest
equivalent path.

Worked example from the book: for "sc//./../tc/awk/././" the stack evolves
as <sc>, <>, <tc>, <tc, awk>. The three "." components and the empty piece
produced by the "//" after "sc" are skipped. The result is "tc/awk".

The book's program is `shortest_equivalent_path(path)`; this file's
function of the same name follows the same stack algorithm (see the code
comparison at the end for the differences).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    '/usr/./bin/../lib' -> '/usr/lib'
    'a/b/../c'          -> 'a/c'
    '/'                 -> '/'
    'a/./b'             -> 'a/b'
"""


def shortest_equivalent_path(path: str) -> str:
    """Simplify a UNIX pathname by removing . and resolving .. segments.

    Implements the textbook's `shortest_equivalent_path` stack algorithm
    (page 103), restructured: the absolute-path marker is kept in a boolean
    instead of on the stack.
    """

    # An empty string is falsy, so `not path` is True for ''. The book also
    # rejects the empty string as an invalid path. `raise ValueError(...)`
    # signals that the argument has the right type but an unacceptable value.
    if not path:
        raise ValueError('Empty pathname')

    # str.startswith(prefix) returns True when the string begins with prefix.
    # A leading '/' means an absolute path rooted at the top directory.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#str.startswith
    absolute = path.startswith('/')

    # A list used as the stack of kept names (and leading '..' entries).
    pieces = []

    # str.split('/') breaks the path at every slash. Consecutive slashes and
    # a leading/trailing slash produce empty strings:
    # '/a//b/'.split('/') -> ['', 'a', '', 'b', ''].
    # Documentation: https://docs.python.org/3/library/stdtypes.html#str.split
    for part in path.split('/'):

        # Empty pieces (from repeated or edge slashes) and '.' change nothing.
        # `part in ('', '.')` tests membership in a two-element tuple.
        # `continue` skips straight to the next loop iteration.
        if part in ('', '.'):
            continue
        if part == '..':

            # A real name on top of the stack is cancelled by '..'.
            # (`pieces and ...` short-circuits when the list is empty.)
            if pieces and pieces[-1] != '..':
                pieces.pop()

            # Nothing to cancel in an absolute path: '..' would go above the
            # root, which the book also treats as an error.
            elif absolute:
                raise ValueError('Cannot traverse above root')

            # Nothing to cancel in a relative path: keep the '..' because the
            # path starts at an ancestor of the current directory.
            else:
                pieces.append(part)
        else:
            pieces.append(part)

    # str.join(iterable) concatenates the strings in the list, placing the
    # separator '/' between neighbours: '/'.join(['usr', 'lib']) -> 'usr/lib'.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#str.join
    if absolute:
        return '/' + '/'.join(pieces)

    # `X or Y` evaluates to X if X is truthy, otherwise to Y. An empty
    # relative result ('') is replaced by '.', the current directory.
    return '/'.join(pieces) or '.'


# TEXTBOOK POST-SOLUTION DISCUSSION (page 103)
# --------------------------------------------
# The time complexity is O(n), where n is the length of the pathname.
#
# VARIANTS
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def shortest_equivalent_path(path)`; raises
# ValueError('Empty string is not a valid path.') for an empty input; uses
# `path_names = []` (comment: "Uses list as a stack.") and, for an absolute
# path, pushes '/' onto the stack itself (comment: "Special case: starts with
# '/', which is an absolute path."). It iterates over a generator expression
# `(token for token in path.split('/') if token not in ['.', ''])`. On '..':
# if the stack is empty or its top is '..' it pushes '..'; otherwise, if the
# top is '/', it raises ValueError('Path error'), else pops. The result is
# `'/'.join(path_names)` with `result[result.startswith('//'):]` to drop the
# extra leading slash (comment: "Avoid starting '//'.").
# File: same name, hints `path: str -> str`; different error messages; the
# absolute marker is a boolean `absolute` instead of a '/' entry on the
# stack; the stack is named `pieces`; filtering uses `continue` instead of a
# generator expression; the '..' branches are reordered (pop first, then
# error for absolute, then push '..'); the absolute result is built as
# '/' + '/'.join(pieces) instead of the slicing trick.
# Behavioural difference: for a relative path that reduces to nothing
# (e.g. 'a/..'), the book returns '' while the file returns '.'.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Demonstrations check representative input/output behavior: '.' and
    # '..' in an absolute path, '..' in a relative path, the root alone,
    # and a '.' that is simply dropped.
    #
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, pytest does the thorough testing.
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
