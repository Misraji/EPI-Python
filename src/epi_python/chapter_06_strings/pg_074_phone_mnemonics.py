"""EPI exercise 6.7, printed page 74: Compute all mnemonics for a phone number.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute all mnemonics for a phone number.
Method/complexity: Recursive search over all keypad choices; O(n * 4^n) construction time, O(n) recursion memory excluding output.
For the book's original explanation and variants, see:
    pg_074_exercise_06_07_compute_all_mnemonics_for_a_phone_number.md

Run: python -m epi_python.chapter_06_strings.pg_074_phone_mnemonics
Test: python -m pytest tests/chapter_06_strings/test_pg_074_phone_mnemonics.py -v
"""

PHONE = ("0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ")


def phone_mnemonic(phone_number: str) -> list[str]:
    """Generate every letter sequence represented by a keypad number."""
    if any(ch not in "0123456789" for ch in phone_number):
        raise ValueError("Phone number must contain only digits")
    result = []
    candidate = [''] * len(phone_number)

    def search(pos: int) -> None:
        if pos == len(phone_number):
            result.append(''.join(candidate))
            return
        for letter in PHONE[int(phone_number[pos])]:
            candidate[pos] = letter
            search(pos + 1)

    search(0)
    return result


if __name__ == "__main__":
    print("phone 23:", phone_mnemonic("23"))
    assert len(phone_mnemonic("23")) == 9
