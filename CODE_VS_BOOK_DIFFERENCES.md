# Code vs. book: differences for review

Produced during the documentation pass of October 26, 2026. **No executable code or tests were changed.**
Each exercise file also carries a `# TEXTBOOK CODE COMPARISON` block with the same information next to the code.
Page 164 (Exercise 12.2) is the approved sample; its code matches the book's two listings.


### src/epi_python/chapter_04_primitive_types/pg_024_parity.py
- Exercise: 4.1 Computing the parity of a word, printed pages 24–27
- Code vs book: book prints four functions all named `parity(x)`; file renames them `parity_brute_force`, `parity_erase_lowest_set_bit`, `parity_lookup_table`, `parity_xor_folding`, parameter `word: int` with type hints. File adds `_check_word` (ValueError outside 0..2**64-1), `_build_16bit_parity_cache`/`_PRECOMPUTED_PARITY` (book never shows table construction), and a `parity` wrapper. Lookup version uses module constant `_CACHE_MASK` and literal shifts 48/32/16 instead of book's local `MASK_SIZE`/`BIT_MASK` and `k * MASK_SIZE`; XOR-fold returns `word & 1` instead of `x & 0x1`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_04_primitive_types/pg_027_swap_bits.py
- Exercise: 4.2 Swap bits, printed pages 27–28
- Code vs book: same name/parameters plus type hints; book's local `bit_mask` variable folded into `x ^= (1 << i) | (1 << j)`; extra parentheses in the bit test (same meaning in Python); book's code comments were missing (restored as comments).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_04_primitive_types/pg_028_closest_int_same_bit_count.py
- Exercise: 4.4 Find a closest integer with the same weight, printed pages 28–29
- Code vs book: book's local `NUM_UNSIGNED_BITS = 64` becomes a parameter `width: int = 64`; loop variable `i` -> `index`; book's in-place `x ^= ...; return x` becomes `mask = ...; return x ^ mask`; ValueError message differs ('All bits are 0 or 1' in book).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_04_primitive_types/pg_028_reverse_bits.py
- Exercise: 4.3 Reverse bits, printed page 28
- Code vs book: `reverse_bits` gains a `width` parameter (non-64 widths delegate to brute force) and a 64-bit range check; uses module `_MASK_16` and literal shifts instead of `MASK_SIZE`/`BIT_MASK`; adds `_build_reverse_16_bit_table` (book never builds PRECOMPUTED_REVERSE). `reverse_bits_brute_force` is not in the book and differs from the book's described (uncoded) swap-based brute force.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_04_primitive_types/pg_029_multiply_without_arithmetic.py
- Exercise: 4.5 Compute x × y without arithmetical operators, printed pages 29–31
- Code vs book: book's nested ripple-carry `add` (mask `k`, `carryin`/`carryout`, `running_sum | carryin`) is NOT in the file; file uses a top-level `add_bits` with a different XOR/AND-carry loop. `multiply` uses `result` instead of `running_sum`, split shift statements, and adds a negative-input check that uses `<` (an operator the problem forbids).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_04_primitive_types/pg_031_divide_without_arithmetic.py
- Exercise: 4.6 Compute x/y, printed page 31
- Code vs book: different algorithm structure. Book starts at `power = 32`, `y_power = y << power` and only shifts down (O(n)); file restarts from `multiple, factor = y, 1` each outer iteration and shifts up (the O(n**2) approach the book discusses before improving it). Adds ValueError input check.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_04_primitive_types/pg_032_power.py
- Exercise: 4.7 Compute x^y, printed page 32
- Code vs book: book loops on a separate `power` variable (`result, power = 1.0, y`, combined `x, power = x * x, power >> 1`); file mutates `y` directly with split statements. Adds ZeroDivisionError check for x == 0, y < 0.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_04_primitive_types/pg_032_reverse_digits.py
- Exercise: 4.8 Reverse digits, printed pages 32–33
- Code vs book: book `reverse(x)` renamed `reverse_digits` with hints; `x_remaining` -> `remaining`; sign stored in `negative` rather than re-testing `x < 0`. Loop body matches.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_04_primitive_types/pg_033_is_number_palindromic.py
- Exercise: 4.9 Check if a decimal integer is a palindrome, printed pages 33–34
- Code vs book: book `is_palindrome_number` uses `math.floor(math.log10(x)) + 1` and a `for i in range(num_digits // 2)` loop; file `is_number_palindromic` has no math import, finds the divisor with a while loop and loops `while x:`, removing both digits in one statement (stopping rule differs from the book). `is_number_palindromic_half_reverse` is an extra, non-book alternative. Old docstring misquoted the book's examples (-112); corrected to the book's list.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_04_primitive_types/pg_034_uniform_random.py
- Exercise: 4.10 Generate uniform random numbers, printed pages 34–35
- Code vs book: adds `bit_source=None` parameter defaulting to `random.getrandbits(1)` (book calls a provided `zero_one_random()`, no import); bit count via `(count - 1).bit_length()` instead of book's `while (1 << i) < number_of_outcomes` loop (same count); returns inside loop instead of `break` then return; adds lower>upper ValueError.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_04_primitive_types/pg_035_rectangle_intersection.py
- Exercise: 4.11 Rectangle intersection, printed pages 35–36
- Code vs book: namedtuple matches; parameters `R1, R2` -> `a, b` with hints; book's nested `is_intersect` helper replaced by its inlined negation; corners stored in `x1, y1, x2, y2` before building the result. Same results and sentinel.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_21_language_questions/pg_325_compute_top_k_variance.py
- Exercise: 21.8 Python code, printed pages 325–326
- Code vs book: both book programs present. Long version renamed `compute_top_k_variance_original`, type hints/variable annotations added, `key` -> `student`, `variance = variance + ...` -> `+=`. Pythonic version: comprehension variable `scores` renamed `student_scores`/`selected_scores`. Both call an added `_check_inputs` helper.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_21_language_questions/pg_326_exception_handling.py
- Exercise: 21.9 Exception handling, printed pages 326–328
- Code vs book: three book `get_value` functions renamed `get_value_with_finally`/`_with_except`/`_with_except_finally` (locals `file_contents`/`js_text` -> `contents`/`mapping`). `ColSumCsvParseException.__init__(self, *args)` becomes `(message, line_number)` with `super().__init__(message)`. `get_col_sum`: adds `col < 0` check and `newline=""`; message "cannot" vs book's "Cannot"; csv.Error handler drops the book's "In csv.Error handler" print and uses `raise ... from exc`; book's `return running_sum` inside `finally` (which would swallow the raised exceptions) moved after the try statement. The original unrobust `get_col_sum` is not in the file as code.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_039_dutch_flag_partition.py
- Exercise: 5.1 The Dutch national flag problem, printed pages 39–42
- Code vs book: All three book programs are present but the book names all of them `dutch_flag_partition(pivot_index, A)`; the file renames the first two `dutch_flag_partition_quadratic` / `dutch_flag_partition_two_pass`, renames `A` to `values`, adds type hints, omits `RED, WHITE, BLUE = range(3)`, adds helper `_validate_pivot` (raises IndexError, rejects negative indices), and returns the list (book returns None). The two-pass version's second loop is restructured (`reversed(range(smaller, len(values)))` with no `< pivot` break, vs. book's full reverse scan with break). Final version splits `smaller, equal = smaller + 1, equal + 1` into two statements.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_043_multiply_digits.py
- Exercise: 5.3 Multiply two arbitrary-precision integers, printed pages 43–44
- Code vs book: Book `multiply(num1, num2)`; file `multiply_digits` with type hints and an added empty-operand ValueError guard. Sign uses `!=` instead of `^`. Book mutates the callers' first digits with abs(); file copies both lists with abs() on every digit. Result array renamed `product`; loops use `range(len-1, -1, -1)` instead of `reversed(range(...))`. Leading-zero removal is a `while` loop instead of the book's `next(... enumerate ...) or [0]` slice; sign applied in place to `result[0]` (skipped for [0]) instead of `[sign * result[0]] + result[1:]`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_043_plus_one.py
- Exercise: 5.2 Increment an arbitrary-precision integer, printed page 43
- Code vs book: Book `plus_one(A)`; file renames parameter to `digits` (and loop var `i` to `index`), adds type hints and an empty-input ValueError guard. Otherwise matches.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_044_can_reach_end.py
- Exercise: 5.4 Advancing through an array, printed pages 44–45
- Code vs book: Book `can_reach_end(A)` uses a `while` loop over `furthest_reach_so_far`/`last_index`/`i` and returns `furthest_reach_so_far >= last_index`. File renames parameter `max_steps` and variables (`farthest`, `last`, `index`), adds type hints, and restructures into a `for ... enumerate` loop with `break`, early `return True`, and final `return last < 0`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_045_delete_duplicates.py
- Exercise: 5.5 Delete duplicates from a sorted array, printed pages 45–46
- Code vs book: Book `delete_duplicates(A)` with `write_index`/`i`; file renames parameter `sorted_array`, variables `write`/`read`, adds type hints, and swaps the operands of the `!=` comparison. Otherwise matches.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_046_compute_max_profit.py
- Exercise: 5.6 Buy and sell a stock once, printed pages 46–47
- Code vs book: Book `buy_and_sell_stock_once(prices)`; file renamed `compute_max_profit`, type hints added, `min_price_so_far` renamed `min_seen`, tuple initialisation split into two statements, no `max_profit_sell_today` temporary, and the minimum is updated before (book: after) the profit update. Same results.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_047_buy_and_sell_stock_twice.py
- Exercise: 5.7 Buy and sell a stock twice, printed pages 47–48
- Code vs book: Name/parameter match; type hints and an empty-input guard added. Forward phase uses `append` into `left_profits` instead of indexing a preallocated `first_buy_sell_profits = [0] * len(prices)` via `enumerate`. Backward phase loops days n-1..0 with `range(...,-1,-1)` (book: `reversed(list(enumerate(prices[1:], 1)))`, days n-1..1), keeps an extra running `second_best` and a separate `best_total` starting at 0.0, and uses `(left_profits[i - 1] if i else 0.0)`; book adds `max_price_so_far - price + first_buy_sell_profits[i - 1]` into the reused `max_total_profit`. Variable names differ.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_048_rearrange_alternation.py
- Exercise: 5.8 Computing an alternation, printed pages 48–49
- Code vs book: Book `rearrange(A)` is implemented as `rearrange_alternation_in_place(values) -> None` with `reverse=bool(i % 2)` instead of `reverse=i % 2`. The file also contains `rearrange_alternation`, a non-book helper that copies the list and applies the explicit even/odd swap rule from the book's prose.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_049_generate_primes.py
- Exercise: 5.9 Enumerate all primes to n, printed pages 49–50
- Code vs book: Both book programs are named `generate_primes(n)`; the file names them `generate_primes_basic` and `generate_primes_odd_only`, and uses the name `generate_primes` for a third, non-book sieve (full table, `while c*c <= n`, starts at c*c, list-comprehension result). Basic: `is_prime`->`candidates`, `i`->`multiple`, added `n < 2` guard. Odd-only: `size`->`count`, `is_prime`->`candidate`, `2 * i**2` written `2*i*i`. Type hints added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_050_apply_permutation.py
- Exercise: 5.10 Permute the elements of an array, printed pages 50–52
- Code vs book: Both book programs are named `apply_permutation(perm, A)`. Program 1 keeps the name (A->values, i->start, next->current, temp->destination, cached n, length-check ValueError, `return values` added). Program 2 is `apply_permutation_without_sign_marking`; the book's helper `cyclic_permutation(start, perm, A)` with `next_i`/`next_temp` becomes a closure `permute_cycle(start)` with a tuple-assignment swap; `while ... else` minimum test kept. `apply_permutation_visited` is a non-book helper (book only describes the Boolean-array idea in prose). Type hints added throughout.
- Needs PDF review: none (note: the book's illustrative array is printed as <α,b,c,δ>; transcribed as printed)
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_052_next_permutation.py
- Exercise: 5.11 Compute the next permutation, printed pages 52–54
- Code vs book: Book `next_permutation(perm)` (in place) corresponds to `next_permutation_in_place(permutation)`: variables renamed (`inversion_point`->`pivot`, `i`->`j`), `== -1` written `< 0`, swap loop `range(len-1, pivot, -1)` instead of `reversed(range(...))`, type hints. The file's `next_permutation(values)` reuses the book's name for a non-book copying version that finds the swap index with a `while` loop. Old inaccurate comment about `list.reverse()` was rewritten.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_054_offline_random_sampling.py
- Exercise: 5.12 Sample offline data, printed pages 54–55
- Code vs book: Book `random_sampling(k, A)` calls `random.randint` directly and returns None; file `random_sampling(k, values, rng=None)` adds an optional generator parameter, type hints, a k-range ValueError guard, renames `r` to `j`, and returns `values[:k]`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_055_online_random_sampling.py
- Exercise: 5.13 Sample online data, printed pages 55–56
- Code vs book: Book `online_random_sample(it, k)`; file `online_random_sample(stream, k, rng=None)` with type hints, optional generator, `iter(stream)` call, and two added ValueError checks (negative k; fewer than k items — the book only states this as an assumption). Book's manual `num_seen_so_far` counter replaced by `enumerate(iterator, start=k + 1)`; names `sampling_results`->`reservoir`, `idx_to_replace`->`slot`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_056_compute_random_permutation.py
- Exercise: 5.14 Compute a random permutation, printed pages 56–57
- Code vs book: Book `compute_random_permutation(n)` calls `random_sampling(n, permutation)` (Exercise 5.12). File keeps the name, adds an optional `rng` parameter, type hints and an `n < 0` ValueError guard, and inlines the sampling loop with `rng.randrange(i, n)` instead of calling `random_sampling`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_057_compute_random_subset.py
- Exercise: 5.15 Compute a random subset, printed pages 57–58
- Code vs book: Book `random_subset(n, k)`; file adds optional `rng` parameter, type hints (incl. `dict[int, int]` annotation) and a k-range ValueError guard; variables renamed (`changed_elements`->`changed`, `rand_idx`->`r`, mapped values -> `y`/`x`); the two separate swap assignments become one tuple assignment. Same behaviour.
- Needs PDF review: none. Book-text observations recorded in the docstring: prose gives the random range as [0, n-1-i] while the program uses [i, n-1]; the worked example labels the fourth draw "third iteration".
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_058_nonuniform_random_number.py
- Exercise: 5.16 Generate nonuniform random numbers, printed pages 58–59 (old docstring said 58–60; page 60 belongs to the multidimensional-arrays intro and 5.17)
- Code vs book: Book `nonuniform_random_number_generation(values, probabilities)`; file `nonuniform_random_number(values, probabilities, rng=None)` with type hints, two added ValueError checks, `bisect.bisect_right` instead of `bisect.bisect` (same function), random value scaled by the total weight (`* cumulative[-1]`), and the index clamped with `min(index, len(values) - 1)`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_060_sudoku_checker.py
- Exercise: 5.17 The Sudoku checker problem, printed pages 60–61
- Code vs book: Both book programs present (`is_valid_sudoku`, `is_valid_sudoku_pythonic`), parameter `partial_assignment` renamed `grid`, type hints, added shape and digit-range checks. First: helper `has_duplicate` (filter/lambda) replaced by `no_duplicates` (opposite sense, list comprehension, range check); `any(...)`/`all(...)` generator expressions replaced by explicit loops with early return; `int(math.sqrt(n))` replaced by `isqrt`. Second: book's single Counter generator expression with `str(c)`-position keys and `i / region_size` (true division in Python 3 — likely a book bug for region grouping) replaced by explicit loops building tagged tuple keys with `//`; `Counter` imported directly.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_061_spiral_ordering.py
- Exercise: 5.18 Compute the spiral ordering of a 2D array, printed pages 61–64
- Code vs book: NEITHER of the book's two programs is implemented. The book prints (1) `matrix_in_spiral_order(square_matrix)` with nested `matrix_layer_in_clockwise(offset)` using slices and `zip(*square_matrix)`, and (2) a single-loop version with `SHIFT` direction table, `(direction + 1) & 3`, zeroing visited cells. The file's only function reuses the name `matrix_in_spiral_order(matrix)` but implements a different four-boundary shrinking algorithm, adds empty-input handling and a ragged-row ValueError, supports rectangular matrices, and does not mutate the input.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_064_rotate_matrix.py
- Exercise: 5.19 Rotate a 2D array, printed pages 64–65
- Code vs book: Book `rotate_matrix(square_matrix)` uses `~` indexing and a single four-cell tuple assignment over `for i ... for j in range(i, matrix_size - i)`; file renames parameter `matrix`, adds type hints and a square-shape ValueError, uses explicit `lo`/`hi` bounds, a temporary `top` with four sequential assignments, and returns the matrix (book returns None). The book's `class RotatedMatrix` (read_entry/write_entry view) is missing from the file.
- Needs PDF review: none. Book-text observation noted in docstring: the book calls <13,14,15,16> "the first row" of Figure 5.4(a), but it is the last row.
- check_code_unchanged: OK

### src/epi_python/chapter_05_arrays/pg_065_generate_pascal_triangle.py
- Exercise: 5.20 Compute rows in Pascal's triangle, printed pages 65–66
- Code vs book: Name/parameter match; type hints added. Book preallocates all rows via `[[1] * (i + 1) for i in range(n)]` and fills `result[i][j]` from `result[i - 1]`; file builds and appends rows one at a time, reading the previous row as `triangle[-1]`. Variable names differ. Same output.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_06_strings/pg_068_string_integer_interconversion.py
- Exercise: 6.1 Interconvert Strings and Integers, printed pages 68–69
- Code vs book: int_to_string follows the book's algorithm but restructured (type hints; early `return '0'` instead of the book's `while True ... break` loop; `abs(x)` instead of tuple assignment; '-' appended to the digit list before reversing). Book's reduce-based `string_to_int(s)` is the file's `string_to_int_reduce(text)`: adds ValueError check for '' / '-', lambda params renamed, `s[s[0]=='-':]` replaced by a conditional expression, sign applied with a conditional expression instead of `* (-1 if ... else 1)`. The file's `string_to_int` is an extra explicit-loop helper not in the book (name collision with the book's function).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_06_strings/pg_069_convert_base.py
- Exercise: 6.2 Base Conversion, printed pages 69–70
- Code vs book: Book's recursive `convert_base(num_as_string, b1, b2)` is the file's `convert_base_recursive(number, b1, b2)`: adds validation of bases, empty input and digits (nested `digit_value`), nested output helper renamed `emit(value)` using b2 from the enclosing scope, conditional-expression slice instead of `[is_negative:]`, and "-0" yields "0" (book: "-0"). The file's `convert_base` is an extra iterative (divmod) implementation with a DIGITS constant, not in the book (name collision). Old docstring's "1A7 base 13 = 320" was wrong (it is 306) and was replaced.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_06_strings/pg_070_ss_decode_col_id.py
- Exercise: 6.3 Compute the Spreadsheet Column Encoding, printed pages 70–71
- Code vs book: Book's `ss_decode_col_id(col)` (reduce) is the file's `ss_decode_col_id_reduce(col)` — same expression, type hints added. The file's `ss_decode_col_id(column)` is an extra explicit-loop helper (name collision).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_06_strings/pg_071_replace_and_remove.py
- Exercise: 6.4 Replace and Remove, printed pages 71–72
- Code vs book: Book's `replace_and_remove(size, s)` is the file's `replace_and_remove_in_place(size, letters)`: adds ValueError checks for size and capacity, renamed variables, final size computed before resetting the write index (equivalent), slice assigned `['d','d']` instead of `'dd'`. The file's `replace_and_remove` is an extra helper (extends the list, returns the valid slice instead of the size), not in the book (name collision).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_06_strings/pg_072_is_palindromic.py
- Exercise: 6.5 Test Palindromicity, printed pages 72–73
- Code vs book: Book `is_palindrome(s)` with i, j; file `is_palindromic(text)` with left/right, type hints, inner-loop conditions reordered (`left < right and not ...`), separate increment statements. Same algorithm.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_06_strings/pg_073_reverse_words.py
- Exercise: 6.6 Reverse All the Words in a Sentence, printed pages 73–74
- Code vs book: Book's bytearray `reverse_words(s)` is the file's `reverse_words_bytearray(buffer)`: nested `reverse_range(start, finish)` drops the array parameter (closure), separate increment statements, type hints. The file's `reverse_words(sentence)` is an extra str split/join helper (name collision).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_06_strings/pg_074_phone_mnemonics.py
- Exercise: 6.7 Compute All Mnemonics for a Phone Number, printed pages 74–75
- Code vs book: Table `MAPPING` renamed `PHONE`; adds a digits-only ValueError check; helper `phone_mnemonic_helper(digit)` renamed `search(pos)` with early return; lists renamed `result`/`candidate`, candidate filled with '' instead of 0; type hints. Same algorithm.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_06_strings/pg_075_look_and_say.py
- Exercise: 6.8 The Look-and-Say Problem, printed pages 75–76
- Code vs book: `look_and_say`: book's nested `next_number(s)` helper is inlined, run measured with index j instead of a count variable, renamed variables, type hints. `look_and_say_pythonic`: same expression, variable renamed, type hints.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_06_strings/pg_076_roman_to_integer.py
- Exercise: 6.9 Convert from Roman to Decimal, printed pages 76–77
- Code vs book: Book's `roman_to_integer(s)` (functools.reduce over reversed indices, table `T`) is the file's `roman_to_integer_right_to_left(roman)`, rewritten as an explicit countdown for-loop, table `values`, plus an empty-string guard returning 0; functools not imported. The file's `roman_to_integer` is an extra left-to-right enumerate helper (name collision).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_06_strings/pg_077_get_valid_ip_addresses.py
- Exercise: 6.10 Compute All Valid IP Addresses, printed pages 77–78
- Code vs book: Book `get_valid_ip_address(s)` (singular) loops over part LENGTHS bounded by the remaining string with `parts = [None]*4` and prunes invalid prefixes early; file `get_valid_ip_addresses(digits)` loops over period POSITIONS without len bounds, builds a 4-tuple and checks all parts at once with `all(...)` (no pruning); validity helper `valid(chunk)` uses a different formulation (non-empty, <=3 chars, no leading zero, <=255) vs book's `len(s)==1 or (s[0]!='0' and int(s)<=255)`. Same result order.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_06_strings/pg_078_snake_string.py
- Exercise: 6.11 Write a String Sinusoidally, printed pages 78–79
- Code vs book: Book's three-loop `snake_string(s)` is the file's `snake_string_three_pass(text)` (same body). Book's `snake_string_pythonic(s)` is the file's `snake_string(text)` (`text[0::2]` vs `s[::2]`, same meaning). Names are swapped relative to the book; type hints added. The book's sinusoidal diagram is redrawn in plain text and labelled as such.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_06_strings/pg_079_run_length_encoding.py
- Exercise: 6.12 Implement Run-Length Encoding, printed page 79
- Code vs book: `decoding` matches the book's algorithm (renamed variables, `list[str]` annotation, type hints). `encoding` restructured: book uses one `for i in range(1, len(s)+1)` loop with a count variable; file uses a while loop over run starts with an inner run-extending loop and no count variable. Same results.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_06_strings/pg_079_rabin_karp.py
- Exercise: 6.13 Find the First Occurrence of a Substring, printed pages 79–81
- Code vs book: Book `rabin_karp(t, s)` uses BASE = 26, unbounded integers (no modulus), functools.reduce for initial hashes, a loop over window ends with a separate final-window check. File `rabin_karp(text, pattern)` uses base 256 with modulus 1_000_000_007 and `pow(base, m-1, modulus)`, for-loop initial hashes, a loop over window starts (no separate final check), explicit empty-pattern return; type hints added. Same results.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_07_linked_lists/pg_084_merge_two_sorted_lists.py
- Exercise: 7.1 Merge Two Sorted Lists, printed pages 84–85
- Code vs book: ListNode is a @dataclass (`data`, `next`) instead of the book's class with `__init__(self, data=0, next_node=None)`, so `ListNode()` becomes `ListNode(0)`. Book function `merge_two_sorted_lists(L1, L2)` is named `merge_sorted_lists(l1, l2)` with type hints; the name `merge_two_sorted_lists` is reused for an added list-in/list-out helper. Comparison is `<=` (book `<`), so equal keys are taken from l1 first; `while L1 and L2` becomes explicit `is not None` checks; `tail.next = L1 or L2` becomes a conditional expression; `dummy_head` renamed `dummy`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_07_linked_lists/pg_085_reverse_sublist.py
- Exercise: 7.2 Reverse a Single Sublist, printed pages 85–86
- Code vs book: Same head-insertion algorithm. Book `reverse_sublist(L, start, finish)` is `reverse_sublist_nodes(head, start, finish)` (type hints); the name `reverse_sublist` is reused for an added list-in/list-out helper that raises ValueError on bad bounds. Book's single three-target tuple assignment is split into three ordinary assignments; variables renamed (dummy_head/sublist_head/sublist_iter/temp -> dummy/predecessor/front/moving). ListNode is a @dataclass. Old docstring's O(n) complexity and variants were wrong and were replaced with the book's O(f) and its two variants.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_07_linked_lists/pg_086_has_cycle.py
- Exercise: 7.3 Test for Cyclicity, printed pages 86–87
- Code vs book: Book main `has_cycle(head)` (nested `cycle_len`) is `has_cycle_nodes_via_cycle_length(head)` with the cycle-length loop inlined. `has_cycle_nodes(head)` implements the program the book prints as a variant question ("Is the program correct?"; the book gives no answer), using a new `finder` pointer instead of resetting `slow`. Loop condition `fast and fast.next and fast.next.next` became `fast is not None and fast.next is not None`. `has_cycle(values, cycle_start)` is an added bool helper, not the book's has_cycle. Type hints added; ListNode is a @dataclass.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_07_linked_lists/pg_087_overlapping_no_cycle_lists.py
- Exercise: 7.4 Test for Overlapping Lists—Lists Are Cycle-Free, printed pages 87–88
- Code vs book: Same name `overlapping_no_cycle_lists`; params `a, b`. File swaps lists and lengths and advances `length_b - length_a` (book swaps only lists and uses `abs(...)`); final loop `while a is not b` versus the book's `while L1 and L2 and L1 is not L2` (equivalent after alignment). Imports ListNode from pg_084. Helpers build_nodes, node_values, overlapping_tail_first_value added. Old hint text was wrong and was replaced with the book's hint.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_07_linked_lists/pg_088_overlapping_lists_with_cycles.py
- Exercise: 7.5 Test for Overlapping Lists—Lists May Have Cycles, printed pages 88–90
- Code vs book: Book `overlapping_lists(L1, L2)` is `overlapping_lists_with_cycles(a, b)`. It uses `has_cycle_nodes` (the 7.3 variant program) rather than the book's main has_cycle. The control flow is restructured: the book first walks around root2's cycle to rule out disjoint cycles, then always does the stem-length alignment and returns `L1 if L1 is L2 else root1`. The file aligns stems only when the entries are identical, and otherwise walks entry_a's cycle looking for entry_b. One-cycle test uses `(x is None) != (y is None)`. It has three repository imports (ListNode, has_cycle_nodes, overlapping_no_cycle_lists), two of them mid-file.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_07_linked_lists/pg_090_delete_node.py
- Exercise: 7.6 Delete a Node from a Singly Linked List, printed page 90
- Code vs book: Book `deletion_from_list(node_to_delete)` is `delete_node(node)`. It has the same two assignments plus an added ValueError when the node is the tail. Helpers build_nodes, node_values, delete_at_index added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_07_linked_lists/pg_090_remove_kth_last.py
- Exercise: 7.7 Remove the kth Last Element from a List, printed pages 90–91
- Code vs book: Same name `remove_kth_last` (param `head`). It adds ValueError for k <= 0 and IndexError when k > length (the book only assumes at least k nodes). Iterators are renamed first/second -> lead/follow. The lead starts at the dummy and loops `while lead.next is not None` (book: starts at head, `while first:`), which gives the same step count. Helpers added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_07_linked_lists/pg_091_remove_duplicates_sorted_list.py
- Exercise: 7.8 Remove Duplicates from a Sorted List, printed pages 91–92
- Code vs book: Book `remove_duplicates(L)` is `remove_duplicates_nodes(head)`. `it` is renamed `current`, and truthiness tests became `is not None`; otherwise the code is identical. ListNode is a @dataclass. Helper remove_duplicates_sorted_list added. Old variant text ("retain at most m copies") misstated the book; it is replaced with the book's variant (remove all nodes of any k appearing more than m times).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_07_linked_lists/pg_092_cyclic_right_shift.py
- Exercise: 7.9 Implement Cyclic Right Shift for Singly Linked Lists, printed pages 92–93
- Code vs book: Book `cyclically_right_shift_list(L, k)` is `cyclic_right_shift(head, k)`. It adds ValueError for k < 0. `n` is renamed `length`, and `if k == 0` became `if not k`. The `while steps_to_new_head:` countdown became `for _ in range(steps)`. The algorithm is otherwise the same. Helpers added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_07_linked_lists/pg_093_even_odd_merge.py
- Exercise: 7.10 Implement Even-Odd Merge, printed pages 93–94
- Code vs book: Same name `even_odd_merge`, but a DIFFERENT METHOD. The book uses two dummy heads, a `tails` list and a `turn ^= 1` indicator. The file uses interleaved `even`/`odd` pointer relinking with a saved `odd_head` and no dummy nodes. Output and O(n)/O(1) bounds are the same. Helpers added. Old hint text was wrong and was replaced with the book's hint ("Use temporary additional storage.").
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_07_linked_lists/pg_094_linked_list_palindrome.py
- Exercise: 7.11 Test Whether a Singly Linked List Is Palindromic, printed pages 94–95
- Code vs book: Same name. The file uses a nested `reverse()` instead of the book's external `reverse_linked_list`. The compare loop is driven by `second is not None` and uses answer/break instead of `return False`. The file also re-reverses the second half to restore the input, which the book only mentions as possible. The `__main__` block prints only and has no asserts. Helpers added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_07_linked_lists/pg_095_list_pivot.py
- Exercise: 7.12 Implement List Pivoting, printed pages 95–96
- Code vs book: Book `list_pivoting(L, x)` is `list_pivot(head, pivot)`. The book's six named head/iter variables and if/elif/else chain are replaced by lists `dummy`/`tail` and a nested conditional expression for the index. The file detaches each node as it goes (the book instead sets `greater_iter.next = None` at the end), and the join step uses a conditional on whether the equal region is empty. Helpers added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_07_linked_lists/pg_096_add_list_based_integers.py
- Exercise: 7.13 Add List-Based Integers, printed page 96
- Code vs book: Same name `add_two_numbers` (params `a, b`). The book's single `val = carry + (L1.data if L1 else 0) + ...` expression and conditional-expression advances are replaced by `total` with two if-blocks. `val % 10` / `val // 10` are replaced by `divmod(total, 10)`, and `place_iter`/`dummy_head` are renamed `tail`/`dummy`. Helpers added.
- Needs PDF review: none
- check_code_unchanged: OK

