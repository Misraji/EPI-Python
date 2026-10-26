# Implementation and validation coverage

The book's table of contents contains **264 exercises** (chapters 4–24). All 264 are indexed and have page-linked OCR-text Markdown references. The introductory text for all 24 chapters is also available under each `pg-NNN-README.md`.

**72** exercises currently have manually reviewed or independently reconstructed `.py` implementations with accompanying pytest modules.

**192** remain reference-only; no claim of working code or successful tests is made for them.

The runnable 12.2 example preserves the prior approved two textbook implementations. Other reviewed modules are educational reconstructions, labeled inside each source file, and should be compared to the original book before treating them as exact transcriptions.

### Limitations

- EPI PDF text extraction contains substantial OCR errors, including syntax, mathematical symbols, and indentation. Markdown captures that text layer, *not* a guaranteed faithful source transcription.
- Some exercises start on the same page. Reference transcripts may overlap and may include nearby solutions.
- Drawings and figures are not reconstructed into Markdown.
- The original PDF is not included in this GitHub-ready ZIP.
- No continuous integration run has happened on GitHub itself; local validation results appear below when available.

### Reviewed Python implementations

- **4.1**, printed p. 24: `src/epi_python/chapter_04_primitive_types/pg_024_parity.py`
- **4.2**, printed p. 27: `src/epi_python/chapter_04_primitive_types/pg_027_swap_bits.py`
- **4.3**, printed p. 28: `src/epi_python/chapter_04_primitive_types/pg_028_reverse_bits.py`
- **4.4**, printed p. 28: `src/epi_python/chapter_04_primitive_types/pg_028_closest_int_same_bit_count.py`
- **4.8**, printed p. 32: `src/epi_python/chapter_04_primitive_types/pg_032_reverse_digits.py`
- **4.9**, printed p. 33: `src/epi_python/chapter_04_primitive_types/pg_033_is_number_palindromic.py`
- **5.2**, printed p. 43: `src/epi_python/chapter_05_arrays/pg_043_plus_one.py`
- **5.4**, printed p. 44: `src/epi_python/chapter_05_arrays/pg_044_can_reach_end.py`
- **5.5**, printed p. 45: `src/epi_python/chapter_05_arrays/pg_045_delete_duplicates.py`
- **5.6**, printed p. 46: `src/epi_python/chapter_05_arrays/pg_046_compute_max_profit.py`
- **5.7**, printed p. 47: `src/epi_python/chapter_05_arrays/pg_047_buy_and_sell_stock_twice.py`
- **5.8**, printed p. 48: `src/epi_python/chapter_05_arrays/pg_048_rearrange_alternation.py`
- **5.9**, printed p. 49: `src/epi_python/chapter_05_arrays/pg_049_generate_primes.py`
- **5.11**, printed p. 52: `src/epi_python/chapter_05_arrays/pg_052_next_permutation.py`
- **5.20**, printed p. 65: `src/epi_python/chapter_05_arrays/pg_065_generate_pascal_triangle.py`
- **6.1**, printed p. 68: `src/epi_python/chapter_06_strings/pg_068_string_integer_interconversion.py`
- **6.3**, printed p. 70: `src/epi_python/chapter_06_strings/pg_070_ss_decode_col_id.py`
- **6.5**, printed p. 72: `src/epi_python/chapter_06_strings/pg_072_is_palindromic.py`
- **6.6**, printed p. 73: `src/epi_python/chapter_06_strings/pg_073_reverse_words.py`
- **6.8**, printed p. 75: `src/epi_python/chapter_06_strings/pg_075_look_and_say.py`
- **6.9**, printed p. 76: `src/epi_python/chapter_06_strings/pg_076_roman_to_integer.py`
- **6.10**, printed p. 77: `src/epi_python/chapter_06_strings/pg_077_get_valid_ip_addresses.py`
- **6.12**, printed p. 79: `src/epi_python/chapter_06_strings/pg_079_run_length_encoding.py`
- **6.13**, printed p. 79: `src/epi_python/chapter_06_strings/pg_079_rabin_karp.py`
- **7.1**, printed p. 84: `src/epi_python/chapter_07_linked_lists/pg_084_merge_two_sorted_lists.py`
- **7.2**, printed p. 85: `src/epi_python/chapter_07_linked_lists/pg_085_reverse_sublist.py`
- **7.3**, printed p. 86: `src/epi_python/chapter_07_linked_lists/pg_086_has_cycle.py`
- **7.8**, printed p. 91: `src/epi_python/chapter_07_linked_lists/pg_091_remove_duplicates_sorted_list.py`
- **8.2**, printed p. 101: `src/epi_python/chapter_08_stacks_and_queues/pg_101_evaluate_rpn.py`
- **8.3**, printed p. 102: `src/epi_python/chapter_08_stacks_and_queues/pg_102_is_well_formed.py`
- **8.4**, printed p. 102: `src/epi_python/chapter_08_stacks_and_queues/pg_102_shortest_equivalent_path.py`
- **8.8**, printed p. 108: `src/epi_python/chapter_08_stacks_and_queues/pg_108_queue_from_stacks.py`
- **9.1**, printed p. 114: `src/epi_python/chapter_09_binary_trees/pg_114_is_balanced_binary_tree.py`
- **9.2**, printed p. 116: `src/epi_python/chapter_09_binary_trees/pg_116_is_symmetric_binary_tree.py`
- **9.7**, printed p. 121: `src/epi_python/chapter_09_binary_trees/pg_121_inorder_traversal.py`
- **10.1**, printed p. 134: `src/epi_python/chapter_10_heaps/pg_134_merge_sorted_arrays.py`
- **10.3**, printed p. 136: `src/epi_python/chapter_10_heaps/pg_136_sort_approximately_sorted_array.py`
- **10.5**, printed p. 139: `src/epi_python/chapter_10_heaps/pg_139_online_median.py`
- **11.1**, printed p. 145: `src/epi_python/chapter_11_searching/pg_145_search_first_of_k.py`
- **11.2**, printed p. 146: `src/epi_python/chapter_11_searching/pg_146_search_entry_equal_to_index.py`
- **11.3**, printed p. 147: `src/epi_python/chapter_11_searching/pg_147_search_smallest.py`
- **11.4**, printed p. 148: `src/epi_python/chapter_11_searching/pg_148_square_root.py`
- **11.6**, printed p. 150: `src/epi_python/chapter_11_searching/pg_150_matrix_search.py`
- **12.1**, printed p. 163: `src/epi_python/chapter_12_hash_tables/pg_163_can_form_palindrome.py`
- **12.2**, printed p. 164: `src/epi_python/chapter_12_hash_tables/pg_164_is_letter_constructible_from_magazine.py`
- **12.5**, printed p. 167: `src/epi_python/chapter_12_hash_tables/pg_167_find_nearest_repetition.py`
- **12.8**, printed p. 173: `src/epi_python/chapter_12_hash_tables/pg_173_longest_subarray_with_distinct_entries.py`
- **13.1**, printed p. 182: `src/epi_python/chapter_13_sorting/pg_182_intersect_two_sorted_arrays.py`
- **13.4**, printed p. 185: `src/epi_python/chapter_13_sorting/pg_185_smallest_nonconstructible_value.py`
- **14.1**, printed p. 199: `src/epi_python/chapter_14_binary_search_trees/pg_199_is_binary_tree_bst.py`
- **15.1**, printed p. 219: `src/epi_python/chapter_15_recursion/pg_219_compute_tower_hanoi.py`
- **15.3**, printed p. 222: `src/epi_python/chapter_15_recursion/pg_222_permutations.py`
- **15.4**, printed p. 224: `src/epi_python/chapter_15_recursion/pg_224_generate_power_set.py`
- **15.5**, printed p. 226: `src/epi_python/chapter_15_recursion/pg_226_combinations.py`
- **15.6**, printed p. 227: `src/epi_python/chapter_15_recursion/pg_227_generate_balanced_parentheses.py`
- **16.1**, printed p. 236: `src/epi_python/chapter_16_dynamic_programming/pg_236_num_combinations_for_final_score.py`
- **16.2**, printed p. 239: `src/epi_python/chapter_16_dynamic_programming/pg_239_levenshtein_distance.py`
- **16.4**, printed p. 244: `src/epi_python/chapter_16_dynamic_programming/pg_244_compute_binomial_coefficients.py`
- **16.6**, printed p. 246: `src/epi_python/chapter_16_dynamic_programming/pg_246_optimum_subject_to_capacity.py`
- **16.10**, printed p. 253: `src/epi_python/chapter_16_dynamic_programming/pg_253_number_of_ways_to_top.py`
- **16.12**, printed p. 257: `src/epi_python/chapter_16_dynamic_programming/pg_257_longest_nondecreasing_subsequence.py`
- **17.2**, printed p. 261: `src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_261_minimum_waiting_time.py`
- **17.4**, printed p. 264: `src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_264_has_three_sum.py`
- **17.5**, printed p. 266: `src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_266_majority_search.py`
- **17.7**, printed p. 269: `src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_269_max_water_container.py`
- **17.8**, printed p. 270: `src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_270_largest_rectangle_under_skyline.py`
- **18.4**, printed p. 281: `src/epi_python/chapter_18_graphs/pg_281_is_deadlocked.py`
- **18.7**, printed p. 284: `src/epi_python/chapter_18_graphs/pg_284_transform_string.py`
- **24.1**, printed p. 351: `src/epi_python/chapter_24_honors_class/pg_351_gcd.py`
- **24.2**, printed p. 352: `src/epi_python/chapter_24_honors_class/pg_352_first_missing_positive.py`
- **24.12**, printed p. 365: `src/epi_python/chapter_24_honors_class/pg_365_max_of_sliding_window.py`
- **24.28**, printed p. 390: `src/epi_python/chapter_24_honors_class/pg_390_max_subarray_sum_in_circular_array.py`

### Local validation

See [VALIDATION.md](VALIDATION.md): 356 pytest tests passed; all 72 standalone modules executed successfully; syntax compilation completed without errors. Ruff and mypy were not available locally.
