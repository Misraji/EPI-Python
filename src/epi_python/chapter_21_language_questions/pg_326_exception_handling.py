"""EPI Python — Exercise 21.9: Exception Handling

Chapter 21: Language Questions
Textbook: pages 326–328 (printed page numbers; the problem and the start of
the program to rewrite are at the bottom of 326, the explanation and three
JSON examples are on 327, and the rewritten CSV program is on 328).

PROBLEM (from the textbook)
---------------------------
Briefly describe exception handling in Python, paying special attention to
the roles played by try, except, else, finally, and raise. Rewrite the
following program using exceptions to make it more robust.

The program to rewrite is `get_col_sum(filename, col)`. In outline (not
copied): it opens the file (the book's comment notes this may raise
IOError), wraps it in csv.reader, adds int(row[col]) for every row into a
running sum, closes the file, and prints "Sum = " followed by the total.
It has no error handling at all.

HINT (from the textbook)
------------------------
The book gives no hint for this exercise.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
What an exception is: running a statement or evaluating an expression can
fail, and such failures are called exceptions. An exception need not end
the program. For example, if a user types a filename that does not exist,
or that they are not allowed to read, the program can simply ask again.
Checks like this are written with a `try` block.

Allowed shapes: a `try` block may be followed by
    - an `except` block,
    - a `finally` block,
    - an `except` block and then a `finally` block, or
    - an `except` block, then an `else` block, then a `finally` block.

`finally`: if present, it always runs, whether or not an exception was
raised and whether or not it was caught.

The book then shows three versions of a small `get_value(filename, key)`
function that reads a JSON file and looks up a key:
1. try/finally with no except (here `get_value_with_finally`): any
   exception raised inside `try` propagates to the caller, but the
   `finally` block still closes the file, so a parsing error does not leak
   the file handle.
2. Plain try/except (here `get_value_with_except`): catches ValueError and
   returns (False,), returning (True, value) on success. The file must be
   closed in both branches, so the closing code is duplicated.
3. try/except/finally (here `get_value_with_except_finally`): the same
   behaviour, with the single `handle.close()` moved into `finally`,
   removing the duplication.

Finally the book rewrites the CSV program with try/except/else/finally
(here `get_col_sum` plus the exception class `ColSumCsvParseException`):
- The `else` block shows which code runs only when no exception occurred
  (printing the sum).
- `raise` is used both to create new exceptions (IndexError when a row is
  too short) and to pass errors upward in a new form (a csv.Error becomes
  a ColSumCsvParseException that records the line number), because
  programs should raise exceptions that suit their level of abstraction.
- An inner try/except skips any field that cannot be converted to int,
  printing a message about it.
- `finally` closes the file so there is no resource leak.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    A JSON file containing {"answer": 42}:
        get_value_with_finally(path, "answer")        -> 42
        get_value_with_except(path, "answer")         -> (True, 42)
        get_value_with_except_finally(path, "answer") -> (True, 42)
    A CSV file with rows "3,4", "5,6", "7,oops", column 1:
        get_col_sum -> 10 (4 + 6; "oops" is reported and skipped)
"""

# Python standard library: CSV file reading and writing.
# Module documentation: https://docs.python.org/3/library/csv.html
# csv.reader: https://docs.python.org/3/library/csv.html#csv.reader
# csv.Error: https://docs.python.org/3/library/csv.html#csv.Error
import csv

# Python standard library: JSON encoder and decoder.
# Module documentation: https://docs.python.org/3/library/json.html
# json.loads: https://docs.python.org/3/library/json.html#json.loads
import json


# Type hints (`filename: str`, `key: str`) document intended types; Python
# does not enforce them. No return hint is given because the value can be
# of any JSON type.
def get_value_with_finally(filename: str, key: str):
    """Textbook's first `get_value`: try/finally, exceptions propagate.

    The file is always closed, even if parsing or the key lookup fails.
    """

    # open(filename) opens a file for reading text and returns a file object.
    # It raises OSError (for example FileNotFoundError) if the file cannot be
    # opened; that happens before the `try`, so it simply propagates.
    # https://docs.python.org/3/library/functions.html#open
    handle = open(filename)
    try:

        # handle.read() returns the whole file as one string.
        # json.loads(text) parses JSON text into Python objects (a JSON
        # object becomes a dict). Invalid JSON raises json.JSONDecodeError,
        # a subclass of ValueError. `mapping[key]` raises KeyError if the
        # key is missing. Neither is caught here; both propagate.
        contents = handle.read()
        mapping = json.loads(contents)

        # Even though `return` leaves the function, the `finally` block
        # below still runs first.
        return mapping[key]
    finally:

        # Prevent a resource leak if there is an error parsing the contents
        # (book comment). close() releases the operating-system file handle.
        handle.close()


