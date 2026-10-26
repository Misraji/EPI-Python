"""EPI 18.4: Deadlock detection, printed page 281.

Educational reconstruction, not a verbatim transcription. Algorithm: DFS active recursion-stack color identifies back edges (cycles).
The corresponding chapter's exercise Markdown retains the PDF text-layer
explanations, question and variants (with known OCR mistakes).

Run: python -m epi_python.chapter_18_graphs.pg_281_is_deadlocked
Tests: python -m pytest tests/chapter_18_graphs/test_pg_281_is_deadlocked.py -v
"""

def is_deadlocked(adjacency: list[list[int]]) -> bool:
    """Detect a directed cycle in a wait-for graph using DFS colors."""
    state=[0]*len(adjacency)  # 0 unseen, 1 visiting, 2 completed
    def visit(node):
        if state[node]==1:
            return True
        if state[node]==2:
            return False
        state[node]=1
        for neighbor in adjacency[node]:
            if visit(neighbor):
                return True
        state[node]=2
        return False
    return any(visit(index) for index in range(len(adjacency)) if state[index]==0)

if __name__ == "__main__":
    # Executable demonstration cases; pytest has the full set.
    result=is_deadlocked([])
    print('is_deadlocked', result)
    assert result == False
    result=is_deadlocked([[1], [2], []])
    print('is_deadlocked', result)
    assert result == False
    result=is_deadlocked([[1], [2], [0]])
    print('is_deadlocked', result)
    assert result == True
    result=is_deadlocked([[0]])
    print('is_deadlocked', result)
    assert result == True
