"""
This file contains a few useful commands for parsing input and
interacting with the user via the command line.

@author: stephen.huenneke@opower.com
"""

def prompt_user_boolean(message, default):
    user_input = raw_input(message)
    if not user_input:
        return default
    if user_input and user_input.lower()[0] == "y":
        return True
    return False
