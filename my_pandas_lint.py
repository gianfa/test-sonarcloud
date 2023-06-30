import astroid
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class PandasChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'pandas-checker'

    MSG_ID = 'invalid-pandas-method'
    MSG = 'Invalid Pandas method used: %s'

    def visit_call(self, node):
        if not isinstance(node.func, astroid.Attribute):
            return
        if node.func.attrname not in ['read_csv', 'read_excel', 'to_csv', 'to_excel']:
            return
        if not node.func.expr or node.func.expr.name != 'pd':
            return
        self.add_message(self.MSG_ID, node=node, args=(node.func.attrname,),)


def register(linter):
    linter.register_checker(PandasChecker(linter))


# class PandasCustomCheck(BaseChecker):
#     __implements__ = IAstroidChecker

#     name = 'pandas-custom-check'
#     priority = -1
#     msgs = {
#         'W9999': (
#             'Evitare l\'uso di cicli per il DataFrame di Pandas',
#             'pandas-loop',
#             'Il ciclo è inefficiente, usa le funzioni di Pandas'
#         ),
#     }

#     def visit_for(self, node):
#         if isinstance(node.iter, astroid.Call) and node.iter.func.name in ('iterrows', 'itertuples'):
#             self.add_message('pandas-loop', node=node)

# def register(linter):
#     linter.register_checker(PandasCustomCheck(linter))