## Summary
- Files done: 13/13; all check_code_unchanged OK; no FAIL.
- Files with code differences from the book: 13 (all; mostly renames, the dataclass ListNode, added guards and helpers; substantive structural differences in 7.3 (variant program used as primary in has_cycle_nodes), 7.5 (restructured case order), 7.10 (different relinking method), 7.11 (restores list), 7.12 (list-of-tails form)).
- NEEDS PDF REVIEW items: none.

### src/epi_python/chapter_08_stacks_and_queues/pg_098_stack_with_max.py
- Exercise: 8.1 Implement a stack with max API, printed pages 98–100
- Code vs book: Both book programs present. Program 1 `Stack`: `push(self, x)` renamed `push(self, value: int)`, cached max computed into a separate local `maximum`, return-type hints added. Program 2 (book also `Stack`) renamed `StackWithCount`; `MaxWithCount.__init__` parameter `max` renamed `maximum` with hints and separate assignments; `empty` uses `not self._element`; push/pop use `value`/`current_maximum`/a record reference `maximum` instead of `x`/`pop_element`/`current_max` with repeated `[-1]` indexing; method order push before pop; attribute type hints added. Extra helper `stack_max_history` not in book.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_08_stacks_and_queues/pg_101_evaluate_rpn.py
- Exercise: 8.2 Evaluate RPN expressions, printed page 101
- Code vs book: Book `evaluate(RPN_expression)` uses a `DELIMITER` constant and an `OPERATORS` dict of lambdas applied to two pops in one statement; file `evaluate_rpn(expression: str) -> int` uses a literal "," split, a set-membership test and an if/elif chain with explicit `right`/`left` locals, list renamed `stack` with type hint. Same arithmetic (int(x / y) truncation) and result.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_08_stacks_and_queues/pg_102_is_well_formed.py
- Exercise: 8.3 Test a string over "{,},(,),[,]" for well-formedness, printed page 102
- Code vs book: Book `is_well_formed(s)` uses `left_chars` and a left->right `lookup` dict, pushing when `c in lookup` and otherwise popping; file uses parameter `brackets: str`, a right->left `matching` dict, `stack`, and `character in '([{'`. Behavioural difference only for non-bracket characters: book returns False on them, file ignores them.
- Needs PDF review: page 102, second "not well-formed" example reads "()" at scan resolution (would be well-formed; possibly a misprint or a different string).
- check_code_unchanged: OK

