#!/bin/bash
# Script to clean database from Como Vamos Colombia
python3 pythondeleter.py
python3 columns.py
python3 replacer.py
python3 transfer.py
