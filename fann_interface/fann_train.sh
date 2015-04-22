#!/bin/bash

gcc -lfann -l m train_pkgs_eeg.c -o train_pkgs_eeg_prog
./train_pkgs_eeg_prog