### src/epi_python/chapter_08_stacks_and_queues/pg_102_shortest_equivalent_path.py
- Exercise: 8.4 Normalize pathnames, printed pages 102–103
- Code vs book: Same name and stack idea. Book pushes '/' onto `path_names` for absolute paths, filters with a generator expression, raises ValueError('Path error') when '..' meets '/', and strips a leading '//' via `result[result.startswith('//'):]`; file uses a boolean `absolute`, list `pieces`, `continue` filtering, reordered '..' branches, different error messages, and builds '/' + join. Behavioural difference: relative path reducing to nothing returns '.' in file vs '' in book.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_08_stacks_and_queues/pg_103_sunset_view.py
- Exercise: 8.5 Compute buildings with a sunset view, printed pages 103–104
- Code vs book: SIGNIFICANT. The book's stack program (namedtuple `BuildingWithHeight`, stack `candidates`, `enumerate`, pop while `>=`, return ids of `reversed(candidates)`) is missing. The file's `examine_buildings_with_sunset(heights: list[int])` is a reverse scan with a running maximum (the book's brute-force idea) returning `[::-1]`. Same selected index set, but order differs (book [5, 4, 2] vs file [2, 4, 5] for [3,7,8,3,6,1]); file needs a list, not a stream; file docstring describes direction differently (west-to-east / toward east).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_08_stacks_and_queues/pg_106_binary_tree_depth_order.py
- Exercise: 8.6 Compute binary tree nodes in order of increasing depth, printed pages 106–107
- Code vs book: Book `binary_tree_depth_order(tree)` rebuilds a per-level Python list with comprehensions; file `binary_tree_depth_order(root: TreeNode | None)` uses a single `collections.deque` with popleft and a `range(len(queue))` inner loop (extra import). Same output. Not in book: `TreeNode` import from chapter 9 file and helper `depth_order_values`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_08_stacks_and_queues/pg_107_circular_queue.py
- Exercise: 8.7 Implement a circular queue, printed pages 107–108
- Code vs book: Book `class Queue` with `SCALE_FACTOR = 2`, fields `_head`, `_tail`, `_num_queue_elements`, slice-concatenation reorder on resize, `+=` extension, dequeue not clearing slot. File `CircularQueue(capacity: int = 1)` adds default and ValueError validation, drops `_tail` (computed) and `SCALE_FACTOR` (doubling hard-coded), renames count `_size`, reorders via modulo list comprehension, clears dequeued slot, different error message. Helper `circular_queue_roundtrip` not in book.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_08_stacks_and_queues/pg_108_queue_from_stacks.py
- Exercise: 8.8 Implement a queue using stacks, printed pages 108–109
- Code vs book: Same algorithm and class name. Attributes `_enq`/`_deq` renamed `_incoming`/`_outgoing` (separate assignments), parameter `x` renamed `item: int`, type hints added, error message 'dequeue from empty queue' vs 'empty queue', book's code comments absent. Helper `queue_from_stacks` not in book.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_08_stacks_and_queues/pg_109_queue_with_max.py
- Exercise: 8.9 Implement a queue with max API, printed pages 109–111
- Code vs book: Both book programs present. Program 1 `QueueWithMax`: fields `_entries`/`_candidates_for_max` renamed `_queue`/`_max_candidates`, `from collections import deque`, parameter `value: int`, guard-clause raises with different messages. Program 2 (book also `QueueWithMax`) renamed `QueueWithMaxTwoStacks`, stacks `_enqueue`/`_dequeue` renamed `_incoming`/`_outgoing`, max written as nested if instead of conditional expression; imports repository `Stack` from pg_098. Helper `queue_max_history` not in book.
- Needs PDF review: none (note: Figure 8.4's last panel prints Q = 3,2,0,1,2,4,4, inconsistent with the previous panel; recorded as printed and flagged as an apparent book misprint in the docstring)
- check_code_unchanged: OK

### src/epi_python/chapter_10_heaps/pg_134_merge_sorted_arrays.py
- Exercise: 10.1 Merge sorted files, printed pages 134–135
- Code vs book: Both book programs present with the same names. `merge_sorted_arrays`: parameter `sorted_arrays` renamed `sorted_lists: list[list[int]]`, locals renamed (`iterators`, `first`, `smallest`, `source_index`, `upcoming`), iterator indexed inline instead of separate `smallest_array_iter`, type hints added, book comments omitted. `merge_sorted_arrays_pythonic`: same body, parameter renamed with hints.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_10_heaps/pg_135_sort_increasing_decreasing_array.py
- Exercise: 10.2 Sort an increasing-decreasing array, printed pages 135–136
- Code vs book: Book program 1 uses `INCREASING, DECREASING = range(2)`, loops to `len(A) + 1`, ends increasing runs on `>=`, reverses with `A[i - 1:start_idx - 1:-1]`, and merges with 10.1's `merge_sorted_arrays`; file (`values: list[int]`) uses a boolean flag, explicit empty check, strict `<`/`>` run boundaries, `[::-1]` reversal, last run appended after loop, and `heapq.merge`. Same sorted result. Book program 2 `sort_k_increasing_decreasing_array_pythonic` (nested `Monotonic` callable + `itertools.groupby`) is MISSING from the file.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_10_heaps/pg_136_sort_approximately_sorted_array.py
- Exercise: 10.3 Sort an almost-sorted array, printed pages 136–137
- Code vs book: Book takes an iterator `sequence`, pushes the first k items via `itertools.islice` + heappush, then heappushpop for the rest, then pops. File takes `values: list[int], k: int`, heapifies the slice `values[:k+1]` (k+1 items), loops over `values[k+1:]`; no itertools import; requires a list rather than a stream. Same sorted output.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_10_heaps/pg_137_k_closest_stars.py
- Exercise: 10.4 Compute the k closest stars, printed pages 137–139
- Code vs book: SIGNIFICANT. Book's `Star` class (`distance` property via `math.sqrt`, `__lt__`) and explicit max-heap of `(-distance, star)` with pop at k+1 and `heapq.nlargest` return are MISSING. File uses plain (x, y, z) tuples and a single `heapq.nsmallest(k, stars, key=squared distance)` call, adds ValueError for k < 0, returns closest first. Also noted: book's comment says result is "furthest to closest", but nlargest over (-distance, star) appears to yield closest first (for user review).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_10_heaps/pg_139_online_median.py
- Exercise: 10.5 Compute the median of online data, printed pages 139–140
- Code vs book: Same two-heap idea. Book `online_median(sequence)` routes x through `min_heap` via heappushpop, keeps the extra element in the min-heap (larger half), returns `min_heap[0]` (int) for odd counts and `0.5 * (...)` for even. File (`values: list[int] -> list[float]`, heaps `smaller`/`larger`) pushes into the negated lower half first (heappush + heappop), keeps the extra element in the lower half, returns `float(-smaller[0])` / `(...)/2`. Same median values; file always returns floats.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_10_heaps/pg_140_k_largest_in_binary_heap.py
- Exercise: 10.6 Compute the k largest elements in a max-heap, printed pages 140–141
- Code vs book: Same algorithm and name. Parameters `A, k` renamed `max_heap: list[int], k: int`; book returns [] for k <= 0, file raises ValueError unless 0 <= k <= len (book does not check k > len); candidate list built directly; popped pair unpacked instead of peeking `[0][1]` first; children handled in one loop over a tuple; result renamed `answer`; book comments omitted.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_09_binary_trees/pg_114_is_balanced_binary_tree.py
- Exercise: 9.1 Test if a binary tree is height-balanced, printed pages 114–116
- Code vs book: differs. Book uses `is_balanced_binary_tree(tree)` with nested `check_balanced` returning a `collections.namedtuple` BalancedStatusWithHeight (empty -> (True, -1)). File puts the algorithm in `is_balanced_nodes(root: TreeNode | None)` with nested `height(node)` returning an int (-1 = unbalanced sentinel, empty height 0), merges the right-subtree and difference checks, no namedtuple; `is_balanced_binary_tree` is reused for a tuple-to-TreeNode adapter not in the book; own `TreeNode` dataclass; type hints added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_09_binary_trees/pg_116_is_symmetric_binary_tree.py
- Exercise: 9.2 Test if a binary tree is symmetric, printed pages 116–117
- Code vs book: minor differences. Book `is_symmetric(tree)` / nested `check_symmetric(subtree_0, subtree_1)` with separate both-empty / both-present / return False branches; file `is_symmetric_nodes(root)` / nested `mirrored(left, right)` merges the empty cases into `return left is right`. Same logic. File adds tuple adapter `is_symmetric_binary_tree`, own `TreeNode` dataclass, type hints.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_09_binary_trees/pg_117_lowest_common_ancestor.py
- Exercise: 9.3 Compute the lowest common ancestor in a binary tree, printed pages 117–118
- Code vs book: SEMANTIC difference. Book `lca(tree, node0, node1)` identifies targets by node identity (`tree is node0`) and uses namedtuple Status; file `lowest_common_ancestor(root, a: int, b: int)` matches targets by key value (`node.data in (a, b)`) and returns a plain tuple. Differs on duplicate keys and when a == b (book counts 2 for node0 is node1; file counts 1). Old docstring wrongly claimed identity was used. Helpers `build_tree`, `nested_tree`, `lca_value` not in book; TreeNode imported from 9.1 module.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_09_binary_trees/pg_118_lca_with_parent.py
- Exercise: 9.4 Compute the LCA when nodes have parent pointers, printed pages 118–119
- Code vs book: restructured. Book `lca(node_0, node_1)` with `get_depth`, swaps only nodes, then `depth_diff = abs(...)` decrement loop; file `lca_with_parent(a, b)` with `depth`, swaps nodes and depths, climbs with `for _ in range(depth_a - depth_b)`. Tandem loop identical. Added `ParentNode` dataclass, `build_parent_tree`, `find_node`, `lca_parent_value`; type hints.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_09_binary_trees/pg_119_sum_root_to_leaf_paths.py
- Exercise: 9.5 Sum the root-to-leaf paths in a binary tree, printed pages 119–120
- Code vs book: book `sum_root_to_leaf(tree, partial_path_sum=0)` uses `* 2 + tree.data`; file `sum_root_to_leaf(root, partial=0)` uses `(partial << 1) | root.data` and adds a ValueError check for non-0/1 values (not in book). Helpers `build_tree`, `nested_tree`, `sum_root_to_leaf_paths` added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_09_binary_trees/pg_120_has_path_sum.py
- Exercise: 9.6 Find a root to leaf path with specified sum, printed page 120
- Code vs book: book `has_path_sum(tree, remaining_weight)` compares leaf `remaining_weight == tree.data`; file `has_path_sum(root, target)` computes `remainder = target - root.data` first and tests `remainder == 0` at a leaf. Equivalent. Helpers `build_tree`, `nested_tree`, `has_path_sum_values` added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_09_binary_trees/pg_121_inorder_traversal.py
- Exercise: 9.7 Implement an inorder traversal without recursion, printed page 121
- Code vs book: same loop. Book `inorder_traversal(tree)` reuses `tree` as the pointer with `s, result`; file `inorder_nodes(root)` uses `stack`, `current`, `result` and `is not None` tests. Name `inorder_traversal` reused for a tuple adapter (not in book). Own `TreeNode` dataclass; type hints.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_09_binary_trees/pg_121_preorder_without_recursion.py
- Exercise: 9.8 Implement a preorder traversal without recursion, printed pages 121–122
- Code vs book: book `preorder_traversal(tree)` pushes both children unconditionally (`path += [curr.right, curr.left]`) and skips None on pop; file returns [] early for empty tree and pushes only non-None children with two appends. Same order. Helpers `build_tree`, `nested_tree`, `preorder_values` added. (Book has no hint for 9.8; the old docstring had invented one, removed.)
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_09_binary_trees/pg_122_kth_node_inorder.py
- Exercise: 9.9 Compute the kth node in an inorder traversal, printed pages 122–123
- Code vs book: book `find_kth_node_binary_tree(tree, k)` tests `left_size + 1 < k` (right), `left_size == k - 1` (return), else left; file `kth_node_inorder(root, k)` tests return / left / right in a different order. Same logic. Added `SizeNode` dataclass, `make_size_tree`, `kth_inorder_value`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_09_binary_trees/pg_123_inorder_successor.py
- Exercise: 9.10 Compute the successor, printed pages 123–124
- Code vs book: book `find_successor(node)`; file `inorder_successor(node)` adds a `node is None` guard and uses explicit `is not None` tests; otherwise identical. `inorder_successor_value` added; ParentNode/build_parent_tree/find_node imported from 9.4 module.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_09_binary_trees/pg_124_morris_inorder.py
- Exercise: 9.11 Implement an inorder traversal with O(1) space, printed pages 124–125
- Code vs book: DIFFERENT ALGORITHM. Book `inorder_traversal(tree)` uses parent fields with a `prev` pointer and three cases, never modifying the tree. File `inorder_constant_space(root)` is a Morris traversal on nodes without parent fields (temporarily threads `predecessor.right`). The book's implementation is missing from the file; the file name refers to Morris. Old docstring's hint and variant did not match the book (replaced). Helpers `build_tree`, `nested_tree`, `morris_values` added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_09_binary_trees/pg_125_reconstruct_from_traversals.py
- Exercise: 9.12 Reconstruct a binary tree from traversal data, printed pages 125–127
- Code vs book: same hash-table idea, different recursion. Book `binary_tree_from_preorder_inorder(preorder, inorder)` helper takes preorder and inorder start/end ranges and computes `left_subtree_size`; file `reconstruct_from_preorder_inorder` nested `construct(lo, hi)` takes only the inorder range and consumes preorder via a `nonlocal position` counter. File adds ValueError validation (length/key-set mismatch, duplicates). Helpers `build_tree`, `nested_tree`, `reconstruct_tree` added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_09_binary_trees/pg_127_reconstruct_preorder_markers.py
- Exercise: 9.13 Reconstruct a binary tree from a preorder traversal with markers, printed pages 127–128
- Code vs book: book `reconstruct_preorder(preorder)` passes the iterator as a helper parameter with no error handling; file `reconstruct_preorder_with_null` keeps the iterator in an enclosing variable used by parameterless `read()`, raises ValueError on truncation and on trailing non-None values (a trailing None is not detected). Helpers `build_tree`, `nested_tree`, `reconstruct_marked_tree` added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_09_binary_trees/pg_128_binary_tree_leaves_list.py
- Exercise: 9.14 Form a linked list from the leaves of a binary tree, printed page 128
- Code vs book: book `create_list_of_leaves(tree)` returns a Python list of leaf tree nodes by recursive list concatenation; file `create_list_of_leaves(root)` returns a singly linked list of new `ListNode`s holding leaf data (dummy head, nested `visit`, `nonlocal tail`), importing `ListNode` from chapter 7 mid-module. Helpers `build_tree`, `nested_tree`, `leaf_values` added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_09_binary_trees/pg_128_exterior_binary_tree.py
- Exercise: 9.15 Compute the exterior of a binary tree, printed pages 128–129
- Code vs book: restructured. Book `exterior_binary_tree(tree)` uses `is_leaf`, recursive `left_boundary_and_leaves(subtree, is_boundary)` and `right_boundary_and_leaves(subtree, is_boundary)` returning nodes; file returns data values, special-cases a single node, walks boundaries with while loops, collects leaves with a separate `leaves` helper, and uses `extend(reversed(...))` for the right boundary. Helpers `build_tree`, `nested_tree`, `exterior_values` added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_09_binary_trees/pg_129_right_sibling_tree.py
- Exercise: 9.16 Compute the right sibling tree, printed pages 129–131
- Code vs book: book `construct_right_sibling(tree)` with nested `populate_children_next_field(start_node)`, sets `start_node.right.next = start_node.next and start_node.next.left`, returns nothing; file inlines the helper as nested loops, uses an `if current.next is not None` guard, and returns the root. Added `SiblingNode` dataclass, `make_sibling_tree`, `sibling_pairs` (uses collections.deque for checking only).
- Needs PDF review: none
- check_code_unchanged: OK

## Summary
- Files done: 16/16; all check_code_unchanged OK.
- Files with code differences from the book: 16 (none matches the listing exactly). Most significant: pg_124 (Morris traversal instead of the book's parent-field algorithm; book implementation missing) and pg_117 (targets matched by key value rather than node identity).
- NEEDS PDF REVIEW items: none.

### src/epi_python/chapter_11_searching/pg_145_search_first_of_k.py
- Exercise: 11.1 Search a sorted array for first occurrence of k, printed pages 145–146
- Code vs book: Params renamed (`sorted_array: list[int]`, `key: int`), hints added, `mid` -> `middle`, `result` initialised separately; book's `>` / `==` branches merged into one `>= key` branch with a nested `== key` test. Same behaviour.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_11_searching/pg_146_search_entry_equal_to_index.py
- Exercise: 11.2 Search a sorted array for entry equal to its index, printed pages 146–147
- Code vs book: Function renamed from `search_entry_equal_to_its_index` to `search_entry_equal_to_index`; param `sorted_distinct: list[int]`; no `difference` variable (compares `A[middle]` with `middle` directly); `if`/`if`/`else` instead of `if`/`elif`/`else`. Same behaviour.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_11_searching/pg_147_search_smallest.py
- Exercise: 11.3 Search a cyclically sorted array, printed pages 147–148
- Code vs book: Param renamed `cyclic_sorted`, hints added, `mid` -> `middle`; extra empty-list guard returning -1 (the book's code would return 0).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_11_searching/pg_148_square_root.py
- Exercise: 11.4 Compute the integer square root, printed pages 148–149
- Code vs book: Adds a ValueError for negative k; no `mid_squared` variable; keeps a separate `result` (the last good midpoint) and returns it instead of `left - 1` (same value).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_11_searching/pg_149_real_square_root.py
- Exercise: 11.5 Compute the real square root, printed pages 149–150
- Code vs book: Book loops `while not math.isclose(left, right)` and returns `left`. File has no `math` import, an added `tolerance=1e-12` parameter, a custom relative-width stopping test, a ValueError for negative input, an early return for 0 and 1, and it returns the midpoint. The bracket choice matches the book.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_11_searching/pg_150_matrix_search.py
- Exercise: 11.6 Search in a 2D sorted array, printed pages 150–152
- Code vs book: Params renamed (`matrix`, `target`), hints added; empty-matrix guard added; local `value`; branch test reversed (`value > target` moves left, otherwise moves down). Same behaviour.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_11_searching/pg_152_find_min_max.py
- Exercise: 11.7 Find the min and max simultaneously, printed pages 152–153
- Code vs book: Book's `MinMax` namedtuple, the `collections` import and the nested `min_max` helper are missing. The file uses `sorted()` on pairs and returns a plain tuple. It handles odd length up front, not after the loop. It adds a ValueError for empty input (the book's code would raise IndexError).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_11_searching/pg_153_kth_largest_element.py
- Exercise: 11.8 Find the kth largest element, printed pages 153–155
- Code vs book: The book's randomized algorithm is `find_kth_largest_pdf`. Its nested `find_kth`/`partition_around_pivot` are flattened into one `partition(..., compare)` helper. It also adds an `rng` parameter, ValueError/RuntimeError, and renamed variables. The file's `find_kth_largest` (the book's name) is a separate middle-pivot Hoare-style quickselect that is NOT in the book.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_11_searching/pg_155_find_missing_ip.py
- Exercise: 11.9 Find the missing IP address, printed pages 155–156
- Code vs book: Book's function is `find_missing_element(stream)` and reads the stream twice with `itertools.tee`. The file's `find_missing_ip` takes configurable bit widths (defaults 16/8) and re-reads the input through a callable or `lambda: iter(...)` factory. It adds validation errors, uses a `bytearray` bitmap and `seen.index(0)`, and renames variables. The extra `find_missing_ip_32bit` wrapper (not in the book) uses the book's 32/16 settings.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_11_searching/pg_157_find_duplicate_missing.py
- Exercise: 11.10 Find the duplicate and missing elements, printed pages 157–158
- Code vs book: Book's `DuplicateAndMissing` namedtuple and `functools.reduce` are missing; the file uses an explicit XOR loop. It isolates the lowest set bit with `x & -x` (the book uses `x & ~(x - 1)`). Membership is tested with `values.count(c) == 2` (the book uses `in A`). It adds ValueError guards, renames variables and returns a plain tuple.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_12_hash_tables/pg_163_can_form_palindrome.py
- Exercise: 12.1 Test for palindromic permutations, printed pages 163–164
- Code vs book: Param `text: str` and hints added; Counter split into a separate variable `counts`. Same one-line logic.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_12_hash_tables/pg_165_isbn_lru_cache.py
- Exercise: 12.3 Implement an ISBN cache, printed pages 165–166
- Code vs book: Uses `from collections import OrderedDict`. Attributes are `capacity`/`_prices` (book: `_capacity`/`_isbn_price_table`). Recency is refreshed with `move_to_end` instead of pop and re-insert. `insert` adds first and then evicts when over capacity (the book evicts first, then inserts). Adds a ValueError for capacity <= 0. The extra helper `cache_lookup_history` is not in the book.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_12_hash_tables/pg_166_lca_close_ancestors.py
- Exercise: 12.4 Compute the LCA, optimizing for close ancestors, printed pages 166–167
- Code vs book: Book's `lca(node_0, node_1)` is renamed `lca_close_ancestors(a, b)`. The visited set stores `id(node)` because the repo's dataclass ParentNode is unhashable. It uses `is not None` tests and returns None where the book raises ValueError. ParentNode and the helpers are imported from Chapter 9. The extra wrapper `lca_close_value` is not in the book.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_12_hash_tables/pg_167_find_nearest_repetition.py
- Exercise: 12.5 Find the nearest repeated entries in an array, printed pages 167–168
- Code vs book: Param `words: list[str]`; variables renamed; no `latest_equal_word` temporary; result wrapped in `int()`. Same algorithm.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_12_hash_tables/pg_168_smallest_subarray_covering_set.py
- Exercise: 12.6 Find the smallest subarray covering all values, printed pages 168–171
- Code vs book: The first program is renamed `smallest_subarray_covering_set` and has no `Subarray` namedtuple. It returns None when nothing covers the set (book: (-1, -1)) and (0, -1) for an empty set. It tests the count before decrementing. The book's second, streaming program `find_smallest_subarray_covering_subset` (doubly linked list) is MISSING from the file.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_12_hash_tables/pg_171_smallest_subarray_sequential_cover.py
- Exercise: 12.7 Find smallest subarray sequentially covering all values, printed pages 171–172
- Code vs book: No `Subarray` namedtuple; returns a tuple or None. Adds (0, -1) for an empty query and a ValueError for duplicate keywords. Uses `dict.get` plus `continue`. No `shortest_distance` or `distance_to_previous_keyword` variables; the best is compared via the stored result instead (equivalent).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_12_hash_tables/pg_173_longest_subarray_with_distinct_entries.py
- Exercise: 12.8 Find the longest subarray with distinct entries, printed pages 173–174
- Code vs book: Equivalent sliding-window form. It sets `begin = max(begin, last + 1)` and updates `best` every step. The book defers the update until a duplicate is seen and does a final `max(result, len(A) - start)`. Variables are renamed.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_12_hash_tables/pg_174_longest_contained_interval.py
- Exercise: 12.9 Find the length of a longest contained interval, printed pages 174–175
- Code vs book: Variables renamed. A `length` counter replaces `upper_bound - lower_bound - 1`. Same algorithm.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_12_hash_tables/pg_175_string_decompositions.py
- Exercise: 12.10 Compute all string decompositions, printed pages 175–176
- Code vs book: Book has a nested `match_all_words_in_dict` helper with early exit. The file instead slices each window into pieces and compares `Counter(pieces) == target`, with no early exit. It adds guards and a ValueError for unequal word lengths, and uses an explicit loop instead of a list comprehension.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_12_hash_tables/pg_176_collatz_conjecture.py
- Exercise: 12.11 Test the Collatz conjecture, printed pages 176–177
- Code vs book: Book's `test_collatz_conjecture` is renamed `collatz_holds_to`. It starts from 2 (book: 3). It caches every value on each converging path in `verified` (book: odd numbers only). The loop condition is `current not in verified` (book: `test_i >= i` plus a `break` on verified odd numbers). Parity uses `& 1`, and a ValueError is added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_12_hash_tables/pg_177_chess_zobrist_hash.py
- Exercise: 12.12 Implement a hash function for chess, printed pages 177–179
- Code vs book: The book prints no program. `ChessHash` and `chess_board_hash` are the repository's own Zobrist implementation. Unlike the book's 13-state scheme, blank squares have no code. Codes are seeded 64-bit values and the board size is configurable.
- Needs PDF review: none
- check_code_unchanged: OK

## Summary
- Files done: 21 of 21; all `check_code_unchanged` OK; no unresolved FAIL.
- Files whose code differs from the book's listing: all 21. 12.1 differs only cosmetically (renames, type hints and a split-out variable). 12.12 has no book listing to compare against.
- Book implementations missing from files: 12.6's streaming `find_smallest_subarray_covering_subset`. Book namedtuple wrappers were dropped in 11.7, 11.10, 12.6 and 12.7.
- Non-book functions in files: 11.8 `find_kth_largest` (middle-pivot quickselect under the book's name), 11.9 `find_missing_ip_32bit`, 12.3 `cache_lookup_history`, 12.4 `lca_close_value`, and 12.12 (all of its code, because the book has none).
- NEEDS PDF REVIEW items: none.

### src/epi_python/chapter_13_sorting/pg_182_intersect_two_sorted_arrays.py
- Exercise: 13.1 Compute the intersection of two sorted arrays, printed pages 182–183
- Code vs book: book has three listings all named `intersect_two_sorted_arrays(A, B)`. Brute-force one-liner is missing from the file. Binary-search version renamed `intersect_two_sorted_arrays_bisect`, uses `from bisect import bisect_left`, explicit loop instead of comprehension + nested `is_present`, dedup via `result[-1]` instead of `A[i-1]`, and adds a swap to iterate the shorter list (book only suggests this in prose). Linear sweep: lowercase typed params, output named `result` instead of `intersection_A_B`, dedup via `result[-1]` instead of `A[i-1]`; same behaviour.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_13_sorting/pg_183_merge_two_sorted_arrays.py
- Exercise: 13.2 Merge two sorted arrays, printed pages 183–184
- Code vs book: same name and parameters `(A, m, B, n)`; file adds type hints and an extra `ValueError` input-validation check not in the book. Merge loops identical to the book.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_13_sorting/pg_184_eliminate_duplicate_names.py
- Exercise: 13.3 Remove first-name duplicates, printed pages 184–185
- Code vs book: book's hand-written `Name` class with first-name-only `__eq__` and `__lt__` is replaced by a `@dataclass` (all-field `__eq__`, no `__lt__`). Book `eliminate_duplicate(A)` uses `A.sort()` and `cand != A[write_idx - 1]`; file uses `names.sort(key=lambda ...)`, explicit `.first_name` comparison, renamed variables, type hints, and an early return for empty input. Same behaviour.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_13_sorting/pg_185_smallest_nonconstructible_value.py
- Exercise: 13.4 Smallest nonconstructible value, printed pages 185–186
- Code vs book: book param `A`, tracks `max_constructible_value` from 0 and returns it + 1; file param `coins: list[int]`, stores `sorted` copy in `ordered`, tracks `smallest_missing` from 1 (= book value + 1). Equivalent.
- Needs PDF review: none (book's problem sentence has typo "not to the sum", quoted with [sic])
- check_code_unchanged: OK

### src/epi_python/chapter_13_sorting/pg_186_find_max_simultaneous_events.py
- Exercise: 13.5 Render a calendar, printed pages 186–188
- Code vs book: `Event` namedtuple same (imported via `from collections import namedtuple`); book's `Endpoint` namedtuple absent, file uses `(time, 0/1)` tuples and plain `endpoints.sort()` instead of `key=lambda e: (e.time, not e.is_start)`; loop/append instead of comprehensions; added ValueError check; counters renamed `active`/`maximum`, max updated after every endpoint. Same results.
- Needs PDF review: none (Figure 13.1 interval coordinates not transcribed; only caption quoted)
- check_code_unchanged: OK

### src/epi_python/chapter_13_sorting/pg_188_add_interval.py
- Exercise: 13.6 Merging intervals, printed pages 188–189
- Code vs book: book's `Interval` namedtuple absent (file uses plain tuples with `[0]`/`[1]`); type hints; added ValueError for reversed interval; Stage 2 updates `new_start`/`new_end` instead of a new `Interval`; result built via `append`/`extend` instead of `result + [new_interval] + disjoint_intervals[i:]`. Same results.
- Needs PDF review: none (book's worked example says "[1,8] to [0,9]" where [0,8] is meant; noted in docstring)
- check_code_unchanged: OK

### src/epi_python/chapter_13_sorting/pg_189_union_of_intervals.py
- Exercise: 13.7 Compute the union of intervals, printed pages 189–191
- Code vs book: book `Endpoint` namedtuple `('is_closed','val')` -> frozen dataclass `(value, is_closed)`; book `Interval` class with `__lt__` -> frozen dataclass without `__lt__`, ordering via `sorted(key=...)` (copy rather than in-place `intervals.sort()`); merge loop keeps a separate `current` and builds new `Interval`s instead of mutating `result[-1].right`; extension test adds `not right.is_closed`; helper `closed()` added (not in book). Same results.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_13_sorting/pg_191_group_by_age.py
- Exercise: 13.8 Partitioning and sorting an array with many repeated entries, printed pages 191–192
- Code vs book: `Person` namedtuple -> dataclass; `collections.Counter` replaced by a plain dict with `dict.get`; loop variables renamed (`from_index`, `person_age`, `destination`); offset update written as `== 0` -> delete / else `+= 1` instead of `if count: offset = to_idx + 1 else del`. Type hints added. Same behaviour.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_13_sorting/pg_193_team_photo_day.py
- Exercise: 13.9 Team photo day—1, printed pages 193–194
- Code vs book: book has `class Team` with nested `Player` namedtuple, `_players` list, and `@staticmethod valid_placement_exists(A, B)` checking only "A in front of B". File has no Team/Player class; module-level function over plain `list[int]` heights, adds an unequal-length check, and returns True if either orientation works.
- Needs PDF review: none (Figures 13.3/13.4 are pictures; captions quoted)
- check_code_unchanged: OK

### src/epi_python/chapter_13_sorting/pg_194_stable_sort_linked_list.py
- Exercise: 13.10 Implement a fast sorting algorithm for lists, printed pages 194–195
- Code vs book: book's `insertion_sort(L)` listing is missing from the file. `stable_sort_list`: param `head` with type hints, midpoint via `slow, fast = head, head.next` instead of `pre_slow/slow/fast`, merge (Solution 7.1 `merge_two_sorted_lists`) written inline; own `ListNode` dataclass; helpers `to_linked`/`to_list` added. Old "PDF-CHECKED LEARNING NOTES" block removed (its stated variant and example were not in the book).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_13_sorting/pg_195_find_salary_cap.py
- Exercise: 13.11 Compute a salary threshold, printed pages 195–196
- Code vs book: type hints; added ValueError for negatives, empty-list case, explicit early `-1.0` when target > sum; sorts a copy with `sorted()` instead of in-place `.sort()`; variables renamed; comparison written `target <= possible`; final `return max(sorted_salaries)` (unreachable) instead of `return -1.0`. Same results for valid inputs. Old "PDF-CHECKED LEARNING NOTES" block (with non-book example) removed.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_14_binary_search_trees/pg_199_is_binary_tree_bst.py
- Exercise: 14.1 Test if a binary tree satisfies the BST property, printed pages 199–201
- Code vs book: both book listings are named `is_binary_tree_bst`. Recursive version is `is_bst_nodes` (nested `valid` helper instead of default range params). BFS version is `is_bst_nodes_bfs` (plain tuples instead of `QueueEntry` namedtuple, `append` instead of `+=`). The file's `is_binary_tree_bst(tree: tuple)` is an added nested-tuple adapter, not the book's function. Own `TreeNode` dataclass. Inorder approach has no listing in book or file. Old "PDF-CHECKED LEARNING NOTES" block removed.
- Needs PDF review: none (book's BFS walkthrough names B's children "C" and "D" although Figure 14.1 shows B's right child as F; noted as printed)
- check_code_unchanged: OK

### src/epi_python/chapter_14_binary_search_trees/pg_201_find_first_greater_than_k.py
- Exercise: 14.2 Find the first key greater than a given value in a BST, printed pages 201–202
- Code vs book: matches the book's listing apart from added type hints (uses shared `BSTNode` from `bst_nodes.py`). Old "PDF-CHECKED LEARNING NOTES" block removed.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_14_binary_search_trees/pg_202_find_k_largest_in_bst.py
- Exercise: 14.3 Find the k largest elements in a BST, printed pages 202–203
- Code vs book: helper renamed from `find_k_largest_in_bst_helper(tree)` to `helper(subtree)`, list renamed from `k_largest_elements` to `result` (created before the helper), type hints added. Logic the same. Old "PDF-CHECKED LEARNING NOTES" block removed.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_14_binary_search_trees/pg_203_find_lca_in_bst.py
- Exercise: 14.4 Compute the LCA in a BST, printed pages 203–204
- Code vs book: book `find_LCA(tree, s, b)` with outer while and two inner while loops; file `find_lca_in_bst(tree, smaller, bigger)` with type hints, sorts the two keys (order-independent), single loop with if/elif/else, returns None if it runs off the tree. Same result for valid inputs. Old "PDF-CHECKED LEARNING NOTES" block removed.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_14_binary_search_trees/pg_204_rebuild_bst_from_preorder.py
- Exercise: 14.5 Reconstruct a BST from traversal data, printed pages 204–206
- Code vs book: book's first (slicing, O(n^2) worst case) `rebuild_bst_from_preorder` listing is missing. Second listing: nested helper renamed `within_range` (book `rebuild_bst_from_preorder_on_value_range`), variables renamed, type hints, and the range test is strict `lower < key < upper` instead of the book's inclusive `lower_bound <= root <= upper_bound` (same results for distinct keys). Old "PDF-CHECKED LEARNING NOTES" block removed.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_14_binary_search_trees/pg_206_find_closest_elements_in_sorted_arrays.py
- Exercise: 14.6 Find the closest entries in three sorted arrays, printed pages 206–207
- Code vs book: different library: book uses third-party `bintrees.RBTree` keyed by `(value, idx)` holding iterators (`insert`, `min_key`, `max_key`, `pop_min`); file uses stdlib `heapq` with `(value, array_index, position)` tuples and a separately tracked `current_max`. Same O(n log k). File uses indices instead of iterators, raises ValueError on empty arrays (book skips them), returns `int(...)`, renamed variables, type hints. Code left as is per instruction; difference explained in the comparison block.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_14_binary_search_trees/pg_207_generate_first_k_a_b_sqrt2.py
- Exercise: 14.7 Enumerate numbers of the form a + b sqrt(2), printed pages 207–210
- Code vs book: book's `ABSqrt2` class and the BST (`bintrees.RBTree`) version of `generate_first_k_a_b_sqrt2` are missing. The two-index O(n) version is present but works on plain floats instead of ABSqrt2 objects, uses `from math import sqrt`, adds negative/zero-k checks, and compares candidates with an `epsilon = 1e-12` tolerance instead of exact `==`. Type hints added.
- Needs PDF review: none (book's trace step 5 prints A without the 2.414 added in step 4; noted in docstring)
- check_code_unchanged: OK

### src/epi_python/chapter_14_binary_search_trees/pg_210_build_min_height_bst_from_sorted_array.py
- Exercise: 14.8 Build a minimum height BST from a sorted array, printed page 210
- Code vs book: renames only (`A` -> `values`, helper -> `build`, `mid` -> `middle`) plus type hints; logic identical. Old "PDF-CHECKED LEARNING NOTES" block removed.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_14_binary_search_trees/pg_211_pair_includes_ancestor_and_descendant_of_m.py
- Exercise: 14.9 Test if three BST nodes are totally ordered, printed pages 211–212
- Code vs book: same function and parameter names (plus type hints), but the file implements the book's brute-force idea (nested `proper_ancestor` helper, sequential searches in both orders) rather than the book's printed interleaved-search listing (`search_0`/`search_1` loop + nested `search_target`). The interleaved listing is missing; results are the same but without its O(d) bound. Old "PDF-CHECKED LEARNING NOTES" block removed.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_14_binary_search_trees/pg_212_range_lookup_in_bst.py
- Exercise: 14.10 The range lookup problem, printed pages 212–214 (incl. "Augmented BSTs" discussion on 214)
- Code vs book: book's `Interval` namedtuple and `interval` parameter replaced by two parameters `low`, `high`; helper renamed `helper(node)` (book `range_lookup_in_bst_helper(tree)`); `interval.left > tree.data` written `node.data < low`; type hints. Same behaviour. Old "PDF-CHECKED LEARNING NOTES" block removed.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_14_binary_search_trees/pg_215_clients_credits_info.py
- Exercise: 14.11 Add credits, printed pages 215–216
- Code vs book: different library: book's `bintrees.RBTree` (credit -> set of clients) replaced by a stdlib `heapq` max-heap of `(-credit, client_id)` with lazy deletion in `max`. File's `insert` does not call `remove` first; `remove` only pops from the dict (heap entries go stale); parameters renamed (`c`/`C` -> `credits`); type hints; ties in `max` go to the smallest client id. Old "PDF-CHECKED LEARNING NOTES" block removed.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_15_recursion/pg_219_compute_tower_hanoi.py
- Exercise: 15.1 The Towers of Hanoi problem, printed pages 219–221
- Code vs book: differs. Book `compute_tower_hanoi(num_rings)` with nested `compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg, use_peg)`, module constant `NUM_PEGS = 3`, and an explicit `pegs` list-of-lists simulation (`pegs[to_peg].append(pegs[from_peg].pop())`); moves stored as lists `[from_peg, to_peg]`. File: `compute_tower_hanoi(n: int)` with nested `transfer(count, source, target, spare)`, type hints added, no NUM_PEGS, no peg simulation, moves stored as tuples, guard written as early `if count == 0: return` instead of `if num_rings_to_move > 0:` (negative n would recurse forever in the file). Recursion structure and peg roles match.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_15_recursion/pg_221_n_queens.py
- Exercise: 15.2 Generate all nonattacking placements of n-Queens, printed pages 221–222
- Code vs book: same algorithm. Helper renamed `solve_n_queens` -> `solve`, list `col_placement` -> `placement`, loop variables `i, c` -> `prior_row, prior_col`; type hints added; `result`/`placement` initialized in two statements before the helper instead of the book's single tuple assignment after it; book's inline code comments not reproduced.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_15_recursion/pg_222_permutations.py
- Exercise: 15.3 Generate permutations, printed pages 222–224
- Code vs book: both book programs present but differ. Program 1: book `permutations(A)` / nested `directed_permutations(i)` mutates A in place; file `permutations(values: list[int])` / nested `visit(position)` works on a copy; base case `position == len(remaining)` vs book `i == len(A) - 1` (empty input: book returns [], file [[]]). Program 2: book loops calling `next_permutation(A)` from Solution 5.11 without sorting in the listing; file `permutations_by_next_permutation` sorts first and inlines the next-permutation steps.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_15_recursion/pg_224_generate_power_set.py
- Exercise: 15.4 Generate the power set, printed pages 224–226
- Code vs book: differs. Extra non-book function `generate_power_set` (iterative doubling) reuses the book's name. Book recursive program -> `generate_power_set_recursive` with helper `visit(index, chosen)` using append/pop and `chosen.copy()` instead of the book's `directed_power_set(to_be_selected, selected_so_far)` passing a new concatenated list. Book bit-mask program -> `generate_power_set_by_bits`; book appends the bit index `int(math.log2(...))` to the subset, file appends `values[bit_index]` (the element). Variable renames and type hints added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_15_recursion/pg_226_combinations.py
- Exercise: 15.5 Generate all subsets of size k, printed pages 226–227
- Code vs book: differs. Book helper `directed_combinations(offset, partial_combination)` uses a while loop with pruning `num_remaining <= n - i + 1` and passes new lists `partial_combination + [i]`; file helper `visit(next_value, partial)` uses `for value in range(next_value, n+1)` with no pruning and append/pop on one shared list. Type hints added. Same output.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_15_recursion/pg_227_generate_balanced_parentheses.py
- Exercise: 15.6 Generate strings of matched parens, printed pages 227–228
- Code vs book: same rules, different bookkeeping. Book helper `directed_generate_balanced_parentheses(num_left_parens_needed, num_right_parens_needed, valid_prefix, result=[])` counts parens still needed and collects into a mutable default argument it returns; file helper `visit(opened, closed, text)` counts parens used, appends to an enclosing `results` list, checks completion first with early return. Type hints added. Same output order.
- Needs PDF review: page 228, exact summand of the recurrence C(k+1) = sum_{i=0}^{k} (...)/(k+1) (printed like a binomial).
- check_code_unchanged: OK

### src/epi_python/chapter_15_recursion/pg_228_palindrome_decompositions.py
- Exercise: 15.7 Generate palindromic decompositions, printed pages 228–229
- Code vs book: nearly matches. Both programs present. First: book parameter `input` renamed `text: str`, type hints added, `result` initialized before rather than after the nested helper. Second (Pythonic): matches except type hints.
- Needs PDF review: none (note: book's worked example prints "4451991"/"451991"/"51991", apparently a misprint for the suffixes of "0204451881"; documented in the file).
- check_code_unchanged: OK

### src/epi_python/chapter_15_recursion/pg_229_generate_all_binary_trees.py
- Exercise: 15.8 Generate binary trees, printed pages 229–230
- Code vs book: function body matches the book; file adds type hints and defines its own `BinaryTreeNode` @dataclass (book uses its Chapter 9 class), adding a `dataclasses` import.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_15_recursion/pg_230_solve_sudoku.py
- Exercise: 15.9 Implement a Sudoku solver, printed pages 230–232
- Code vs book: differs in structure. Book nests `valid_to_add(i, j, val)` inside `solve_partial_sudoku`; file defines both side by side. Book `EMPTY_ENTRY = 0` constant vs file local `empty_entry`; book recomputes `int(math.sqrt(len(...)))` per check with `I`/`J`, file uses `math.isqrt(n)` once with `region_i`/`region_j`; file adds a ValueError input check not in the book; type hints added; `val` -> `value`. (Book's "row"/"column" comments are attached to the opposite checks.)
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_15_recursion/pg_232_gray_code.py
- Exercise: 15.10 Compute a Gray code, printed pages 232–233
- Code vs book: differs; one book program missing. Backtracking program renamed `gray_code_backtracking`, history set held in enclosing scope instead of passed as `directed_gray_code(history)`, `differs_by_one_bit` moved out a level and wrapped in `bool()`, early `num_bits < 1` return and `assert` around the initial call added, `del result[-1]` -> `result.pop()`, variable renames, type hints. Reflection program `gray_code` matches apart from renames (`prev`, `value`) and type hints. Book's `gray_code_pythonic` is MISSING from the file.
- Needs PDF review: page 232, middle value of "The next few values are (0010)2, ?, (0111)2" not clearly legible (reads like (0011)2, which would repeat).
- check_code_unchanged: OK

### src/epi_python/chapter_16_dynamic_programming/pg_236_num_combinations_for_final_score.py
- Exercise: 16.1 Count the number of score combinations, printed pages 236–239
- Code vs book: differs. `num_combinations_for_final_score` (1D list) carries the book's name but is not the book's program; it is the O(s)-space version the book only states as a variant. The book's 2D program is `num_combinations_for_final_score_table`, with renamed parameters/variables (`score`, `scores`, `dp`, `row`, `total`), zero-initialized rows with `dp[row][0] = 1` set in the loop instead of `[[1] + [0]*final_score ...]`, an added empty-`scores` guard, and type hints.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_16_dynamic_programming/pg_239_levenshtein_distance.py
- Exercise: 16.2 Compute the Levenshtein distance, printed pages 239–242
- Code vs book: differs. `levenshtein_distance` (bottom-up, two rolling rows) carries the book's name but is not printed in the book. The book's memoized program is `levenshtein_distance_memoized`: parameters `A`, `B` -> `first`, `second`; helper `compute_distance_between_prefixes(A_idx, B_idx)` -> `distance(i, j)`; cache `distance_between_prefixes` -> `cache`; result computed into a local and min argument order changed (delete, add, substitute vs book's substitute, add, delete); type hints added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_16_dynamic_programming/pg_242_number_of_ways.py
- Exercise: 16.3 Count the number of ways to traverse a 2D array, printed pages 242–244
- Code vs book: same algorithm. Book's cache `number_of_ways` (shadowing the function name, created after the helper) renamed `ways` and created before; `x == y == 0` written `x == 0 and y == 0`; `0 if x == 0 else ...` written `... if x > 0 else 0`; added `n <= 0 or m <= 0` guard returning 0; type hints added.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_16_dynamic_programming/pg_244_compute_binomial_coefficients.py
- Exercise: 16.4 Compute the binomial coefficients, printed pages 244–245
- Code vs book: different algorithm. Book `compute_binomial_coefficient(n, k)` is a memoized recursion (nested `compute_x_choose_y(x, y)`, 2D cache `x_choose_y`). File `compute_binomial_coefficients` (plural) builds Pascal's triangle rows bottom-up (O(n) space, O(n^2) time) and adds a `k < 0 or k > n` guard. The book's memoized implementation is missing from the file.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_16_dynamic_programming/pg_245_is_pattern_contained_in_grid.py
- Exercise: 16.5 Search for a sequence in a 2D array, printed pages 245–246
- Code vs book: nearly matches. Parameter `S` -> `s`; type hints added; `previous_attempts` created before (not after) the helper; final return adds `or not s` (empty pattern on empty grid returns True). Helper body matches.
- Needs PDF review: page 245, worked-example step "search for <4,6> from (0,1)'s neighbors" (the matched entry is (1,0)); confirm wording.
- check_code_unchanged: OK

### src/epi_python/chapter_16_dynamic_programming/pg_246_optimum_subject_to_capacity.py
- Exercise: 16.6 The knapsack problem, printed pages 246–249
- Code vs book: different implementation. Book uses `Item = collections.namedtuple('Item', ('weight', 'value'))` and a memoized recursion `optimum_subject_to_item_and_capacity(k, available_capacity)` with 2D cache `V` (-1 = unknown), O(nw) space. File keeps the name/parameters but takes plain (weight, value) tuples and fills a 1D table `best` with descending capacities (O(w) space, the book's first variant). The book's memoized implementation and namedtuple are missing from the file.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_16_dynamic_programming/pg_249_decompose_into_dictionary_words.py
- Exercise: 16.7 The bedbathandbeyond.com problem, printed pages 249–251
- Code vs book: nearly matches. File adds `if not domain: return []` (book would raise IndexError on empty input), type hints, and renames `idx` -> `index`.
- Needs PDF review: page 250, worked-example step (3.) for "ama" (stated reason does not match the split); confirm wording.
- check_code_unchanged: OK

### src/epi_python/chapter_16_dynamic_programming/pg_251_minimum_path_weight.py
- Exercise: 16.8 Find the minimum weight path in a triangle, printed pages 251–252
- Code vs book: matches the book's listing apart from an added `if not triangle: return 0` guard (same result as the book) and type hints.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_16_dynamic_programming/pg_252_maximum_revenue.py
- Exercise: 16.9 Pick up coins for maximum gain, printed pages 252–253
- Code vs book: matches the book's listing apart from an added `if not coins: return 0` guard, type hints, and creating the cache before (not after) the nested helper.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_16_dynamic_programming/pg_253_number_of_ways_to_top.py
- Exercise: 16.10 Count the number of moves to climb stairs, printed pages 253–254
- Code vs book: different implementation. Book uses a memoized recursion `compute_number_of_ways_to_h(h)` (base `h <= 1`) with cache `number_of_ways_to_h`; file computes the same recurrence bottom-up with list `ways` and `ways[0] = 1`. Parameter `maximum_step` renamed `max_step`; type hints added. The book's memoized implementation is missing from the file.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_16_dynamic_programming/pg_254_minimum_messiness.py
- Exercise: 16.11 The pretty printing problem, printed pages 254–256
- Code vs book: nearly matches. File adds `if not words: return 0` and a ValueError for words longer than a line, writes `0 if j == 0` for the book's `0 if j - 1 < 0`, returns `int(min_messiness[-1])`, and adds type hints.
- Needs PDF review: none (note: Figure 16.14 caption says "aaa bb" while the grids show "bbb", and the text's "(c)/(d) respectively" is opposite to the sub-figure captions; documented in the file).
- check_code_unchanged: OK

### src/epi_python/chapter_16_dynamic_programming/pg_257_longest_nondecreasing_subsequence.py
- Exercise: 16.12 Find the longest nondecreasing subsequence, printed pages 257–258
- Code vs book: differs. Book `longest_nondecreasing_subsequence_length(A)` with list `max_length` and a one-expression update using `max([...], default=0)`; file `longest_nondecreasing_subsequence(values)` with `best_ending_here`, `enumerate` and an explicit inner loop (same values), plus an empty-input guard and type hints. File also adds `longest_nondecreasing_subsequence_fast` (bisect_right, O(n log n)) and the `bisect` import, not in the book (book states the O(n log n) version only as a variant).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_260_optimum_task_assignment.py
- Exercise: 17.1 Compute an optimum assignment of tasks, printed pages 260–261
- Code vs book: matches algorithmically; file adds type hints (`task_durations: list[int]`, `-> list[PairedTasks]`) and lays out the list comprehension differently. Boot-camp `change_making` (p. 260) not in file.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_261_minimum_waiting_time.py
- Exercise: 17.2 Schedule to minimize waiting time, printed pages 261–262
- Code vs book: book `minimum_total_waiting_time(service_times)` uses enumerate and adds `service_time * num_remaining_queries`; file renamed to `minimum_waiting_time` with type hints and accumulates a running prefix sum (`elapsed`) instead. Same result, both sort in place.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_262_find_minimum_visits.py
- Exercise: 17.3 The interval covering problem, printed pages 262–263
- Code vs book: same logic; file uses `from collections import namedtuple` / `from operator import attrgetter` instead of module-qualified calls, adds type hints, and drops the book's inline code comments (paraphrased in new comments).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_264_has_three_sum.py
- Exercise: 17.4 The 3-sum problem, printed pages 264–266
- Code vs book: book has `has_two_sum(A, t)` (boot camp) and `has_three_sum(A, t)` = `A.sort(); return any(has_two_sum(A, t - a) for a in A)`. File has only `has_three_sum(values, target)` with type hints, uses `sorted()` (no in-place mutation), and inlines the two-pointer loop; `has_two_sum` missing as a separate function.
- Needs PDF review: none (variant 3 on p. 266 prints "A[p] <= A[r] <= A[s]" with undefined s; reproduced as printed and noted)
- check_code_unchanged: OK

### src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_266_majority_search.py
- Exercise: 17.5 Find the majority element, printed pages 266–267
- Code vs book: same voting loop with renamed parameter/variables (`input_stream`/`it`/`candidate_count` -> `values`/`value`/`count`) and type hints; file ADDS a verification pass (`values.count(candidate) > len(values)//2`) and returns None without a strict majority, whereas the book returns the candidate unconditionally in one pass.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_267_find_ample_city.py
- Exercise: 17.6 The gasup problem, printed pages 267–269
- Code vs book: same algorithm; file moves `CityAndRemainingGas` from inside the function to module level, drops `num_cities` local, adds type hints, and adds a ValueError check for empty/mismatched input (not in the book).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_269_max_water_container.py
- Exercise: 17.7 Compute the maximum water trapped by a pair of vertical lines, printed pages 269–270
- Code vs book: book `get_max_trapped_water(heights)` with `i, j, max_water`, `width`; file renamed `max_water_container` with type hints and variables `left, right, best`. Tie handling differs (book advances left on equal heights, file advances right); same result. Both return the max water, not the pair the problem statement asks for.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_270_largest_rectangle_under_skyline.py
- Exercise: 17.8 Compute the largest rectangle under the skyline, printed pages 270–272
- Code vs book: book `calculate_largest_rectangle(heights)`; file renamed `largest_rectangle_under_skyline` with type hints, variables renamed (`pillar_indices`->`stack`, `max_rectangle_area`->`best`), sentinel list stored as `extended`. Pop condition differs: book `>= h`, file `> height` (same result). Book's code comment paraphrased rather than kept.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_18_graphs/pg_276_search_maze.py
- Exercise: 18.1 Search a maze, printed pages 276–278
- Code vs book: colour encoding INVERTED (book `WHITE, BLACK = range(2)` = 0, 1; file `WHITE, BLACK = 1, 0`). Otherwise same DFS; `from collections import namedtuple` instead of `collections.namedtuple`, type hints added, `path` declared before the helper, final `if not ...: return []` replaced by a conditional expression; book's code comments not present in original file.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_18_graphs/pg_278_flip_color.py
- Exercise: 18.2 Paint a Boolean matrix, printed pages 278–280
- Code vs book: both book programs present. Book names both `flip_color(x, y, A)`; file has `flip_color` (BFS) and `flip_color_recursive` (DFS), parameter `A`->`a`, type hints. BFS: book uses an in-function `Coordinate` namedtuple and `q`, `d`, `next_x/next_y`; file uses plain tuples, `queue`, `dx, dy`, `nx, ny`, and `from collections import deque`. Same logic.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_18_graphs/pg_280_fill_surrounded_regions.py
- Exercise: 18.3 Compute enclosed regions, printed pages 280–281
- Code vs book: same algorithm; file adds type hints and an empty-board guard (not in book), uses `from collections import deque`, and builds the initial boundary queue with differently structured comprehensions (same cells).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_18_graphs/pg_281_is_deadlocked.py
- Exercise: 18.4 Deadlock detection, printed pages 281–282
- Code vs book: book's `class GraphVertex` (white/gray/black colors, `edges`) is MISSING; file's `is_deadlocked(adjacency: list[list[int]])` works on integer adjacency lists with a separate `state` list (0/1/2). Helper `has_cycle(cur)` renamed `visit(node)`, explicit for loop instead of `any(...)`, explicit black check. Same three-color DFS logic.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_18_graphs/pg_282_clone_graph.py
- Exercise: 18.5 Clone a graph, printed pages 282–283
- Code vs book: same BFS; parameter `G`->`g`, `if not G` -> `if g is None`, queue `q`->`queue`, `from collections import deque`, type hints added to GraphVertex and clone_graph.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_18_graphs/pg_283_is_any_placement_feasible.py
- Exercise: 18.6 Making wired connections, printed pages 283–284
- Code vs book: parameters `G`/`s` -> `g`/`start`, type hints added; book peeks `q[0]` and does `del q[0]`, file uses `popleft()`; conflict test differs (book `t.d == q[0].d`, file `neighbor.d % 2 == v.d % 2` — equivalent under BFS); `from collections import deque`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_18_graphs/pg_284_transform_string.py
- Exercise: 18.7 Transform one string to another, printed pages 284–286
- Code vs book: book `transform_string(D, s, t)` (dictionary first) vs file `transform_string(start, target, dictionary)` (dictionary last, type hints). Book uses a `StringWithDistance` namedtuple, removes visited words from D (mutating it; KeyError if s not in D), checks target on dequeue, uses `string.ascii_lowercase`. File uses tuples, a separate `visited` set (dictionary untouched), checks target on generation (`distance+1`), literal alphabet, and adds early returns for start == target and target not in dictionary.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_18_graphs/pg_286_find_largest_number_teams.py
- Exercise: 18.8 Team photo day — 2, printed pages 286–288
- Code vs book: same structure (GraphVertex, nested build_topological_ordering/dfs/find_longest_path); parameter `G`->`g`, outer loop `for g in G` -> `for vertex in g`, dfs loop variable `next` -> `neighbor`, type hints added throughout.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_19_parallel_computing/pg_291_spell_check_service.py
- Exercise: 19.1 Implement caching for a multithreaded dictionary, printed pages 291–292
- Code vs book: the book's first (racy) program is not in the file. The corrected program is restructured: class-level `w_last`/`closest_to_last_word`/`lock` and `@staticmethod service(req, resp)` become instance attributes set in a new `__init__(closest_in_dictionary)` and `service(self, word)` that returns the result instead of `resp.encode_into_response`; the lookup is injected; the cache stores `result.copy()` instead of `result`. Locking pattern matches.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_19_parallel_computing/pg_292_increment_thread.py
- Exercise: 19.2 Analyze two unsynchronized interleaved threads, printed pages 292–293
- Code vs book: book is a top-level script (globals `N`, `counter`, `global counter`, prints result); file wraps it in `run_unsynchronized_increments(n: int) -> int` with a nested `increment_thread` using `nonlocal`, and returns the counter. Increment and start/join sequence match.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_19_parallel_computing/pg_293_odd_even_monitor.py
- Exercise: 19.3 Implement synchronization for two interleaving threads, printed pages 293–294
- Code vs book: OddEvenMonitor matches. OddThread/EvenThread take extra `emit` and `limit` parameters and call `self.emit(i)` instead of `print(i)`, looping to `limit` instead of 100. File adds driver `print_in_order(limit=100)` not in the book.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_19_parallel_computing/pg_294_thread_pool_server.py
- Exercise: 19.4 Implement a thread pool, printed pages 294–295
- Code vs book: none of the book's three socket-server programs (original `main()`, thread-per-request, `ThreadPoolExecutor(max_workers=NTHREADS)` accept loop) is present. File has an added finite adapter `process_requests(requests, process_req, max_workers=2)` that submits each request to a ThreadPoolExecutor (as a context manager) and returns `future.result()` values; `from concurrent.futures import ThreadPoolExecutor`; no socket/threading imports.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_19_parallel_computing/pg_295_account_transfer.py
- Exercise: 19.5 Deadlock, printed pages 295–296
- Code vs book: file has only the corrected Account (book's original locks only `self._lock`). Additions not in book: `_id_lock` around id assignment, locked `get_balance`, `amount<0` rejection, `transfer` returns the Thread. `_move` parameter `acc_to`->`other`, book's `print('returning True')` omitted, thread variable `th`->`thread`, method order changed. Lock-ordering logic matches.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_19_parallel_computing/pg_296_readers_writers_lock.py
- Exercise: 19.6 The readers-writers problem, printed pages 296–297
- Code vs book: substantially different. Book: `Reader`/`Writer` threading.Thread subclasses with infinite run() loops using `RW.LR` (used with wait/notify), `RW.LW`, `RW.read_count`, `RW.data`, `do_something_else()`; writer holds LW and waits on LR until read_count == 0. File: a single `ReadersWritersLock` class (first reader acquires the write lock, last reader releases it; no wait/notify). Book's Reader/Writer classes are missing.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_19_parallel_computing/pg_297_writers_preference_lock.py
- Exercise: 19.7 The readers-writers problem with write preference, printed pages 297–298
- Code vs book: the book prints NO program (prose only: readers lock and immediately release the write lock). The file's `WritersPreferenceLock` (Condition + waiting-writer count) is entirely an addition and uses a different mechanism from the book's description.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_19_parallel_computing/pg_298_parallel_collatz.py
- Exercise: 19.9 Test the Collatz conjecture in parallel, printed pages 298–299
- Code vs book: `collatz_check` matches. `worker` returns a bool instead of the book's `assert` + `print('(%d,%d)' ...)`. The book's top-level submission snippet (undefined N/NTHREADS/RANGESIZE, `range(N // RANGESIZE)`) is replaced by an added driver `parallel_collatz(limit, max_workers=2, range_size=20)` that clips the final interval and returns `all(future.result() ...)`; `from concurrent.futures import ProcessPoolExecutor`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_19_parallel_computing/pg_298_timer_class.py
- Exercise: 19.8 Implement a Timer class, printed page 298
- Code vs book: the book prints NO program (design described in prose). The file's `Timer` class is entirely an addition following that design (heapq min-heap, name-keyed dict, one Condition as the single lock, dispatch thread), but with a different interface than the problem statement (`schedule(name, callback, delay_seconds)` instead of a constructor taking an object with run/name), lazy cancellation, and an added `close()`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_351_gcd.py
- Exercise: 24.1 Compute the greatest common divisor, printed pages 351–352
- Code vs book: DIFFERENT ALGORITHM. Book prints a recursive binary GCD using shifts and parity tests (no multiplication/division/modulus). File's `gcd(x: int, y: int) -> int` is an iterative Euclidean `x, y = y, x % y` loop (uses the modulus the problem forbids) and applies abs() to accept negatives. Book's binary-GCD implementation is missing.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_352_first_missing_positive.py
- Exercise: 24.2 Find the first missing positive entry, printed pages 352–353
- Code vs book: Book `find_first_missing_positive(A)` mutates A in place and uses `next(...)` over a generator for the second pass. File renamed `first_missing_positive(values: list[int]) -> int`, works on `values.copy()` (O(n) extra space vs book's O(1)), stores the swap index in `target`, and uses an explicit for loop for the second pass. Same results.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_353_buy_and_sell_stock_k_times.py
- Exercise: 24.3 Buy and sell a stock k times, printed pages 353–354
- Code vs book: Same name/algorithm; type hints added; first test extended to `if not k or not prices`; `elif` became `if`; `max(0.0, ...)`, `[0.0] * k`, lists assigned separately; `reversed(range(k))` without `list(...)`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_354_find_biggest_n_minus_one_product.py
- Exercise: 24.4 Compute the maximum product of all entries but one, printed pages 354–356
- Code vs book: Both book programs present. Prefix/suffix version: parameter renamed `a`, hints, added ValueError for <2 elements. Sign-counting version: book reuses the name `find_biggest_n_minus_one_product`; file renames it `find_biggest_n_minus_one_product_by_sign`, adds ValueError guard, loop var `value`, `elif` instead of `else: if`, and `operator.mul` instead of the book's lambda in `functools.reduce`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_356_find_longest_increasing_subarray.py
- Exercise: 24.5 Compute the longest contiguous increasing subarray, printed pages 356–357
- Code vs book: `from collections import namedtuple` instead of `collections.namedtuple`; parameter `a: list[int]`, return hint; added `if not a: return Subarray(0, -1)`. Loop matches book.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_357_rotate_array.py
- Exercise: 24.6 Rotate an array, printed pages 357–359
- Code vs book: Cycle solution: book `rotate_array` with nested `apply_cyclic_permutation` and `fractions.gcd`; file `rotate_array_cycles` inlines the nested function, uses `math.gcd`, adds empty guard. Triple-reverse: same algorithm, first param renamed `rotate_amount`, guard added. Naive: book reverses with slices (`A[:] = A[::-1]` etc.); file uses `a[:] = a[-i:] + a[:-i] if i else a[:]` (different expression, same result).
- Needs PDF review: page 357, the n=6, i=2 permutation is printed as <4,5,1,2,3,4> (repeats 4); transcribed as printed.
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_359_rook_attack.py
- Exercise: 24.7 Identify positions attacked by rooks, printed pages 359–360
- Code vs book: Parameter `a` with hints; flags renamed `first_row_zero`/`first_column_zero` (book `has_first_...`); added empty-board guard; one-line loop bodies. Same algorithm.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_360_justify_text.py
- Exercise: 24.8 Justify text, printed pages 360–361
- Code vs book: Parameters `words, line_length` (book `L`), variables `current_*` (book `curr_*`), added ValueError for over-long words, final return adds `if words else []` (book returns one blank-padded line for empty input).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_361_zipping_linked_list.py
- Exercise: 24.9 Implement list zipping, printed pages 361–362
- Code vs book: Parameter `head` (book `L`), iterators `first_iter`/`second_iter` (book `first_half_iter`/`second_half_iter`); same statements. File adds helpers not printed here: `ListNode`, its own `reverse_linked_list`, `as_list`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_362_copy_postings_list.py
- Exercise: 24.10 Copy a postings list, printed pages 362–364
- Code vs book: Parameter `head`, `if head is None`; Stage 1 var `copy` (book `new_node`); Stage 3 rewritten as a loop over original nodes with a `copy` variable and conditional `copy.next = ...` (book: single loop `it.next, it = it.next.next, it.next`); `PostingListNode` class defined in file. Same results.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_364_longest_matching_parentheses.py
- Exercise: 24.11 Compute the longest substring with matching parens, printed pages 364–365
- Code vs book: matches (type hints added; conditional expression on one line).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_365_max_of_sliding_window.py
- Exercise: 24.12 Compute the maximum of a sliding window, printed pages 365–366
- Code vs book: COMPLETELY DIFFERENT PROGRAM. Book: `TrafficElement` class (`__lt__`, `__eq__`) and `calculate_traffic_volumes(A, w)` over timestamped traffic using QueueWithMax (Ch. 8). File: `max_of_sliding_window(values, k)` over k consecutive plain values using a `collections.deque` monotonic queue, with ValueError for k <= 0 and [] for k > len. Book's classes/functions missing.
- Needs PDF review: page 365, data array lists (14, 1.1) but Figure 24.5(a) and the page-366 output show 1.7 at timestamp 14; page 366, enqueued pair printed as "(t_i, t_i)".
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_366_postorder_traversal.py
- Exercise: 24.13 Implement a postorder traversal without recursion, printed pages 366–368
- Code vs book: Both book programs present. Solution 1 (book `postorder_traversal` with nested `inverted_preorder_traversal`) renamed `postorder_traversal_via_reverse` with the nested function inlined. Solution 2 same name and statements, compressed onto single lines; hints added. `BinaryTreeNode` defined in file.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_368_calculate_bonus.py
- Exercise: 24.14 Compute fair bonuses, printed pages 368–370
- Code vs book: Both programs present. Heap version (book also named `calculate_bonus`) renamed `calculate_bonus_heap`; uses plain `(p, i)` tuples instead of the `EmployeeData` namedtuple; left-neighbor update uses `max(...)` (book assigns `tickets[next_dev-1] + 1`). Two-pass version matches (hints added).
- Needs PDF review: page 369, worked walk-through (David, Andy, Bob, Charlie; total 7; "Charlie ... a neighbor of Charlie and David") is inconsistent with the printed examples; transcribed as printed.
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_370_binary_search_unknown_length.py
- Exercise: 24.15 Search a sorted array of unknown length, printed pages 370–372
- Code vs book: Parameter `a`, hints on k/return; `elif` written as `if` (equivalent); added `if p == 0: left = 0` (no effect). Otherwise same.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_372_find_kth_in_two_sorted_arrays.py
- Exercise: 24.16 Search in two sorted arrays, printed pages 372–373
- Code vs book: Same partition binary search but restructured: `while low <= high` with `x = (low + high) // 2` (book `while b < t` plus a post-loop return of `max(A_b_1, B_k_b_1)`); variables renamed; post-loop replaced by `raise RuntimeError`; added ValueError for invalid k.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_373_find_kth_largest_unknown_length.py
- Exercise: 24.17 Find the kth largest element—large n, small k, printed pages 373–374
- Code vs book: Book calls Solution 11.8 (reorders list) then `del candidates[k:]` and returns `candidates[k - 1]`. File imports the repository's Ch. 11 `find_kth_largest` (non-reordering), so pruning is rewritten via a cutoff value, comprehension and padding; returns the helper's value; added ValueErrors for k <= 0 and too-short stream.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_374_find_element_appears_once.py
- Exercise: 24.18 Find an element that appears only once, printed pages 374–375
- Code vs book: Parameter `a`; bit read as `(value >> i) & 1` instead of `x & 1` with `x >>= 1`; book's nested `handle_negative` replaced by an inline conditional expression on `result`. Same results.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_375_find_line_with_most_points.py
- Exercise: 24.19 Find the line through the most points, printed pages 375–376
- Code vs book: differs. Book uses `collections.namedtuple`/`collections.defaultdict`/`fractions.gcd`; file imports `namedtuple`, `defaultdict`, `math.gcd` directly. Type hints `list[Point]`/`-> int` added. Book's explicit vertical-line branch (`elif p1.x == p2.x:` -> key (0, 1)) is absent; file instead adds a sign-normalization step and uses floor division `//=` with variable `divisor` where the book uses true division `/` with variable `gcd`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_376_build_bst_from_sorted_doubly_list.py
- Exercise: 24.20 Convert a sorted doubly linked list into a BST, printed pages 376–378
- Code vs book: differs. File adds a `DoublyNode` class (book prints none); parameter `L` renamed `head`; type hints added; nested helper renamed from `build_bst_from_sorted_doubly_list_helper` to `build`; cursor list named `current` (book `head = [L]`); book's combined `curr, head[0] = head[0], head[0].next` split into separate statements with an added `ValueError` check when the list is shorter than n; local `curr` renamed `root`.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_378_bst_to_doubly_linked_list.py
- Exercise: 24.21 Convert a BST to a sorted doubly linked list, printed pages 378–379
- Code vs book: differs. File adds a `BSTNode` class; type hints added; book's `HeadAndTail` namedtuple replaced by plain (head, tail) tuples (so no `collections` import); helper renamed from `bst_to_doubly_linked_list_helper(tree)` to `helper(root)` with `is None` test; final `.head` becomes `[0]`. Logic otherwise the same.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_379_merge_two_bsts.py
- Exercise: 24.22 Merge two BSTs, printed pages 379–380
- Code vs book: differs. Book's program is a 4-line composition calling `bst_to_doubly_list`, `count_length`, `merge_two_sorted_lists` and `build_bst_from_sorted_doubly_list` from earlier solutions. File (params `a`, `b` with type hints, added `BSTNode` class) implements all stages inline: nested `to_list` (tuple-returning), an inline merge loop that also counts n, and a size-based `build(size)` rebuild instead of the book's `(start, end)` helper (root choice may differ for even sizes).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_380_is_match.py
- Exercise: 24.23 Implement regular expression matching, printed pages 380–383
- Code vs book: differs. Type hints added. Star case restructured: book loops from `i = 1` with condition `regex[0] in ('.', s[i - 1])` and tests the zero-occurrence case last (`return is_match_here(regex[2:], s)`); file starts at `i=0`, tries zero occurrences first, uses `break`, returns False. Book's `if regex[0] == '^'` replaced by `regex.startswith('^')` (avoids IndexError on empty regex). Other cases match.
- Needs PDF review: none (the book's underlining of matched substrings in the examples is not reproducible in plain text; noted in the docstring)
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_383_expression_synthesis.py
- Exercise: 24.24 Synthesize an expression, printed pages 383–385
- Code vs book: differs. Nested `directed_expression_synthesis` renamed `search(remaining, current_term)`; `evaluate()` moved up one nesting level with renamed locals; type hints added. The book's pruning test before trying '+' (`target - evaluate() <= functools.reduce(...)`) is absent (no `functools` import). Stack handling differs (operator swapped instead of operand popped/re-pushed; `.pop()` instead of `del`). Added `if not remaining` base case and `if not digits: return False` guard.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_385_count_inversions.py
- Exercise: 24.25 Count inversions, printed pages 385–386
- Code vs book: differs in structure only. Parameter `A` renamed `a`, type hints added; the book's two nested functions (`count_subarray_inversions`, `merge_sort_and_count_inversions_across_subarrays`) are combined into one `merge_sort_count(start, end)`; locals renamed (`sorted_A`->`merged`, `left_start`/`right_start`->`i`/`j`, `inversion_count`->`inv`). Algorithm and final slice assignment match.
- Needs PDF review: page 386 recurrence printed as `T(n) = O(n) + 2T(n - 1)` (likely typo for n/2; flagged in file)
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_386_compute_skyline.py
- Exercise: 24.26 Draw the skyline, printed pages 386–388
- Code vs book: minor differences. `namedtuple` imported directly; type hints added; added `if not buildings: return []` guard; book's `min(buildings, key=lambda b: b.left).left` / `max(..., key=lambda b: b.right).right` replaced by generator expressions `min(b.left for b in buildings)` / `max(b.right ...)`. Otherwise matches the book's digitized program. The book's divide-and-conquer solution is described only (not printed) and is not in the file.
- Needs PDF review: none (Figure 24.8 building coordinates summarized, not transcribed)
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_388_check_feasible.py
- Exercise: 24.27 Measure with defective jugs, printed pages 388–389
- Code vs book: differs. Book `check_feasible(jugs, L, H, c=set())` recurses on itself with a mutable default cache shared across calls and defines `VolumeRange` inside the function; file uses `lower`/`upper` with type hints, a per-call `visited` set and nested `helper(l, h)`, module-level `VolumeRange`, and an explicit for-loop instead of the book's `any(...)` generator. Same logic.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_390_max_subarray_sum_in_circular_array.py
- Exercise: 24.28 Compute the maximum subarray sum in a circular array, printed pages 389–391 (file name says 390; problem starts on 389)
- Code vs book: differs substantially. Book prints two programs named `max_subarray_sum_in_circular(A)`: (1) S_i + E_i with running maxima (O(n) space), (2) `find_optimum_subarray_using_comp(comp)` with max/min (O(1) space). File has one function `max_subarray_sum_in_circular_array(values)` that is a rewrite of program 2 in a single loop; program 1 is missing. Behaviour differs: book allows empty subarray (returns 0 for all-negative input); file requires nonempty subarray (returns max element) and returns 0 for empty input.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_391_get_height.py
- Exercise: 24.29 Determine the critical height, printed pages 391–392
- Code vs book: minor differences only. Type hints added; helper renamed `get_height_helper(cases, drops)` -> `helper(c, d)`; memo table `F` renamed `table` and created before the helper; `elif` chain written as two one-line `if`s. Same algorithm.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_393_max_rectangle_submatrix.py
- Exercise: 24.30 Find the maximum 2D subarray, printed pages 392–395 (file name says 393; problem starts on 392)
- Code vs book: differs. Book prints three programs. (1) `max_rectangle_submatrix`: file uses two int tables instead of a `MaxHW` namedtuple table, has no pruning test (`w*h > max_rect_area`), uses `min_width=cols` instead of `float('inf')`, adds empty guard. (2) `max_square_submatrix`: file uses a different recurrence `1 + min(below, right, diagonal)` rather than the book's MaxHW table plus `min(s[i+1][j+1] + 1, min(h, w))`. (3) The skyline-based O(mn) `max_rectangle_submatrix` (using `calculate_largest_rectangle` from 17.8) is missing. Parameter `A` -> `a`, type hints added.
- Needs PDF review: page 395 variant "Solve the largest square 2D subarray problem using O(m) time" transcribed as printed (wording looks odd; flagged in file comment, not as a NEEDS PDF REVIEW marker)
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_395_huffman_encoding.py
- Exercise: 24.31 Implement Huffman coding, printed pages 395–398
- Code vs book: differs. Book uses a nested `BinaryTree` class with `__lt__` in the heap and `assign_huffman_code(tree, code)` that builds code strings in a dict `huffman_encoding`; file uses `(freq, serial, node)` heap tuples with an `itertools.count()` tie-breaker (extra import), tuple internal nodes, and `assign(node, depth)` recording code lengths only (`max(1, depth)`). Returns the same average-length sum. Added type hints and empty-input guard; single-symbol behaviour differs (book 0, file 1).
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_398_calculate_trapping_water.py
- Exercise: 24.32 Trapping water, printed pages 398–399
- Code vs book: minor differences. Type hints and an empty-input guard added; inner function's parameter/locals renamed (`heights`->`values`, `partial_sum`->`volume`, `h`->`height`). Otherwise matches.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_399_search_frequent_items.py
- Exercise: 24.33 The heavy hitter problem, printed pages 399–400
- Code vs book: minor differences. Type hints and an `if k <= 1: return []` guard added; loop variables renamed (`buf`->`word`, `it`->`candidate`, `value`->`count`); decrement loop iterates `list(table)`. Otherwise matches.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_400_find_longest_subarray_less_equal_k.py
- Exercise: 24.34 Find the longest subarray whose sum <= k, printed pages 400–402
- Code vs book: differs. Parameter `A` -> `a`, type hints and empty-input guard added; book's `functools.reduce`/`reversed` construction of `min_prefix_sum` replaced by a copy plus explicit backward loop (no `functools` import); indices `a`/`b` renamed `start`/`end`, `min_curr_sum` -> `minimum_sum`; best length updated via `max()` instead of `curr_length` + `if`. Same algorithm.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_402_find_best_proposals.py
- Exercise: 24.35 Road network, printed pages 402–403
- Code vs book: differs. Params `H, P` renamed `highways, proposals` with type hints; nested loops instead of `itertools.product`; Floyd-Warshall inlined (book: nested `floyd_warshall(G)` with inf checks); duplicate highways keep the minimum distance; saving per pair takes min over both directions of the proposal (book uses one direction only, so totals can differ); file returns None when no positive saving, whereas book starts at `-inf` with default `HighwaySection(-1, -1, 0)` and returns the first proposal even with zero saving.
- Needs PDF review: none
- check_code_unchanged: OK

### src/epi_python/chapter_24_honors_class/pg_403_is_arbitrage_exist.py
- Exercise: 24.36 Test if arbitrage is possible, printed pages 403–405
- Code vs book: differs. Param `G` -> `rates` with type hints; natural `math.log` instead of the book's `math.log10`; nested `bellman_ford(G, source)` inlined; inf-guard in relaxation replaced by a `1e-12` floating-point tolerance (also in the final `any`); added empty-input guard. Same algorithm.
- Needs PDF review: none (Table 24.3 entry JPY->CHF = 1.2442 transcribed as printed; looks anomalous)
- check_code_unchanged: OK
