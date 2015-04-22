#!/usr/bin/env python

from psychopy import visual, core, event
from parser import Parser
import random
import pickle
import datetime


p = Parser()


while True:
    p.update()
    p.start_raw_recording("baseline_raw.csv")
    p.start_esense_recording("esense_raw.csv")
    if p.package_counter == p.package_size:
        extract_and_sent_to_c(p.package)
	#if p.sending_data:		
	#	p.start_raw_recording("baseline_raw.csv")

