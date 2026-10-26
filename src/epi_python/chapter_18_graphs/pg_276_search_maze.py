"""EPI Python 18.1, textbook printed page 276: Search a maze.

QUESTION: Find a path through white cells of a maze from an entrance to an exit.

TEXTBOOK ALGORITHM: Depth-first search marks visited cells black and backtracks when a route fails.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_18_graphs.pg_276_search_maze
Test: python -m pytest tests/chapter_18_graphs/test_pg_276_search_maze.py -v
"""

# collections.namedtuple documentation: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple


Coordinate = namedtuple('Coordinate', ('x','y'))
WHITE, BLACK = 1, 0


def search_maze(maze: list[list[int]], s: Coordinate, e: Coordinate) -> list[Coordinate]:
    path: list[Coordinate] = []

    def search_maze_helper(cur: Coordinate) -> bool:
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x])
                and maze[cur.x][cur.y] == WHITE):
            return False
        path.append(cur)
        maze[cur.x][cur.y] = BLACK
        if cur == e:
            return True
        if any(map(search_maze_helper,
                   (Coordinate(cur.x-1,cur.y), Coordinate(cur.x+1,cur.y),
                    Coordinate(cur.x,cur.y-1), Coordinate(cur.x,cur.y+1)))):
            return True
        del path[-1]
        return False

    return path if search_maze_helper(s) else []


if __name__ == '__main__':
    maze=[[1,1,0],[0,1,1],[1,0,1]]
    route=search_maze(maze,Coordinate(0,0),Coordinate(2,2))
    print('Maze route:',route)
    assert route and route[0]==(0,0) and route[-1]==(2,2)
