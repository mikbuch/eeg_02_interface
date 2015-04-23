#!/usr/bin/env python

from psychopy import visual, core, event
from parser import Parser
import feature
import subprocess as sp  

# main_win = visual.Window([2560, 1440],monitor='testMonitor', \
#         winType='pyglet', units='pix', fullscr = True)
main_win = visual.Window([300, 300],monitor='testMonitor', \
        winType='pyglet', units='pix', fullscr = False)
main_win.setMouseVisible(False)


bulb_onn = visual.ImageStim(win=main_win, image='bulb_onn.png', pos=(0,0))
bulb_off = visual.ImageStim(win=main_win, image='bulb_off.png', pos=(0,0))

blinks_count = 0
pkg_buffor = 0
bulb_on = False

p = Parser()

bulb_off.draw()
main_win.flip()

while True:
    p.update()
    p.start_raw_recording("baseline_raw.csv")
#     print(str(p.package_counter) + ' counter')
    if p.package_counter > p.package_size - 9:
        pkg_buffor += 1
#         print('counter: ' + str(p.package_counter))
#         print('len: ' + str(len(p.package)))
#         print(p.package)
#         print('')
        fann_out = feature.zero_negative(p.package)
        params = ''
        for param in fann_out:
            params += ' ' + str(param)
        cmd = 'fann_interface/decide_pkg_eeg' + params 
        process = sp.Popen(cmd,stdout=sp.PIPE,shell=True)
        output = process.communicate()[0]
        if float(output) > 0.5:
            blinks_count += 1
        if pkg_buffor == 8:
            if blinks_count > 5:
                print('blink ' + str(blinks_count))
                if not bulb_on:
                    bulb_onn.draw()
                    main_win.flip()
                    bulb_on = True
                else:
                    bulb_off.draw()
                    main_win.flip()
                    bulb_on = False
            else:
                print('not blink ' + str(blinks_count))
            pkg_buffor = 0
            blinks_count = 0

main_win.close()
