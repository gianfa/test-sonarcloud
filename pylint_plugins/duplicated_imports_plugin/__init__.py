# ~./pylint_plugins/duplicated_imports_plugin/__init__.py~#
"""main plugin"""


from typing import TYPE_CHECKING

from duplicated_imports_plugin.duplicated_imports_checker import (
    DuplicateFromImportsChecker,
)


if TYPE_CHECKING:
    from pylint.lint import PyLinter


def register(linter: "PyLinter") -> None:
    """register is auto recognized by pylints plugins manager"""
    linter.register_checker(DuplicateFromImportsChecker(linter))