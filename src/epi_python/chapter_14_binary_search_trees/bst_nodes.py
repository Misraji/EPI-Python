"""Reusable BST node for the exercises in Chapter 14."""

# dataclass generates an initializer, reducing repetitive class boilerplate.
# https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass(eq=False)
class BSTNode:
    data: int
    left: "BSTNode | None" = None
    right: "BSTNode | None" = None
