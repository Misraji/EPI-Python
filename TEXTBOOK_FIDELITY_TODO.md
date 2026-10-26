# Remaining textbook fidelity work

This is an annotation/merging pass, **not** a line-by-line manual transcription of the PDF.

- 215 exercise reference Markdown files embedded in corresponding Python files; source MD removed.
- 49 conceptual Markdown references retained.
- Every newly embedded page transcription is explicitly marked **UNVERIFIED OCR**.
- Alternative complete implementations present in the PDF still need case-by-case comparison/reconstruction.
- OCR code embedded in comments is *not* an executable alternative implementation.
- Verify hints, problem statements, complete explanations, worked examples, variant problems, tables, and page boundaries manually.
- Library API comments and import URLs were added by parsing code, not manually reviewing whether every comment is accurate for its context.

## Chapter introductions still requiring verification

| File | Nonwhitespace characters | Status |
|---|---:|---|
| `src/epi_python/chapter_01_getting_ready/pg-006-README.md` | 20226 | OCR_UNVERIFIED |
| `src/epi_python/chapter_02_strategies_for_a_great_interview/pg-013-README.md` | 20223 | OCR_UNVERIFIED |
| `src/epi_python/chapter_03_conducting_an_interview/pg-019-README.md` | 9688 | OCR_UNVERIFIED |
| `src/epi_python/chapter_04_primitive_types/pg-023-README.md` | 2551 | OCR_UNVERIFIED |
| `src/epi_python/chapter_05_arrays/pg-037-README.md` | 5317 | OCR_UNVERIFIED |
| `src/epi_python/chapter_06_strings/pg-067-README.md` | 2887 | OCR_UNVERIFIED |
| `src/epi_python/chapter_07_linked_lists/pg-082-README.md` | 4684 | OCR_UNVERIFIED |
| `src/epi_python/chapter_08_stacks_and_queues/pg-097-README.md` | 2047 | OCR_UNVERIFIED |
| `src/epi_python/chapter_09_binary_trees/pg-112-README.md` | 6096 | OCR_UNVERIFIED |
| `src/epi_python/chapter_10_heaps/pg-132-README.md` | 4821 | OCR_UNVERIFIED |
| `src/epi_python/chapter_11_searching/pg-142-README.md` | 6355 | OCR_UNVERIFIED |
| `src/epi_python/chapter_12_hash_tables/pg-159-README.md` | 11910 | OCR_UNVERIFIED |
| `src/epi_python/chapter_13_sorting/pg-180-README.md` | 5645 | OCR_UNVERIFIED |
| `src/epi_python/chapter_14_binary_search_trees/pg-197-README.md` | 4703 | OCR_UNVERIFIED |
| `src/epi_python/chapter_15_recursion/pg-217-README.md` | 5343 | OCR_UNVERIFIED |
| `src/epi_python/chapter_16_dynamic_programming/pg-234-README.md` | 4942 | OCR_UNVERIFIED |
| `src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg-259-README.md` | 3469 | OCR_UNVERIFIED |
| `src/epi_python/chapter_18_graphs/pg-273-README.md` | 6754 | OCR_UNVERIFIED |
| `src/epi_python/chapter_19_parallel_computing/pg-289-README.md` | 5746 | OCR_UNVERIFIED |
| `src/epi_python/chapter_20_design_problems/pg-301-README.md` | 2552 | OCR_UNVERIFIED |
| `src/epi_python/chapter_21_language_questions/pg-319-README.md` | 385 | OCR_UNVERIFIED |
| `src/epi_python/chapter_22_object_oriented_design/pg-333-README.md` | 389 | OCR_UNVERIFIED |
| `src/epi_python/chapter_23_common_tools/pg-339-README.md` | 379 | OCR_UNVERIFIED |
| `src/epi_python/chapter_24_honors_class/pg-350-README.md` | 2865 | OCR_UNVERIFIED |

## Exercises requiring PDF review

