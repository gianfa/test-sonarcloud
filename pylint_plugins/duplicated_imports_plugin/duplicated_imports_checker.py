# https://betterprogramming.pub/how-to-easily-extend-pylint-with-plugins-d8ead26a68ac
"""duplicated import from checker"""
from typing import TYPE_CHECKING, Any, Optional
from typing import Set
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

if TYPE_CHECKING:
    from pylint.lint import PyLinter


class DuplicateFromImportsChecker(BaseChecker):

    __implements__ = IAstroidChecker

    name = "duplicated-from-imports"
    priority = -1
    msgs = {
        # <Pylint hint [C, R, W, E, F]>: <unique ID>
        "W8801": (
            "Import from '%s' module is duplicated",  # msg to be displayes
            "duplication-module-imports",  # msg lookup name
            "Combine the duplicated imports",  # recommendation 
        ),
    }

    def __init__(self, linter: Optional["PyLinter"] = None) -> None:
        super().__init__(linter)
        self._imports: Set[Any] = set()

    def leave_module(self, _):
        self._imports.clear()

    def visit_importfrom(self, node: nodes.ImportFrom) -> None:
        if node.modname in self._imports:
            self.add_message(
                "duplication-module-imports", node=node, args=(node.modname,)
            )
        self._imports.add(node.modname)