# This file will contain the custom errors classes to handle misinterpretation of the ASM code.

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidRegister(Error):
    """Raised when a register is inputted that is not valid"""

class InvalidValue(Error):
    """Raised when a value is inputted that is not valid"""

class InvalidVariable(Error):
    """Raised when an operation is inputted that is not valid"""
