"""EPI Python — Exercise 19.4: Implement a Thread Pool

Chapter 19: Parallel Computing
Textbook: pages 294–295 (printed page numbers; the server program on 294;
the question, hint, solution and both improved programs on 295).

PROBLEM (from the textbook)
---------------------------
The following program, implements part of a simple HTTP server:

(The book's program: SERVERPORT = 8080 and a main() that creates a TCP
server socket with socket.socket(socket.AF_INET, socket.SOCK_STREAM), binds
it to ('', SERVERPORT), calls listen(5), then loops forever: accept() a
connection and call process_req(sock) on it directly.)

Suppose you find that the program has poor performance because it
frequently blocks on I/O. What steps could you take to improve the
program's performance? Feel free to use any utilities from the standard
library, including concurrency classes.

HINT (from the textbook)
------------------------
Use multithreading, but control the number of threads.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
1. First attempt: instead of processing each request in the accepting
   loop, start a new thread per request, i.e.
   threading.Thread(target=process_req, args=(sock,)).start() for each
   accepted socket.

2. Problem: the number of threads is uncontrolled. Each thread costs
   nontrivial resources — time to start and end it, and memory. A lightly
   loaded server may not notice, but under load this can cause exceptions
   that are hard, maybe impossible, to handle.

3. The right trade-off is a thread pool: a bounded-size collection of
   threads. A pool can be built fairly easily on a blocking queue (the book
   describes it as a queue that blocks the writing thread on a put until
   the queue is empty). But since the problem allows library routines, the
   book simply uses concurrent.futures.ThreadPoolExecutor with
   max_workers=NTHREADS (NTHREADS = 2) and, for each accepted socket,
   executor.submit(process_req, sock).

This file does not open sockets. Instead process_requests(requests,
process_req, max_workers=2) is a finite, testable adapter that submits each
request to a ThreadPoolExecutor exactly as the book's loop does, then
collects the results.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
process_requests([1, 2, 3], lambda item: item * item) runs the squaring
"handler" on at most 2 worker threads and returns [1, 4, 9] (results in
submission order).
"""

# Python standard library: high-level interface for running callables
# asynchronously on pools of threads or processes.
# Module documentation: https://docs.python.org/3/library/concurrent.futures.html
# ThreadPoolExecutor API: https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
# Executor.submit / Future.result: https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.submit
#                                  https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.result
from concurrent.futures import ThreadPoolExecutor


def process_requests(requests, process_req, max_workers=2):
    """Finite testable adapter to the book's server-side executor.submit loop.

    Mirrors the textbook's thread-pool solution: each request is handed to
    a ThreadPoolExecutor with a bounded number of workers (book:
    NTHREADS = 2). Returns the handlers' results in request order.
    """

    # ThreadPoolExecutor(max_workers=k) creates a pool of at most k worker
    # threads that are REUSED for many tasks — the bound the book wants.
    #
    # Used in a `with` statement, the executor is shut down automatically
    # at the end of the block: shutdown(wait=True) waits for all submitted
    # tasks to finish and then stops the worker threads.
    with ThreadPoolExecutor(max_workers=max_workers) as executor:

        # executor.submit(fn, arg) schedules fn(arg) on a pool thread and
        # immediately returns a Future, a handle to the eventual result.
        # Extra tasks wait in the executor's internal queue until a worker
        # is free. This list comprehension submits every request.
        futures = [executor.submit(process_req, request) for request in requests]

        # future.result() blocks until that task has finished and returns
        # its value (or re-raises the exception the task raised). Iterating
        # over `futures` in order keeps the results in request order.
        return [future.result() for future in futures]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 295)
# --------------------------------------------
# The book's solution ends with the ThreadPoolExecutor program; it gives no
# complexity analysis or further remarks.
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - The book prints three socket-server programs: the original
#   single-threaded main() calling process_req(sock); a thread-per-request
#   version using threading.Thread(target=process_req, args=(sock,));
#   and the thread-pool version with
#   `executor = concurrent.futures.ThreadPoolExecutor(max_workers=NTHREADS)`
#   and `executor.submit(process_req, sock)` in an infinite accept loop.
#   None of these socket programs is in the file.
# - The file's `process_requests(requests, process_req, max_workers=2)` is
#   an added adapter: it takes a finite list of request objects instead of
#   accepting sockets, takes the handler as a parameter (the book's
#   process_req is undefined there), uses the executor as a context
#   manager, and returns the handlers' results via Future.result().
# - Import: book `concurrent.futures.ThreadPoolExecutor` (module-qualified);
#   file `from concurrent.futures import ThreadPoolExecutor`. The book also
#   uses the socket and threading modules, which the file does not import.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Three "requests" handled by a lambda (small anonymous function) that
    # squares its input, standing in for the book's process_req.
    output=process_requests([1,2,3],lambda item:item*item)
    print('Handled requests:',output)

    # `assert` raises AssertionError if the condition is False; results come
    # back in submission order even though threads may finish in any order.
    assert output==[1,4,9]
