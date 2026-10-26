"""EPI Python 19.4, textbook printed page 294: Implement a thread pool.

QUESTION: Keep an I/O-bound request-processing server from launching unlimited threads.

TEXTBOOK ALGORITHM: Use the PDF ThreadPoolExecutor(max_workers=NTHREADS) and submit each accepted request to its pool. Runnable adapter uses request objects instead of opening a perpetual socket server.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_19_parallel_computing.pg_294_thread_pool_server
Test: python -m pytest tests/chapter_19_parallel_computing/test_pg_294_thread_pool_server.py -v
"""

# concurrent.futures.ThreadPoolExecutor documentation: https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor


def process_requests(requests, process_req, max_workers=2):
    """Finite testable adapter to the book's server-side executor.submit loop."""
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_req, request) for request in requests]
        return [future.result() for future in futures]


if __name__=='__main__':
    output=process_requests([1,2,3],lambda item:item*item)
    print('Handled requests:',output)
    assert output==[1,4,9]
