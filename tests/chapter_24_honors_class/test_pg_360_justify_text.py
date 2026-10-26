# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_24_honors_class.pg_360_justify_text import justify_text


def test_widths_and_words():
    words=['The','quick','brown','fox','jumped','over','the','lazy','dogs.']
    lines=justify_text(words,11)
    assert all(len(line)==11 for line in lines)
    assert ' '.join(' '.join(lines).split())==' '.join(words)
    assert lines[-1].rstrip()=='dogs.'


def test_empty_single():
    assert justify_text([],5)==[]
    assert justify_text(['abc'],5)==['abc  ']
