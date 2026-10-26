"""EPI Python 24.23, textbook printed page 380: Implement regular expression matching.

QUESTION: Implement a subset of regular expression matching: literals, dot, star, start/end anchors.

TEXTBOOK ALGORITHM: The book uses recursive matching of a pattern at an offset plus an outer unanchored substring search.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_380_is_match
Test: python -m pytest tests/chapter_24_honors_class/test_pg_380_is_match.py -v
"""

def is_match(regex: str,s: str) -> bool:
    def is_match_here(regex: str,s: str) -> bool:
        if not regex:return True
        if regex=='$':return not s
        if len(regex)>=2 and regex[1]=='*':
            i=0
            while i<=len(s):
                if is_match_here(regex[2:],s[i:]):return True
                if i==len(s) or regex[0] not in ('.',s[i]):break
                i+=1
            return False
        return bool(s and regex[0] in ('.',s[0]) and is_match_here(regex[1:],s[1:]))
    if regex.startswith('^'):
        return is_match_here(regex[1:],s)
    return any(is_match_here(regex,s[i:]) for i in range(len(s)+1))


if __name__=='__main__':
    print('Regex match:',is_match('^a.*z$','abcz'))
    assert is_match('^a.*z$','abcz')
