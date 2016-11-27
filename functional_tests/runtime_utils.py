# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

"""Utilities for running functional tests as scripts."""


import argparse
import contextlib
import inspect
import types

import numpy as np
import six


EPS = 2.0**(-50)


def _assert_close(approximated, exact, wiggle=8):
    """Assert that two floating point values are close.

    Makes sure the error is isolated to (approximately) the last 3 bits.
    The last 3 bits would amplify the "least significant digit" by 8, and
    4 bits would amplify by 16, etc.

    In the case that ``exact`` is exactly 0, we set an "absolute"
    tolerance for ``approximated`` rather than a relative tolerance.

    Args:
        approximated (float): The value that was computed.
        exact (float): The expected value.
        wiggle (Optional[int]): The amount of wiggle room allowed (relative
            to the smallest value).
    """
    if exact == 0.0:
        assert abs(approximated) < EPS
    else:
        local_epsilon = np.spacing(exact)  # pylint: disable=no-member
        assert abs(approximated - exact) < wiggle * abs(local_epsilon)


def _start_line(func):
    """Get the start line (in source) of a function.

    Args:
        func (~types.FunctionType): A Python function object.

    Returns:
        int: The start line (in source).
    """
    _, line = inspect.getsourcelines(func)
    return line


def get_parser():
    """Create a command line argument parser.

    Returns:
        argparse.ArgumentParser: An argument parser for functional tests.
    """
    parser = argparse.ArgumentParser(
        description='Run functional tests.')
    parser.add_argument('--save-plot', dest='save_plot',
                        action='store_true')
    return parser


class Config(object):  # pylint: disable=too-few-public-methods
    """Run-time configuration.

    This is a mutable stand-in to allow test set-up to modify
    global state.
    """

    def __init__(self):
        self.running = False
        self.save_plot = False
        self.current_test = None
        self.parser = get_parser()
        self._wiggle = 8

    def _run(self, mod_globals):
        """Run all tests, in source order.

        Args:
            mod_globals (dict): The globals from a module.
        """
        found = []
        for key, value in six.iteritems(mod_globals):
            if not key.lower().startswith('test'):
                continue
            if not isinstance(value, types.FunctionType):
                continue
            found.append(value)

        found.sort(key=_start_line)

        for func in found:
            self.current_test = func.__name__
            func()

    @contextlib.contextmanager
    def wiggle(self, wiggle):
        """Make the context use a temporary wiggle room.

        Args:
            wiggle (int): The temporary amount of wiggle room.
        """
        old_wiggle = self._wiggle
        try:
            self._wiggle = wiggle
            yield self
        finally:
            self._wiggle = old_wiggle

    def assert_close(self, approximated, exact):
        """Assert two values are close, with the local configuration in place.

        Calls :func:`_assert_close` with the current configuration.

        Args:
            approximated (float): The value that was computed.
            exact (float): The expected value.
        """
        _assert_close(approximated, exact, wiggle=self._wiggle)

    def run(self, mod_globals):
        """Run all tests, in source order.

        Args:
            mod_globals (dict): The globals from a module.
        """
        running = self.running
        save_plot = self.save_plot
        try:
            self.running = True
            args = self.parser.parse_args()
            self.save_plot = args.save_plot
            self._run(mod_globals)
        finally:
            self.running = running
            self.save_plot = save_plot
            self.current_test = None