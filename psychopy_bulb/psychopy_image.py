#!/usr/bin/env python2

from psychopy import visual, core, event, gui

mywin = visual.Window([2560, 1440],monitor='testMonitor', \
        winType='pyglet', units='pix', fullscr = True)
mywin.setMouseVisible(False)


bulb_onn = visual.ImageStim(win=mywin, image='bulb_onn.png', pos=(0,0))
bulb_off = visual.ImageStim(win=mywin, image='bulb_off.png', pos=(0,0))

while not 'space' in event.getKeys():
    key_pressed=event.waitKeys(keyList=['1','2','3','4','5','delete'])
    if ('1' in key_pressed):
        bulb_onn.draw()
        mywin.flip()
    if ('2' in key_pressed):
        bulb_off.draw()
        mywin.flip()
    if ('3' in key_pressed):
        pass
    if ('4' in key_pressed):
        pass
    if ('4' in key_pressed):
        pass
    if ('5' in key_pressed):
        pass
    if ('delete' in key_pressed):
        break


mywin.close()
