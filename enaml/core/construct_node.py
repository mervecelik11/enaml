#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
from atom.api import Atom, Str, Typed, ForwardTyped, List

from .expression_engine import ExpressionEngine


class ConstructNode(Atom):
    """ A node class which holds an enamldef type structure.

    A construct node is an abstract representation of the tree described
    by an 'enamldef' block. Unlike the AST generated by the parser, this
    tree will contain resolved class objects and the other information
    needed to create an instance of the 'enamldef'.

    """
    #: The declarative class object to instantiate.
    klass = Typed(type)

    #: The local identifier to associate with the instances.
    identifier = Str()

    #: The construct node children of this node.
    children = List(ForwardTyped(lambda: ConstructNode))

    #: The engine to use for the created declarative instances.
    engine = Typed(ExpressionEngine)

    #: The key for the local scope in the local storage map.
    scope_key = Typed(object)
