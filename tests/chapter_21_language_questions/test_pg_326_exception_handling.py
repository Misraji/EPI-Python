"""Exception-handling examples from EPI pp.326–328."""

# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_21_language_questions.pg_326_exception_handling import (
    get_col_sum,
    get_value_with_finally,
    get_value_with_except,
    get_value_with_except_finally,
)


def test_json_variants(tmp_path):
    filename = tmp_path / 'document.json'
    filename.write_text('{"value": 8}', encoding='utf-8')
    assert get_value_with_finally(str(filename), 'value') == 8
    assert get_value_with_except(str(filename), 'value') == (True, 8)
    assert get_value_with_except_finally(str(filename), 'value') == (True, 8)
    filename.write_text('{invalid', encoding='utf-8')
    with pytest.raises(ValueError):
        get_value_with_finally(str(filename), 'value')
    assert get_value_with_except(str(filename), 'value') == (False,)
    assert get_value_with_except_finally(str(filename), 'value') == (False,)


def test_csv_converts_and_skips_invalid_values(tmp_path, capsys):
    filename = tmp_path / 'scores.csv'
    filename.write_text('a,3\nb,-5\nc,bad\nd,8\n', encoding='utf-8')
    assert get_col_sum(str(filename), 1) == 6
    output = capsys.readouterr().out
    assert 'cannot convert bad to int' in output
    assert 'Sum = 6' in output


def test_csv_missing_column_and_file(tmp_path):
    filename = tmp_path / 'short.csv'
    filename.write_text('a,3\nb\n', encoding='utf-8')
    with pytest.raises(IndexError):
        get_col_sum(str(filename), 1)
    with pytest.raises(OSError):
        get_col_sum(str(tmp_path / 'not_a_file.csv'), 1)
