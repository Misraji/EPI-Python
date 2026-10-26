# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_24_honors_class.pg_395_huffman_encoding import CharWithFrequency,huffman_encoding


def test_huffman_average_length():
    assert huffman_encoding([CharWithFrequency('a',50),CharWithFrequency('b',25),CharWithFrequency('c',25)])==1.5
    assert huffman_encoding([CharWithFrequency('a',50),CharWithFrequency('b',50)])==1.0
    assert huffman_encoding([])==0