def get_value_with_except(filename: str, key: str):
    """Textbook's second `get_value`: try/except with duplicated cleanup."""
    handle = open(filename)
    try:
        contents = handle.read()
        mapping = json.loads(contents)

        # Close on the success path...
        handle.close()

        # Returns a 2-tuple (success flag, value).
        return (True, mapping[key])

    # `except ValueError:` runs only if the try block raised ValueError (or
    # a subclass such as json.JSONDecodeError). Other exceptions, e.g.
    # KeyError, are not caught here and propagate to the caller.
    except ValueError:

        # ...and close again on the error path: the duplication the book
        # points out.
        handle.close()

        # `(False,)` is a 1-tuple; the trailing comma is what makes it a
        # tuple rather than just a parenthesized value.
        return (False,)


def get_value_with_except_finally(filename: str, key: str):
    """Textbook's third `get_value`: try/except/finally, cleanup in one place."""
    handle = open(filename)
    try:
        contents = handle.read()
        mapping = json.loads(contents)
        return (True, mapping[key])
    except ValueError:
        return (False,)

    # `finally` runs after either `return` above has computed its value, so
    # one close() covers both the success and the error path.
    finally:
        handle.close()


# Defining a class that inherits from the built-in `Exception` creates a new
# exception type that can be raised and caught like the built-in ones.
# https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions
class ColSumCsvParseException(Exception):
    """Application-level error raised when csv.reader reports invalid CSV.

    Corresponds to the textbook's class of the same name.
    """

    # `__init__` is the method Python calls to initialise a new object.
    def __init__(self, message: str, line_number: int):

        # super().__init__(message) runs the parent class's (Exception's)
        # initialiser, so str(exc) and exc.args contain the message.
        # https://docs.python.org/3/library/functions.html#super
        super().__init__(message)

        # Extra attribute recording how many rows had been processed.
        self.line_number = line_number


def get_col_sum(filename: str, col: int) -> int:
    """Textbook's rewritten CSV column sum using try/except/else/finally.

    Repository version: `return` is placed after the `finally` block (see
    TEXTBOOK CODE COMPARISON).
    """

    # Added check: a negative index would silently count from the end of
    # each row in Python, so it is rejected. IndexError is the built-in
    # exception for a bad sequence index.
    if col < 0:
        raise IndexError("Column index must be nonnegative")

    # May raise IOError; it will propagate to the caller (book comment).
    # In Python 3, IOError is another name for OSError.
    # newline="" is the setting the csv documentation recommends for files
    # given to csv.reader, so that newlines inside quoted fields are handled
    # correctly.
    # https://docs.python.org/3/library/functions.html#open
    csv_file = open(filename, newline="")

    # csv.reader(file) returns an iterator; each step yields one row as a
    # list of strings, split on commas (quoted fields are handled). It
    # raises csv.Error for malformed input.
    csv_reader = csv.reader(csv_file)

    # Chained assignment: both names are set to 0.
    running_sum = line_number = 0
    try:
        for row in csv_reader:

            # Too few fields for the requested column: create and raise an
            # IndexError with a descriptive message. It is not caught below,
            # so it propagates (after `finally` closes the file).
            if col >= len(row):
                raise IndexError("Not enough entries in row " + str(row))
            value = row[col]

            # Book comment (paraphrased): skip rows whose column cannot be
            # parsed as an int, logging the fact.
            # int(text) converts a string such as "42" to an int and raises
            # ValueError for text like "oops".
            try:
                running_sum += int(value)
            except ValueError:
                print("cannot convert " + value + " to int, ignoring")
            line_number += 1

    # `except csv.Error as exc:` catches only csv.Error and binds the caught
    # exception object to the name `exc`.
    except csv.Error as exc:

        # Programs should raise exceptions appropriate to their level of
        # abstraction, so the csv.Error is passed upward as a
        # ColSumCsvParseException (book comment, paraphrased).
        # `raise NewError(...) from exc` records `exc` as the direct cause
        # (stored in __cause__), so tracebacks show both errors.
        # https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
        raise ColSumCsvParseException("Error processing csv", line_number) from exc
    else:

        # `else` runs only when the `try` block finished WITHOUT raising.
        print("Sum = " + str(running_sum))
    finally:

        # Ensure there is no resource leak (book comment). `finally` runs on
        # success, after an exception, and before any return or re-raise.
        csv_file.close()

    # Reached only when no exception escaped the try statement above.
    return running_sum


