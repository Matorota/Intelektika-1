#!/usr/bin/env python3
import sys
sys.stdout = sys.stderr  # Force all output to stderr

exec(open('search_algorithms_data.py').read())
