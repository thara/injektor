# -*- coding: utf-8 -*-
"""
Injektor is a simple, lightweight, easy-to-use dependency injection framework.
It is distributed as a single file module and has no dependencies other than the Python Standard Library.
"""
__author__ = 'Tomochika Hara'
__version__ = '0.1.0'
__license__ = 'MIT'


class Bindings(object):
    """ Mappings from a name to the object"""

    def __init__(self):
        self._mappings = {}

    def register(self, name, binding):
        assert isinstance(name, str)
        assert binding is not None
        self._mappings[name] = binding

    def lookup(self, name):
        return self._mappings[name]


class Injected(object):

    def __init__(self, name, bindings):
        assert isinstance(name, str)
        assert bindings is not None
        self.name = name
        self.bindings = bindings
        self._attr_name = "__injected_" + name

    def __get__(self, obj, objtype):
        if hasattr(obj, self._attr_name):
            return getattr(obj, self._attr_name)
        value = self.bindings.lookup(self.name)
        setattr(obj, self._attr_name, value)
        return value
