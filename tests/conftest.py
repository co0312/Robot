"""Path hack to make tests work."""
import sys
import os

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(TEST_DIR)  # to import this file from test code.
ROOT_DIR = os.path.dirname(TEST_DIR)
sys.path.append(ROOT_DIR)