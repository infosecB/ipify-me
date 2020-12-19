#!/usr/bin/env python

"""Tests for `ipify_me` package."""


import unittest
import re
from click.testing import CliRunner

# from ipify_me import ipify_me
from ipify_me import cli
from ipify_me import core

class TestIpify_me(unittest.TestCase):
    """Tests for `ipify_me` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test the Get IP function."""
        result = core.get_ipify_ip()
        assert re.search('\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b', result) == True

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'Your external IP' in result.output