# TEXTBOOK POST-SOLUTION DISCUSSION (page 328)
# -------------------------------------------
# Python has many built-in exception types, e.g. IndexError,
# FloatingPointError, EnvironmentError and ValueError, and these should be
# used whenever possible.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# JSON examples:
# - Book names all three functions `get_value(filename, key)`; file uses
#   `get_value_with_finally`, `get_value_with_except` and
#   `get_value_with_except_finally`, with `str` type hints.
# - Book's local names `file_contents` and `js_text`; file uses `contents`
#   and `mapping`. Logic is otherwise the same as the book's listings.
# CSV exception class:
# - Book: `def __init__(self, *args)`, calls `Exception.__init__(self,
#   *args)` and sets `self.line_number = args[1]`. File:
#   `__init__(self, message: str, line_number: int)`, calls
#   `super().__init__(message)` (only the message, not both args) and sets
#   `self.line_number = line_number`.
# CSV function `get_col_sum`:
# - Type hints added; file adds `if col < 0: raise IndexError(...)`.
# - Book: `open(filename)`; file: `open(filename, newline="")`.
# - Book's skip message is "Cannot convert ..." (capital C); file prints
#   "cannot convert ...".
# - Book's csv.Error handler is `except csv.Error:` and prints
#   "In csv.Error handler" before raising; file binds `as exc`, has no
#   print, and uses `raise ... from exc`.
# - Book places `return running_sum` INSIDE the `finally` block. In Python a
#   return in `finally` discards any exception in flight, so the book's
#   version would silently swallow the IndexError and the
#   ColSumCsvParseException it raises. The file puts `return running_sum`
#   after the try statement, so those exceptions propagate.
# - The book does not present the original, unrobust `get_col_sum` as
#   separate executable code in this file; it is summarised in the PROBLEM
#   section only.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # The examples write small temporary files so that this block runs
    # anywhere without needing existing data files.

    # Python standard library: temporary files and directories.
    # Module documentation: https://docs.python.org/3/library/tempfile.html
    # TemporaryDirectory: https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryDirectory
    from tempfile import TemporaryDirectory

    # Python standard library: object-oriented filesystem paths.
    # Module documentation: https://docs.python.org/3/library/pathlib.html
    # Path.write_text: https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_text
    from pathlib import Path

    # `with TemporaryDirectory() as directory:` creates a new empty directory
    # and binds its path (a str) to `directory`. When the `with` block ends,
    # even because of an error, the directory and its contents are deleted.
    with TemporaryDirectory() as directory:

        # Path(directory) / "example.json" joins path components with the
        # `/` operator. write_text(...) creates/overwrites the file with the
        # given text.
        json_file = Path(directory) / "example.json"
        json_file.write_text('{"answer": 42}', encoding="utf-8")

        # Functions are objects, so the three versions can be looped over.
        for function in (
            get_value_with_finally,
            get_value_with_except,
            get_value_with_except_finally,
        ):
            # str(json_file) converts the Path back to a plain string.
            result = function(str(json_file), "answer")
            print(function.__name__, result)

            # `assert` stops the program with an AssertionError if the
            # condition is false. The condition is a conditional expression
            # `A if test else B`: the first version returns the bare value
            # 42, the other two return the tuple (True, 42).
            assert result == 42 if function is get_value_with_finally else result == (True, 42)

        # CSV example: column 1 holds 4, 6 and "oops"; "oops" is reported
        # and skipped, so the sum is 10.
        csv_file = Path(directory) / "example.csv"
        csv_file.write_text("3,4\n5,6\n7,oops\n", encoding="utf-8")
        assert get_col_sum(str(csv_file), 1) == 10
        print("CSV exception-handling example passed.")
