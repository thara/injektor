# -*- coding: utf-8 -*-
import unittest
from injektor import Bindings, Injected

bindings_1 = Bindings()
bindings_2 = Bindings()


class Sample1:
    sample_injected_1 = Injected('sample_injected_1', bindings_1)


class Sample2:
    sample_injected_2 = Injected('sample_injected_2', bindings_2)


class TestInjected(unittest.TestCase):

    def test_injected_binding_object(self):
        injected_object = object()
        bindings_1.register('sample_injected_1', injected_object)

        obj = Sample1()
        self. assertTrue(obj.sample_injected_1 is injected_object)

    @unittest.expectedFailure
    def test_fail(self):

        obj = Sample2()
        obj.sample_injected_2
