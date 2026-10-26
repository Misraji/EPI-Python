"""EPI 6.10: Compute all valid IP addresses — printed page 77.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Compute all valid IP addresses
Algorithm: Enumerate three dot positions; reject leading zeros, empty groups, and octets exceeding 255.
Read the corresponding `pg_077_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_06_strings.pg_077_get_valid_ip_addresses
Test: python -m pytest tests/chapter_06_strings/test_pg_077_get_valid_ip_addresses.py -v
"""

def get_valid_ip_addresses(digits: str) -> list[str]:
    """List valid IPv4 dotted-decimal addresses obtained by inserting dots."""
    def valid(chunk: str) -> bool:
        return bool(chunk) and len(chunk) <= 3 and (chunk == '0' or chunk[0] != '0') and int(chunk) <= 255
    result = []
    for a in range(1,4):
        for b in range(a + 1, a + 4):
            for c in range(b + 1, b + 4):
                parts = (digits[:a],digits[a:b],digits[b:c],digits[c:])
                if all(valid(part) for part in parts):
                    result.append('.'.join(parts))
    return result


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = get_valid_ip_addresses('0000')
    print("get_valid_ip_addresses:", observed)
    assert observed == ['0.0.0.0']
    observed = get_valid_ip_addresses('1111')
    print("get_valid_ip_addresses:", observed)
    assert observed == ['1.1.1.1']
    observed = get_valid_ip_addresses('123')
    print("get_valid_ip_addresses:", observed)
    assert observed == []
    observed = get_valid_ip_addresses('9999')
    print("get_valid_ip_addresses:", observed)
    assert observed == ['9.9.9.9']
