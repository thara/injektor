# -*- coding: utf-8 -*-
__author__ = 'Tomochika Hara'
__version__ = '0.1.0'
__license__ = 'MIT'


class Injector(object):

    def __init__(self):
        self.bindings = {}

    def register(self, name, binding):
        assert isinstance(name, str)
        assert binding is not None
        self.bindings[name] = binding

    def lookup(self, name):
        return self.bindings[name]


class Inject(object):

    def __init__(self, name, injector):
        assert isinstance(name, str)
        assert injector is not None
        self.name = name
        self.injector = injector
        self._attr_name = "__injected_" + name

    def __get__(self, obj, objtype):
        if hasattr(obj, self._attr_name):
            return getattr(obj, self._attr_name)
        value = self.injector.lookup(self.name)
        setattr(obj, self._attr_name, value)
        return value
