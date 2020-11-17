#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `awesome_project` package."""

# Third party modules
import pytest

# First party modules
import awesome_project


def test_version():
    assert awesome_project.__version__.count(".") == 2


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
