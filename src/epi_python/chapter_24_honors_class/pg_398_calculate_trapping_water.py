"""EPI Python 24.32, textbook printed page 398: Trapping water.

QUESTION: Trap rainwater between histogram bars.

TEXTBOOK ALGORITHM: The PDF splits at a maximum-height bar, then accumulates left- and right-side water using running maxima.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_398_calculate_trapping_water
Test: python -m pytest tests/chapter_24_honors_class/test_pg_398_calculate_trapping_water.py -v
"""

def calculate_trapping_water(heights: list[int]) -> int:
    if not heights:
        return 0
    max_h = heights.index(max(heights))

    def trapping_water_till_end(values):
        volume = 0
        highest_level_seen = float('-inf')
        for height in values:
            if height >= highest_level_seen:
                highest_level_seen = height
            else:
                volume += highest_level_seen - height
        return volume

    return (trapping_water_till_end(heights[:max_h])
            + trapping_water_till_end(reversed(heights[max_h + 1:])))


if __name__ == '__main__':
    example = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print('Trapped volume:', calculate_trapping_water(example))
    assert calculate_trapping_water(example) == 6
