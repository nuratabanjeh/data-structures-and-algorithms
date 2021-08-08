from stackQueue import (Node, Stack,Queue)
import pytest

def testingPush(stack_3_vals):
    def testingPush(stack_3_vals):
    # Can successfully push multiple values onto a stack
        actual = stack_3_vals.top.value
        expected = 'd'
        assert actual == expected