- 4.1 p.24: `src/epi_python/chapter_04_primitive_types/pg_024_parity.py` — embedded OCR not certified, source alternatives not enumerated.
- 4.2 p.27: `src/epi_python/chapter_04_primitive_types/pg_027_swap_bits.py` — embedded OCR not certified, source alternatives not enumerated.
- 4.3 p.28: `src/epi_python/chapter_04_primitive_types/pg_028_reverse_bits.py` — embedded OCR not certified, source alternatives not enumerated.
- 4.4 p.28: `src/epi_python/chapter_04_primitive_types/pg_028_closest_int_same_bit_count.py` — embedded OCR not certified, source alternatives not enumerated.
- 4.5 p.29: `src/epi_python/chapter_04_primitive_types/pg_029_multiply_without_arithmetic.py` — embedded OCR not certified, source alternatives not enumerated.
- 4.6 p.31: `src/epi_python/chapter_04_primitive_types/pg_031_divide_without_arithmetic.py` — embedded OCR not certified, source alternatives not enumerated.
- 4.7 p.32: `src/epi_python/chapter_04_primitive_types/pg_032_power.py` — embedded OCR not certified, source alternatives not enumerated.
- 4.8 p.32: `src/epi_python/chapter_04_primitive_types/pg_032_reverse_digits.py` — embedded OCR not certified, source alternatives not enumerated.
- 4.9 p.33: `src/epi_python/chapter_04_primitive_types/pg_033_is_number_palindromic.py` — embedded OCR not certified, source alternatives not enumerated.
- 4.10 p.34: `src/epi_python/chapter_04_primitive_types/pg_034_uniform_random.py` — embedded OCR not certified, source alternatives not enumerated.
- 4.11 p.35: `src/epi_python/chapter_04_primitive_types/pg_035_rectangle_intersection.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.1 p.39: `src/epi_python/chapter_05_arrays/pg_039_dutch_flag_partition.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.2 p.43: `src/epi_python/chapter_05_arrays/pg_043_plus_one.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.3 p.43: `src/epi_python/chapter_05_arrays/pg_043_multiply_digits.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.4 p.44: `src/epi_python/chapter_05_arrays/pg_044_can_reach_end.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.5 p.45: `src/epi_python/chapter_05_arrays/pg_045_delete_duplicates.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.6 p.46: `src/epi_python/chapter_05_arrays/pg_046_compute_max_profit.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.7 p.47: `src/epi_python/chapter_05_arrays/pg_047_buy_and_sell_stock_twice.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.8 p.48: `src/epi_python/chapter_05_arrays/pg_048_rearrange_alternation.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.9 p.49: `src/epi_python/chapter_05_arrays/pg_049_generate_primes.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.10 p.50: `src/epi_python/chapter_05_arrays/pg_050_apply_permutation.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.11 p.52: `src/epi_python/chapter_05_arrays/pg_052_next_permutation.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.12 p.54: `src/epi_python/chapter_05_arrays/pg_054_offline_random_sampling.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.13 p.55: `src/epi_python/chapter_05_arrays/pg_055_online_random_sampling.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.14 p.56: `src/epi_python/chapter_05_arrays/pg_056_compute_random_permutation.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.15 p.57: `src/epi_python/chapter_05_arrays/pg_057_compute_random_subset.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.16 p.58: `src/epi_python/chapter_05_arrays/pg_058_nonuniform_random_number.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.17 p.60: `src/epi_python/chapter_05_arrays/pg_060_sudoku_checker.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.18 p.61: `src/epi_python/chapter_05_arrays/pg_061_spiral_ordering.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.19 p.64: `src/epi_python/chapter_05_arrays/pg_064_rotate_matrix.py` — embedded OCR not certified, source alternatives not enumerated.
- 5.20 p.65: `src/epi_python/chapter_05_arrays/pg_065_generate_pascal_triangle.py` — embedded OCR not certified, source alternatives not enumerated.
- 6.1 p.68: `src/epi_python/chapter_06_strings/pg_068_string_integer_interconversion.py` — embedded OCR not certified, source alternatives not enumerated.
- 6.2 p.69: `src/epi_python/chapter_06_strings/pg_069_convert_base.py` — embedded OCR not certified, source alternatives not enumerated.
- 6.3 p.70: `src/epi_python/chapter_06_strings/pg_070_ss_decode_col_id.py` — embedded OCR not certified, source alternatives not enumerated.
- 6.4 p.71: `src/epi_python/chapter_06_strings/pg_071_replace_and_remove.py` — embedded OCR not certified, source alternatives not enumerated.
- 6.5 p.72: `src/epi_python/chapter_06_strings/pg_072_is_palindromic.py` — embedded OCR not certified, source alternatives not enumerated.
- 6.6 p.73: `src/epi_python/chapter_06_strings/pg_073_reverse_words.py` — embedded OCR not certified, source alternatives not enumerated.
- 6.7 p.74: `src/epi_python/chapter_06_strings/pg_074_phone_mnemonics.py` — embedded OCR not certified, source alternatives not enumerated.
- 6.8 p.75: `src/epi_python/chapter_06_strings/pg_075_look_and_say.py` — embedded OCR not certified, source alternatives not enumerated.
- 6.9 p.76: `src/epi_python/chapter_06_strings/pg_076_roman_to_integer.py` — embedded OCR not certified, source alternatives not enumerated.
- 6.10 p.77: `src/epi_python/chapter_06_strings/pg_077_get_valid_ip_addresses.py` — embedded OCR not certified, source alternatives not enumerated.
- 6.11 p.78: `src/epi_python/chapter_06_strings/pg_078_snake_string.py` — embedded OCR not certified, source alternatives not enumerated.
- 6.12 p.79: `src/epi_python/chapter_06_strings/pg_079_run_length_encoding.py` — embedded OCR not certified, source alternatives not enumerated.
- 6.13 p.79: `src/epi_python/chapter_06_strings/pg_079_rabin_karp.py` — embedded OCR not certified, source alternatives not enumerated.
- 7.1 p.84: `src/epi_python/chapter_07_linked_lists/pg_084_merge_two_sorted_lists.py` — embedded OCR not certified, source alternatives not enumerated.
- 7.2 p.85: `src/epi_python/chapter_07_linked_lists/pg_085_reverse_sublist.py` — embedded OCR not certified, source alternatives not enumerated.
- 7.3 p.86: `src/epi_python/chapter_07_linked_lists/pg_086_has_cycle.py` — embedded OCR not certified, source alternatives not enumerated.
- 7.4 p.87: `src/epi_python/chapter_07_linked_lists/pg_087_overlapping_no_cycle_lists.py` — embedded OCR not certified, source alternatives not enumerated.
- 7.5 p.88: `src/epi_python/chapter_07_linked_lists/pg_088_overlapping_lists_with_cycles.py` — embedded OCR not certified, source alternatives not enumerated.
- 7.6 p.90: `src/epi_python/chapter_07_linked_lists/pg_090_delete_node.py` — embedded OCR not certified, source alternatives not enumerated.
- 7.7 p.90: `src/epi_python/chapter_07_linked_lists/pg_090_remove_kth_last.py` — embedded OCR not certified, source alternatives not enumerated.
- 7.8 p.91: `src/epi_python/chapter_07_linked_lists/pg_091_remove_duplicates_sorted_list.py` — embedded OCR not certified, source alternatives not enumerated.
- 7.9 p.92: `src/epi_python/chapter_07_linked_lists/pg_092_cyclic_right_shift.py` — embedded OCR not certified, source alternatives not enumerated.
- 7.10 p.93: `src/epi_python/chapter_07_linked_lists/pg_093_even_odd_merge.py` — embedded OCR not certified, source alternatives not enumerated.
- 7.11 p.94: `src/epi_python/chapter_07_linked_lists/pg_094_linked_list_palindrome.py` — embedded OCR not certified, source alternatives not enumerated.
- 7.12 p.95: `src/epi_python/chapter_07_linked_lists/pg_095_list_pivot.py` — embedded OCR not certified, source alternatives not enumerated.
- 7.13 p.96: `src/epi_python/chapter_07_linked_lists/pg_096_add_list_based_integers.py` — embedded OCR not certified, source alternatives not enumerated.
- 8.1 p.98: `src/epi_python/chapter_08_stacks_and_queues/pg_098_stack_with_max.py` — embedded OCR not certified, source alternatives not enumerated.
- 8.2 p.101: `src/epi_python/chapter_08_stacks_and_queues/pg_101_evaluate_rpn.py` — embedded OCR not certified, source alternatives not enumerated.
- 8.3 p.102: `src/epi_python/chapter_08_stacks_and_queues/pg_102_is_well_formed.py` — embedded OCR not certified, source alternatives not enumerated.
- 8.4 p.102: `src/epi_python/chapter_08_stacks_and_queues/pg_102_shortest_equivalent_path.py` — embedded OCR not certified, source alternatives not enumerated.
- 8.5 p.103: `src/epi_python/chapter_08_stacks_and_queues/pg_103_sunset_view.py` — embedded OCR not certified, source alternatives not enumerated.
- 8.6 p.106: `src/epi_python/chapter_08_stacks_and_queues/pg_106_binary_tree_depth_order.py` — embedded OCR not certified, source alternatives not enumerated.
- 8.7 p.107: `src/epi_python/chapter_08_stacks_and_queues/pg_107_circular_queue.py` — embedded OCR not certified, source alternatives not enumerated.
- 8.8 p.108: `src/epi_python/chapter_08_stacks_and_queues/pg_108_queue_from_stacks.py` — embedded OCR not certified, source alternatives not enumerated.
- 8.9 p.109: `src/epi_python/chapter_08_stacks_and_queues/pg_109_queue_with_max.py` — embedded OCR not certified, source alternatives not enumerated.
- 9.1 p.114: `src/epi_python/chapter_09_binary_trees/pg_114_is_balanced_binary_tree.py` — embedded OCR not certified, source alternatives not enumerated.
- 9.2 p.116: `src/epi_python/chapter_09_binary_trees/pg_116_is_symmetric_binary_tree.py` — embedded OCR not certified, source alternatives not enumerated.
- 9.3 p.117: `src/epi_python/chapter_09_binary_trees/pg_117_lowest_common_ancestor.py` — embedded OCR not certified, source alternatives not enumerated.
- 9.4 p.118: `src/epi_python/chapter_09_binary_trees/pg_118_lca_with_parent.py` — embedded OCR not certified, source alternatives not enumerated.
- 9.5 p.119: `src/epi_python/chapter_09_binary_trees/pg_119_sum_root_to_leaf_paths.py` — embedded OCR not certified, source alternatives not enumerated.
- 9.6 p.120: `src/epi_python/chapter_09_binary_trees/pg_120_has_path_sum.py` — embedded OCR not certified, source alternatives not enumerated.
- 9.7 p.121: `src/epi_python/chapter_09_binary_trees/pg_121_inorder_traversal.py` — embedded OCR not certified, source alternatives not enumerated.
- 9.8 p.121: `src/epi_python/chapter_09_binary_trees/pg_121_preorder_without_recursion.py` — embedded OCR not certified, source alternatives not enumerated.
- 9.9 p.122: `src/epi_python/chapter_09_binary_trees/pg_122_kth_node_inorder.py` — embedded OCR not certified, source alternatives not enumerated.
- 9.10 p.123: `src/epi_python/chapter_09_binary_trees/pg_123_inorder_successor.py` — embedded OCR not certified, source alternatives not enumerated.
- 9.11 p.124: `src/epi_python/chapter_09_binary_trees/pg_124_morris_inorder.py` — embedded OCR not certified, source alternatives not enumerated.
- 9.12 p.125: `src/epi_python/chapter_09_binary_trees/pg_125_reconstruct_from_traversals.py` — embedded OCR not certified, source alternatives not enumerated.
- 9.13 p.127: `src/epi_python/chapter_09_binary_trees/pg_127_reconstruct_preorder_markers.py` — embedded OCR not certified, source alternatives not enumerated.
- 9.14 p.128: `src/epi_python/chapter_09_binary_trees/pg_128_binary_tree_leaves_list.py` — embedded OCR not certified, source alternatives not enumerated.
- 9.15 p.128: `src/epi_python/chapter_09_binary_trees/pg_128_exterior_binary_tree.py` — embedded OCR not certified, source alternatives not enumerated.
- 9.16 p.129: `src/epi_python/chapter_09_binary_trees/pg_129_right_sibling_tree.py` — embedded OCR not certified, source alternatives not enumerated.
- 10.1 p.134: `src/epi_python/chapter_10_heaps/pg_134_merge_sorted_arrays.py` — embedded OCR not certified, source alternatives not enumerated.
- 10.2 p.135: `src/epi_python/chapter_10_heaps/pg_135_sort_increasing_decreasing_array.py` — embedded OCR not certified, source alternatives not enumerated.
- 10.3 p.136: `src/epi_python/chapter_10_heaps/pg_136_sort_approximately_sorted_array.py` — embedded OCR not certified, source alternatives not enumerated.
- 10.4 p.137: `src/epi_python/chapter_10_heaps/pg_137_k_closest_stars.py` — embedded OCR not certified, source alternatives not enumerated.
- 10.5 p.139: `src/epi_python/chapter_10_heaps/pg_139_online_median.py` — embedded OCR not certified, source alternatives not enumerated.
- 10.6 p.140: `src/epi_python/chapter_10_heaps/pg_140_k_largest_in_binary_heap.py` — embedded OCR not certified, source alternatives not enumerated.
- 11.1 p.145: `src/epi_python/chapter_11_searching/pg_145_search_first_of_k.py` — embedded OCR not certified, source alternatives not enumerated.
- 11.2 p.146: `src/epi_python/chapter_11_searching/pg_146_search_entry_equal_to_index.py` — embedded OCR not certified, source alternatives not enumerated.
- 11.3 p.147: `src/epi_python/chapter_11_searching/pg_147_search_smallest.py` — embedded OCR not certified, source alternatives not enumerated.
- 11.4 p.148: `src/epi_python/chapter_11_searching/pg_148_square_root.py` — embedded OCR not certified, source alternatives not enumerated.
- 11.5 p.149: `src/epi_python/chapter_11_searching/pg_149_real_square_root.py` — embedded OCR not certified, source alternatives not enumerated.
- 11.6 p.150: `src/epi_python/chapter_11_searching/pg_150_matrix_search.py` — embedded OCR not certified, source alternatives not enumerated.
- 11.7 p.152: `src/epi_python/chapter_11_searching/pg_152_find_min_max.py` — embedded OCR not certified, source alternatives not enumerated.
- 11.8 p.153: `src/epi_python/chapter_11_searching/pg_153_kth_largest_element.py` — embedded OCR not certified, source alternatives not enumerated.
- 11.9 p.155: `src/epi_python/chapter_11_searching/pg_155_find_missing_ip.py` — embedded OCR not certified, source alternatives not enumerated.
- 11.10 p.157: `src/epi_python/chapter_11_searching/pg_157_find_duplicate_missing.py` — embedded OCR not certified, source alternatives not enumerated.
- 12.1 p.163: `src/epi_python/chapter_12_hash_tables/pg_163_can_form_palindrome.py` — embedded OCR not certified, source alternatives not enumerated.
- 12.2 p.164: `src/epi_python/chapter_12_hash_tables/pg_164_is_letter_constructible_from_magazine.py` — embedded OCR not certified, source alternatives not enumerated.
- 12.3 p.165: `src/epi_python/chapter_12_hash_tables/pg_165_isbn_lru_cache.py` — embedded OCR not certified, source alternatives not enumerated.
- 12.4 p.166: `src/epi_python/chapter_12_hash_tables/pg_166_lca_close_ancestors.py` — embedded OCR not certified, source alternatives not enumerated.
- 12.5 p.167: `src/epi_python/chapter_12_hash_tables/pg_167_find_nearest_repetition.py` — embedded OCR not certified, source alternatives not enumerated.
- 12.6 p.168: `src/epi_python/chapter_12_hash_tables/pg_168_smallest_subarray_covering_set.py` — embedded OCR not certified, source alternatives not enumerated.
- 12.7 p.171: `src/epi_python/chapter_12_hash_tables/pg_171_smallest_subarray_sequential_cover.py` — embedded OCR not certified, source alternatives not enumerated.
- 12.8 p.173: `src/epi_python/chapter_12_hash_tables/pg_173_longest_subarray_with_distinct_entries.py` — embedded OCR not certified, source alternatives not enumerated.
- 12.9 p.174: `src/epi_python/chapter_12_hash_tables/pg_174_longest_contained_interval.py` — embedded OCR not certified, source alternatives not enumerated.
- 12.10 p.175: `src/epi_python/chapter_12_hash_tables/pg_175_string_decompositions.py` — embedded OCR not certified, source alternatives not enumerated.
- 12.11 p.176: `src/epi_python/chapter_12_hash_tables/pg_176_collatz_conjecture.py` — embedded OCR not certified, source alternatives not enumerated.
- 12.12 p.177: `src/epi_python/chapter_12_hash_tables/pg_177_chess_zobrist_hash.py` — embedded OCR not certified, source alternatives not enumerated.
- 13.1 p.182: `src/epi_python/chapter_13_sorting/pg_182_intersect_two_sorted_arrays.py` — embedded OCR not certified, source alternatives not enumerated.
- 13.2 p.183: `src/epi_python/chapter_13_sorting/pg_183_merge_two_sorted_arrays.py` — embedded OCR not certified, source alternatives not enumerated.
- 13.3 p.184: `src/epi_python/chapter_13_sorting/pg_184_eliminate_duplicate_names.py` — embedded OCR not certified, source alternatives not enumerated.
- 13.4 p.185: `src/epi_python/chapter_13_sorting/pg_185_smallest_nonconstructible_value.py` — embedded OCR not certified, source alternatives not enumerated.
- 13.5 p.186: `src/epi_python/chapter_13_sorting/pg_186_find_max_simultaneous_events.py` — embedded OCR not certified, source alternatives not enumerated.
- 13.6 p.188: `src/epi_python/chapter_13_sorting/pg_188_add_interval.py` — embedded OCR not certified, source alternatives not enumerated.
- 13.7 p.189: `src/epi_python/chapter_13_sorting/pg_189_union_of_intervals.py` — embedded OCR not certified, source alternatives not enumerated.
- 13.8 p.191: `src/epi_python/chapter_13_sorting/pg_191_group_by_age.py` — embedded OCR not certified, source alternatives not enumerated.
- 13.9 p.193: `src/epi_python/chapter_13_sorting/pg_193_team_photo_day.py` — embedded OCR not certified, source alternatives not enumerated.
- 13.10 p.194: `src/epi_python/chapter_13_sorting/pg_194_stable_sort_linked_list.py` — embedded OCR not certified, source alternatives not enumerated.
- 13.11 p.195: `src/epi_python/chapter_13_sorting/pg_195_find_salary_cap.py` — embedded OCR not certified, source alternatives not enumerated.
- 14.1 p.199: `src/epi_python/chapter_14_binary_search_trees/pg_199_is_binary_tree_bst.py` — embedded OCR not certified, source alternatives not enumerated.
- 14.2 p.201: `src/epi_python/chapter_14_binary_search_trees/pg_201_find_first_greater_than_k.py` — embedded OCR not certified, source alternatives not enumerated.
- 14.3 p.202: `src/epi_python/chapter_14_binary_search_trees/pg_202_find_k_largest_in_bst.py` — embedded OCR not certified, source alternatives not enumerated.
- 14.4 p.203: `src/epi_python/chapter_14_binary_search_trees/pg_203_find_lca_in_bst.py` — embedded OCR not certified, source alternatives not enumerated.
- 14.5 p.204: `src/epi_python/chapter_14_binary_search_trees/pg_204_rebuild_bst_from_preorder.py` — embedded OCR not certified, source alternatives not enumerated.
- 14.6 p.206: `src/epi_python/chapter_14_binary_search_trees/pg_206_find_closest_elements_in_sorted_arrays.py` — embedded OCR not certified, source alternatives not enumerated.
- 14.7 p.207: `src/epi_python/chapter_14_binary_search_trees/pg_207_generate_first_k_a_b_sqrt2.py` — embedded OCR not certified, source alternatives not enumerated.
- 14.8 p.210: `src/epi_python/chapter_14_binary_search_trees/pg_210_build_min_height_bst_from_sorted_array.py` — embedded OCR not certified, source alternatives not enumerated.
- 14.9 p.211: `src/epi_python/chapter_14_binary_search_trees/pg_211_pair_includes_ancestor_and_descendant_of_m.py` — embedded OCR not certified, source alternatives not enumerated.
- 14.10 p.212: `src/epi_python/chapter_14_binary_search_trees/pg_212_range_lookup_in_bst.py` — embedded OCR not certified, source alternatives not enumerated.
- 14.11 p.215: `src/epi_python/chapter_14_binary_search_trees/pg_215_clients_credits_info.py` — embedded OCR not certified, source alternatives not enumerated.
- 15.1 p.219: `src/epi_python/chapter_15_recursion/pg_219_compute_tower_hanoi.py` — embedded OCR not certified, source alternatives not enumerated.
- 15.2 p.221: `src/epi_python/chapter_15_recursion/pg_221_n_queens.py` — embedded OCR not certified, source alternatives not enumerated.
- 15.3 p.222: `src/epi_python/chapter_15_recursion/pg_222_permutations.py` — embedded OCR not certified, source alternatives not enumerated.
- 15.4 p.224: `src/epi_python/chapter_15_recursion/pg_224_generate_power_set.py` — embedded OCR not certified, source alternatives not enumerated.
- 15.5 p.226: `src/epi_python/chapter_15_recursion/pg_226_combinations.py` — embedded OCR not certified, source alternatives not enumerated.
- 15.6 p.227: `src/epi_python/chapter_15_recursion/pg_227_generate_balanced_parentheses.py` — embedded OCR not certified, source alternatives not enumerated.
- 15.7 p.228: `src/epi_python/chapter_15_recursion/pg_228_palindrome_decompositions.py` — embedded OCR not certified, source alternatives not enumerated.
- 15.8 p.229: `src/epi_python/chapter_15_recursion/pg_229_generate_all_binary_trees.py` — embedded OCR not certified, source alternatives not enumerated.
- 15.9 p.230: `src/epi_python/chapter_15_recursion/pg_230_solve_sudoku.py` — embedded OCR not certified, source alternatives not enumerated.
- 15.10 p.232: `src/epi_python/chapter_15_recursion/pg_232_gray_code.py` — embedded OCR not certified, source alternatives not enumerated.
- 16.1 p.236: `src/epi_python/chapter_16_dynamic_programming/pg_236_num_combinations_for_final_score.py` — embedded OCR not certified, source alternatives not enumerated.
- 16.2 p.239: `src/epi_python/chapter_16_dynamic_programming/pg_239_levenshtein_distance.py` — embedded OCR not certified, source alternatives not enumerated.
- 16.3 p.242: `src/epi_python/chapter_16_dynamic_programming/pg_242_number_of_ways.py` — embedded OCR not certified, source alternatives not enumerated.
- 16.4 p.244: `src/epi_python/chapter_16_dynamic_programming/pg_244_compute_binomial_coefficients.py` — embedded OCR not certified, source alternatives not enumerated.
- 16.5 p.245: `src/epi_python/chapter_16_dynamic_programming/pg_245_is_pattern_contained_in_grid.py` — embedded OCR not certified, source alternatives not enumerated.
- 16.6 p.246: `src/epi_python/chapter_16_dynamic_programming/pg_246_optimum_subject_to_capacity.py` — embedded OCR not certified, source alternatives not enumerated.
- 16.7 p.249: `src/epi_python/chapter_16_dynamic_programming/pg_249_decompose_into_dictionary_words.py` — embedded OCR not certified, source alternatives not enumerated.
- 16.8 p.251: `src/epi_python/chapter_16_dynamic_programming/pg_251_minimum_path_weight.py` — embedded OCR not certified, source alternatives not enumerated.
- 16.9 p.252: `src/epi_python/chapter_16_dynamic_programming/pg_252_maximum_revenue.py` — embedded OCR not certified, source alternatives not enumerated.
- 16.10 p.253: `src/epi_python/chapter_16_dynamic_programming/pg_253_number_of_ways_to_top.py` — embedded OCR not certified, source alternatives not enumerated.
- 16.11 p.254: `src/epi_python/chapter_16_dynamic_programming/pg_254_minimum_messiness.py` — embedded OCR not certified, source alternatives not enumerated.
- 16.12 p.257: `src/epi_python/chapter_16_dynamic_programming/pg_257_longest_nondecreasing_subsequence.py` — embedded OCR not certified, source alternatives not enumerated.
- 17.1 p.260: `src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_260_optimum_task_assignment.py` — embedded OCR not certified, source alternatives not enumerated.
- 17.2 p.261: `src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_261_minimum_waiting_time.py` — embedded OCR not certified, source alternatives not enumerated.
- 17.3 p.262: `src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_262_find_minimum_visits.py` — embedded OCR not certified, source alternatives not enumerated.
- 17.4 p.264: `src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_264_has_three_sum.py` — embedded OCR not certified, source alternatives not enumerated.
- 17.5 p.266: `src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_266_majority_search.py` — embedded OCR not certified, source alternatives not enumerated.
- 17.6 p.267: `src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_267_find_ample_city.py` — embedded OCR not certified, source alternatives not enumerated.
- 17.7 p.269: `src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_269_max_water_container.py` — embedded OCR not certified, source alternatives not enumerated.
- 17.8 p.270: `src/epi_python/chapter_17_greedy_algorithms_and_invariants/pg_270_largest_rectangle_under_skyline.py` — embedded OCR not certified, source alternatives not enumerated.
- 18.1 p.276: `src/epi_python/chapter_18_graphs/pg_276_search_maze.py` — embedded OCR not certified, source alternatives not enumerated.
- 18.2 p.278: `src/epi_python/chapter_18_graphs/pg_278_flip_color.py` — embedded OCR not certified, source alternatives not enumerated.
- 18.3 p.280: `src/epi_python/chapter_18_graphs/pg_280_fill_surrounded_regions.py` — embedded OCR not certified, source alternatives not enumerated.
- 18.4 p.281: `src/epi_python/chapter_18_graphs/pg_281_is_deadlocked.py` — embedded OCR not certified, source alternatives not enumerated.
- 18.5 p.282: `src/epi_python/chapter_18_graphs/pg_282_clone_graph.py` — embedded OCR not certified, source alternatives not enumerated.
- 18.6 p.283: `src/epi_python/chapter_18_graphs/pg_283_is_any_placement_feasible.py` — embedded OCR not certified, source alternatives not enumerated.
- 18.7 p.284: `src/epi_python/chapter_18_graphs/pg_284_transform_string.py` — embedded OCR not certified, source alternatives not enumerated.
- 18.8 p.286: `src/epi_python/chapter_18_graphs/pg_286_find_largest_number_teams.py` — embedded OCR not certified, source alternatives not enumerated.
- 19.1 p.291: `src/epi_python/chapter_19_parallel_computing/pg_291_spell_check_service.py` — embedded OCR not certified, source alternatives not enumerated.
- 19.2 p.292: `src/epi_python/chapter_19_parallel_computing/pg_292_increment_thread.py` — embedded OCR not certified, source alternatives not enumerated.
- 19.3 p.293: `src/epi_python/chapter_19_parallel_computing/pg_293_odd_even_monitor.py` — embedded OCR not certified, source alternatives not enumerated.
- 19.4 p.294: `src/epi_python/chapter_19_parallel_computing/pg_294_thread_pool_server.py` — embedded OCR not certified, source alternatives not enumerated.
- 19.5 p.295: `src/epi_python/chapter_19_parallel_computing/pg_295_account_transfer.py` — embedded OCR not certified, source alternatives not enumerated.
- 19.6 p.296: `src/epi_python/chapter_19_parallel_computing/pg_296_readers_writers_lock.py` — embedded OCR not certified, source alternatives not enumerated.
- 19.7 p.297: `src/epi_python/chapter_19_parallel_computing/pg_297_writers_preference_lock.py` — embedded OCR not certified, source alternatives not enumerated.
- 19.8 p.298: `src/epi_python/chapter_19_parallel_computing/pg_298_timer_class.py` — embedded OCR not certified, source alternatives not enumerated.
- 19.9 p.298: `src/epi_python/chapter_19_parallel_computing/pg_298_parallel_collatz.py` — embedded OCR not certified, source alternatives not enumerated.
- 20.1 p.302: `src/epi_python/chapter_20_design_problems/pg_302_exercise_20_01_design_a_spell_checker.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.2 p.303: `src/epi_python/chapter_20_design_problems/pg_303_exercise_20_02_design_a_solution_to_the_stemming_problem.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.3 p.304: `src/epi_python/chapter_20_design_problems/pg_304_exercise_20_03_plagiarism_detector.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.4 p.305: `src/epi_python/chapter_20_design_problems/pg_305_exercise_20_04_pair_users_by_attributes.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.5 p.306: `src/epi_python/chapter_20_design_problems/pg_306_exercise_20_05_design_a_system_for_detecting_copyright_infringement.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.6 p.307: `src/epi_python/chapter_20_design_problems/pg_307_exercise_20_06_design_tex.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.7 p.307: `src/epi_python/chapter_20_design_problems/pg_307_exercise_20_07_design_a_search_engine.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.8 p.308: `src/epi_python/chapter_20_design_problems/pg_308_exercise_20_08_implement_pagerank.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.9 p.310: `src/epi_python/chapter_20_design_problems/pg_310_exercise_20_09_design_terasort_and_petasort.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.10 p.310: `src/epi_python/chapter_20_design_problems/pg_310_exercise_20_10_implement_distributed_throttling.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.11 p.311: `src/epi_python/chapter_20_design_problems/pg_311_exercise_20_11_design_a_scalable_priority_system.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.12 p.312: `src/epi_python/chapter_20_design_problems/pg_312_exercise_20_12_create_photomosaics.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.13 p.312: `src/epi_python/chapter_20_design_problems/pg_312_exercise_20_13_implement_mileage_run.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.14 p.314: `src/epi_python/chapter_20_design_problems/pg_314_exercise_20_14_implement_cormexus.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.15 p.315: `src/epi_python/chapter_20_design_problems/pg_315_exercise_20_15_design_an_online_advertising_system.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.16 p.316: `src/epi_python/chapter_20_design_problems/pg_316_exercise_20_16_design_a_recommendation_system.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.17 p.316: `src/epi_python/chapter_20_design_problems/pg_316_exercise_20_17_design_an_optimized_way_of_distributing_large_files.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.18 p.317: `src/epi_python/chapter_20_design_problems/pg_317_exercise_20_18_design_the_world_wide_web.md` — conceptual reference remains unverified, check for embedded executable listings.
- 20.19 p.318: `src/epi_python/chapter_20_design_problems/pg_318_exercise_20_19_estimate_the_hardware_cost_of_a_photo_sharing_app.md` — conceptual reference remains unverified, check for embedded executable listings.
- 21.1 p.319: `src/epi_python/chapter_21_language_questions/pg_319_exercise_21_01_garbage_collection.md` — conceptual reference remains unverified, check for embedded executable listings.
- 21.2 p.319: `src/epi_python/chapter_21_language_questions/pg_319_exercise_21_02_closure.md` — conceptual reference remains unverified, check for embedded executable listings.
- 21.3 p.320: `src/epi_python/chapter_21_language_questions/pg_320_exercise_21_03_shallow_and_deep_copy.md` — conceptual reference remains unverified, check for embedded executable listings.
- 21.4 p.321: `src/epi_python/chapter_21_language_questions/pg_321_exercise_21_04_iterators_and_generators.md` — conceptual reference remains unverified, check for embedded executable listings.
- 21.5 p.322: `src/epi_python/chapter_21_language_questions/pg_322_exercise_21_05_at_decorator.md` — conceptual reference remains unverified, check for embedded executable listings.
- 21.6 p.323: `src/epi_python/chapter_21_language_questions/pg_323_exercise_21_06_list_vs_tuple.md` — conceptual reference remains unverified, check for embedded executable listings.
- 21.7 p.324: `src/epi_python/chapter_21_language_questions/pg_324_exercise_21_07_star_args_and_star_star_kwargs.md` — conceptual reference remains unverified, check for embedded executable listings.
- 21.8 p.325: `src/epi_python/chapter_21_language_questions/pg_325_exercise_21_08_python_code.md` — conceptual reference remains unverified, check for embedded executable listings.
- 21.9 p.326: `src/epi_python/chapter_21_language_questions/pg_326_exercise_21_09_exception_handling.md` — conceptual reference remains unverified, check for embedded executable listings.
- 21.10 p.328: `src/epi_python/chapter_21_language_questions/pg_328_exercise_21_10_scoping.md` — conceptual reference remains unverified, check for embedded executable listings.
- 21.11 p.330: `src/epi_python/chapter_21_language_questions/pg_330_exercise_21_11_function_arguments.md` — conceptual reference remains unverified, check for embedded executable listings.
- 22.1 p.333: `src/epi_python/chapter_22_object_oriented_design/pg_333_exercise_22_01_template_method_vs_strategy.md` — conceptual reference remains unverified, check for embedded executable listings.
- 22.2 p.334: `src/epi_python/chapter_22_object_oriented_design/pg_334_exercise_22_02_observer_pattern.md` — conceptual reference remains unverified, check for embedded executable listings.
- 22.3 p.334: `src/epi_python/chapter_22_object_oriented_design/pg_334_exercise_22_03_push_vs_pull_observer_pattern.md` — conceptual reference remains unverified, check for embedded executable listings.
- 22.4 p.335: `src/epi_python/chapter_22_object_oriented_design/pg_335_exercise_22_04_singletons_and_flyweights.md` — conceptual reference remains unverified, check for embedded executable listings.
- 22.5 p.336: `src/epi_python/chapter_22_object_oriented_design/pg_336_exercise_22_05_adapters.md` — conceptual reference remains unverified, check for embedded executable listings.
- 22.6 p.337: `src/epi_python/chapter_22_object_oriented_design/pg_337_exercise_22_06_creational_patterns.md` — conceptual reference remains unverified, check for embedded executable listings.
- 22.7 p.338: `src/epi_python/chapter_22_object_oriented_design/pg_338_exercise_22_07_libraries_and_design_patterns.md` — conceptual reference remains unverified, check for embedded executable listings.
- 23.1 p.339: `src/epi_python/chapter_23_common_tools/pg_339_exercise_23_01_merging_in_a_version_control_system.md` — conceptual reference remains unverified, check for embedded executable listings.
- 23.2 p.341: `src/epi_python/chapter_23_common_tools/pg_341_exercise_23_02_hooks.md` — conceptual reference remains unverified, check for embedded executable listings.
- 23.3 p.342: `src/epi_python/chapter_23_common_tools/pg_342_exercise_23_03_is_scripting_more_efficient.md` — conceptual reference remains unverified, check for embedded executable listings.
- 23.4 p.343: `src/epi_python/chapter_23_common_tools/pg_343_exercise_23_04_polymorphism_with_a_scripting_language.md` — conceptual reference remains unverified, check for embedded executable listings.
- 23.5 p.343: `src/epi_python/chapter_23_common_tools/pg_343_exercise_23_05_dependency_analysis.md` — conceptual reference remains unverified, check for embedded executable listings.
- 23.6 p.344: `src/epi_python/chapter_23_common_tools/pg_344_exercise_23_06_ant_vs_maven.md` — conceptual reference remains unverified, check for embedded executable listings.
- 23.7 p.345: `src/epi_python/chapter_23_common_tools/pg_345_exercise_23_07_sql_vs_nosql.md` — conceptual reference remains unverified, check for embedded executable listings.
- 23.8 p.345: `src/epi_python/chapter_23_common_tools/pg_345_exercise_23_08_normalization.md` — conceptual reference remains unverified, check for embedded executable listings.
- 23.9 p.346: `src/epi_python/chapter_23_common_tools/pg_346_exercise_23_09_sql_design.md` — conceptual reference remains unverified, check for embedded executable listings.
- 23.10 p.346: `src/epi_python/chapter_23_common_tools/pg_346_exercise_23_10_ip_tcp_and_http.md` — conceptual reference remains unverified, check for embedded executable listings.
- 23.11 p.347: `src/epi_python/chapter_23_common_tools/pg_347_exercise_23_11_https.md` — conceptual reference remains unverified, check for embedded executable listings.
- 23.12 p.348: `src/epi_python/chapter_23_common_tools/pg_348_exercise_23_12_dns.md` — conceptual reference remains unverified, check for embedded executable listings.
- 24.1 p.351: `src/epi_python/chapter_24_honors_class/pg_351_gcd.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.2 p.352: `src/epi_python/chapter_24_honors_class/pg_352_first_missing_positive.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.3 p.353: `src/epi_python/chapter_24_honors_class/pg_353_buy_and_sell_stock_k_times.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.4 p.354: `src/epi_python/chapter_24_honors_class/pg_354_find_biggest_n_minus_one_product.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.5 p.356: `src/epi_python/chapter_24_honors_class/pg_356_find_longest_increasing_subarray.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.6 p.357: `src/epi_python/chapter_24_honors_class/pg_357_rotate_array.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.7 p.359: `src/epi_python/chapter_24_honors_class/pg_359_rook_attack.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.8 p.360: `src/epi_python/chapter_24_honors_class/pg_360_justify_text.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.9 p.361: `src/epi_python/chapter_24_honors_class/pg_361_zipping_linked_list.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.10 p.362: `src/epi_python/chapter_24_honors_class/pg_362_copy_postings_list.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.11 p.364: `src/epi_python/chapter_24_honors_class/pg_364_longest_matching_parentheses.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.12 p.365: `src/epi_python/chapter_24_honors_class/pg_365_max_of_sliding_window.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.13 p.366: `src/epi_python/chapter_24_honors_class/pg_366_postorder_traversal.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.14 p.368: `src/epi_python/chapter_24_honors_class/pg_368_calculate_bonus.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.15 p.370: `src/epi_python/chapter_24_honors_class/pg_370_binary_search_unknown_length.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.16 p.372: `src/epi_python/chapter_24_honors_class/pg_372_find_kth_in_two_sorted_arrays.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.17 p.373: `src/epi_python/chapter_24_honors_class/pg_373_find_kth_largest_unknown_length.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.18 p.374: `src/epi_python/chapter_24_honors_class/pg_374_find_element_appears_once.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.19 p.375: `src/epi_python/chapter_24_honors_class/pg_375_find_line_with_most_points.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.20 p.376: `src/epi_python/chapter_24_honors_class/pg_376_build_bst_from_sorted_doubly_list.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.21 p.378: `src/epi_python/chapter_24_honors_class/pg_378_bst_to_doubly_linked_list.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.22 p.379: `src/epi_python/chapter_24_honors_class/pg_379_merge_two_bsts.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.23 p.380: `src/epi_python/chapter_24_honors_class/pg_380_is_match.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.24 p.383: `src/epi_python/chapter_24_honors_class/pg_383_expression_synthesis.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.25 p.385: `src/epi_python/chapter_24_honors_class/pg_385_count_inversions.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.26 p.386: `src/epi_python/chapter_24_honors_class/pg_386_compute_skyline.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.27 p.388: `src/epi_python/chapter_24_honors_class/pg_388_check_feasible.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.28 p.390: `src/epi_python/chapter_24_honors_class/pg_390_max_subarray_sum_in_circular_array.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.29 p.391: `src/epi_python/chapter_24_honors_class/pg_391_get_height.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.30 p.393: `src/epi_python/chapter_24_honors_class/pg_393_max_rectangle_submatrix.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.31 p.395: `src/epi_python/chapter_24_honors_class/pg_395_huffman_encoding.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.32 p.398: `src/epi_python/chapter_24_honors_class/pg_398_calculate_trapping_water.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.33 p.399: `src/epi_python/chapter_24_honors_class/pg_399_search_frequent_items.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.34 p.400: `src/epi_python/chapter_24_honors_class/pg_400_find_longest_subarray_less_equal_k.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.35 p.402: `src/epi_python/chapter_24_honors_class/pg_402_find_best_proposals.py` — embedded OCR not certified, source alternatives not enumerated.
- 24.36 p.403: `src/epi_python/chapter_24_honors_class/pg_403_is_arbitrage_exist.py` — embedded OCR not certified, source alternatives not enumerated.
