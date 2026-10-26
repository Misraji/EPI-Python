"""EPI Python 24.8, textbook printed page 360: Justify text.

QUESTION: Justify words into fixed-width lines with evenly spread gaps and left-padded final line.

TEXTBOOK ALGORITHM: Accumulate words until a line would overflow; distribute extra blanks cyclically across gaps.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_360_justify_text
Test: python -m pytest tests/chapter_24_honors_class/test_pg_360_justify_text.py -v
"""

def justify_text(words: list[str],line_length: int) -> list[str]:
    current_line_length,result,current_line=0,[],[]
    for word in words:
        if len(word)>line_length:
            raise ValueError('Word longer than line')
        if current_line_length+len(word)+len(current_line)>line_length:
            for i in range(line_length-current_line_length):
                current_line[i%(len(current_line)-1 or 1)]+=' '
            result.append(''.join(current_line))
            current_line,current_line_length=[],0
        current_line.append(word)
        current_line_length+=len(word)

    # str.ljust pads a string with spaces to the requested width.
    # https://docs.python.org/3/library/stdtypes.html#str.ljust
    return result+[' '.join(current_line).ljust(line_length)] if words else []


if __name__=='__main__':
    lines=justify_text(['The','quick','brown','fox'],11)
    print('Justified lines:',lines)
    assert lines==['The   quick','brown fox  ']
