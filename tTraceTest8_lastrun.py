#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on August 11, 2020, at 17:22
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'tTraceTest8'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Clifton\\Documents\\psych-proj\\tTraceTest8\\tTraceTest8_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1088, 614], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "setup"
setupClock = core.Clock()
posArray1 = [-0.05,-0.1,-0.15,-0.2,-0.25,-0.3,-0.35,-0.4,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4]
posArray2 = [-0.05,-0.1,-0.15,-0.2,-0.25,-0.3,-0.35,-0.4,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4]



# Initialize components for Routine "instr"
instrClock = core.Clock()
instrText = visual.TextStim(win=win, name='instrText',
    text='The order is 1, A, 2, B, 3, C, 4, D, 5, E, 6, F, 7, G, 8, H. Press space to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instrResp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
def drawLine(shapeList):
    lines = []
    if not len(shapeList)%2:  # shapes joined
        while len(shapeList):
            pos1 = shapeList.pop()
            pos2 = shapeList.pop()
            lines.append(visual.Line(win, start=pos1.pos, end=pos2.pos))
    if len(lines):
        for line in lines:
            line.setAutoDraw(True)
trialMouse = event.Mouse(win=win)
x, y = [None, None]
trialMouse.mouseClock = core.Clock()
trialCursor = visual.Polygon(
    win=win, name='trialCursor',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
trialTarget1 = visual.Polygon(
    win=win, name='trialTarget1',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
trialTarget2 = visual.Polygon(
    win=win, name='trialTarget2',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-4.0, interpolate=True)
trialTarget3 = visual.Polygon(
    win=win, name='trialTarget3',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-5.0, interpolate=True)
trialTarget4 = visual.Polygon(
    win=win, name='trialTarget4',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-6.0, interpolate=True)
trialTarget5 = visual.Polygon(
    win=win, name='trialTarget5',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-7.0, interpolate=True)
trialTarget6 = visual.Polygon(
    win=win, name='trialTarget6',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-8.0, interpolate=True)
trialTarget7 = visual.Polygon(
    win=win, name='trialTarget7',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-9.0, interpolate=True)
trialTarget8 = visual.Polygon(
    win=win, name='trialTarget8',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-10.0, interpolate=True)
trialTargetA = visual.Polygon(
    win=win, name='trialTargetA',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-11.0, interpolate=True)
trialTargetB = visual.Polygon(
    win=win, name='trialTargetB',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-12.0, interpolate=True)
trialTargetC = visual.Polygon(
    win=win, name='trialTargetC',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-13.0, interpolate=True)
trialTargetD = visual.Polygon(
    win=win, name='trialTargetD',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-14.0, interpolate=True)
trialTargetE = visual.Polygon(
    win=win, name='trialTargetE',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-15.0, interpolate=True)
trialTargetF = visual.Polygon(
    win=win, name='trialTargetF',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-16.0, interpolate=True)
trialTargetG = visual.Polygon(
    win=win, name='trialTargetG',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-17.0, interpolate=True)
trialTargetH = visual.Polygon(
    win=win, name='trialTargetH',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-18.0, interpolate=True)
# Set experiment start values for variable component trialStep
trialStep = 0
trialStepContainer = []
trialText1 = visual.TextStim(win=win, name='trialText1',
    text='1',
    font='Arial',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);
trialText2 = visual.TextStim(win=win, name='trialText2',
    text='2',
    font='Arial',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-21.0);
trialText3 = visual.TextStim(win=win, name='trialText3',
    text='3',
    font='Arial',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-22.0);
trialText4 = visual.TextStim(win=win, name='trialText4',
    text='4',
    font='Arial',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-23.0);
trialText5 = visual.TextStim(win=win, name='trialText5',
    text='5',
    font='Arial',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-24.0);
trialText6 = visual.TextStim(win=win, name='trialText6',
    text='6',
    font='Arial',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-25.0);
trialText7 = visual.TextStim(win=win, name='trialText7',
    text='7',
    font='Arial',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-26.0);
trialText8 = visual.TextStim(win=win, name='trialText8',
    text='8',
    font='Arial',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-27.0);
trialTextA = visual.TextStim(win=win, name='trialTextA',
    text='A',
    font='Arial',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-28.0);
trialTextB = visual.TextStim(win=win, name='trialTextB',
    text='B',
    font='Arial',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-29.0);
trialTextC = visual.TextStim(win=win, name='trialTextC',
    text='C',
    font='Arial',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-30.0);
trialTextD = visual.TextStim(win=win, name='trialTextD',
    text='D',
    font='Arial',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-31.0);
trialTextE = visual.TextStim(win=win, name='trialTextE',
    text='E',
    font='Arial',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-32.0);
trialTextF = visual.TextStim(win=win, name='trialTextF',
    text='F',
    font='Arial',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-33.0);
trialTextG = visual.TextStim(win=win, name='trialTextG',
    text='G',
    font='Arial',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-34.0);
trialTextH = visual.TextStim(win=win, name='trialTextH',
    text='H',
    font='Arial',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-35.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
tasks = data.TrialHandler(nReps=5, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='tasks')
thisExp.addLoop(tasks)  # add the loop to the experiment
thisTask = tasks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTask.rgb)
if thisTask != None:
    for paramName in thisTask:
        exec('{} = thisTask[paramName]'.format(paramName))

for thisTask in tasks:
    currentLoop = tasks
    # abbreviate parameter names if possible (e.g. rgb = thisTask.rgb)
    if thisTask != None:
        for paramName in thisTask:
            exec('{} = thisTask[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    shuffle(posArray1)
    shuffle(posArray2)
    pos1 = posArray1[0]
    pos2 = posArray2[0]
    pos3 = posArray1[1]
    pos4 = posArray2[1]
    pos5 = posArray1[2]
    pos6 = posArray2[2]
    pos7 = posArray1[3]
    pos8 = posArray2[3]
    pos9 = posArray1[4]
    pos10 = posArray2[4]
    pos11 = posArray1[5]
    pos12 = posArray2[5]
    pos13 = posArray1[6]
    pos14 = posArray2[6]
    pos15 = posArray1[7]
    pos16 = posArray2[7]
    pos17 = posArray1[8]
    pos18 = posArray2[8]
    pos19 = posArray1[9]
    pos20 = posArray2[9]
    pos21 = posArray1[10]
    pos22 = posArray2[10]
    pos23 = posArray1[11]
    pos24 = posArray2[11]
    pos25 = posArray1[12]
    pos26 = posArray2[12]
    pos27 = posArray1[13]
    pos28 = posArray2[13]
    pos29 = posArray1[14]
    pos30 = posArray2[14]
    pos31 = posArray1[15]
    pos32 = posArray2[15]
    instrResp.keys = []
    instrResp.rt = []
    _instrResp_allKeys = []
    # keep track of which components have finished
    instrComponents = [instrText, instrResp]
    for thisComponent in instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instr"-------
    while continueRoutine:
        # get current time
        t = instrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instrText* updates
        if instrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrText.frameNStart = frameN  # exact frame index
            instrText.tStart = t  # local t and not account for scr refresh
            instrText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
            instrText.setAutoDraw(True)
        
        # *instrResp* updates
        waitOnFlip = False
        if instrResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrResp.frameNStart = frameN  # exact frame index
            instrResp.tStart = t  # local t and not account for scr refresh
            instrResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrResp, 'tStartRefresh')  # time at next scr refresh
            instrResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instrResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instrResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instrResp.status == STARTED and not waitOnFlip:
            theseKeys = instrResp.getKeys(keyList=['space'], waitRelease=False)
            _instrResp_allKeys.extend(theseKeys)
            if len(_instrResp_allKeys):
                instrResp.keys = _instrResp_allKeys[-1].name  # just the last key pressed
                instrResp.rt = _instrResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr"-------
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    tasks.addData('instrText.started', instrText.tStartRefresh)
    tasks.addData('instrText.stopped', instrText.tStopRefresh)
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        trialCursor.pos = (1.5,1.5)
        trialMouse.pos = (1.5,1.5)
        
        targetOpac1 = 0.25
        targetOpac2 = 0.25
        targetOpac3 = 0.25
        targetOpac4 = 0.25
        targetOpac5 = 0.25
        targetOpac6 = 0.25
        targetOpac7 = 0.25
        targetOpac8 = 0.25
        targetOpacA = 0.25
        targetOpacB = 0.25
        targetOpacC = 0.25
        targetOpacD = 0.25
        targetOpacE = 0.25
        targetOpacF = 0.25
        targetOpacG = 0.25
        targetOpacH = 0.25
        
        trialStep = 1
        steps = []
        shapeList = []
        # setup some python lists for storing info about the trialMouse
        trialMouse.x = []
        trialMouse.y = []
        trialMouse.leftButton = []
        trialMouse.midButton = []
        trialMouse.rightButton = []
        trialMouse.time = []
        gotValidClick = False  # until a click is received
        trialMouse.mouseClock.reset()
        trialTarget1.setPos((pos1, pos2))
        trialTarget2.setPos((pos5, pos6))
        trialTarget3.setPos((pos9, pos10))
        trialTarget4.setPos((pos13, pos14))
        trialTarget5.setPos((pos15, pos16))
        trialTarget6.setPos((pos17, pos18))
        trialTarget7.setPos((pos19, pos20))
        trialTarget8.setPos((pos21, pos22))
        trialTargetA.setPos((pos3, pos4))
        trialTargetB.setPos((pos7, pos8))
        trialTargetC.setPos((pos11, pos12))
        trialTargetD.setPos((pos23, pos24))
        trialTargetE.setPos((pos25, pos26))
        trialTargetF.setPos((pos27, pos28))
        trialTargetG.setPos((pos29, pos30))
        trialTargetH.setPos((pos31, pos32))
        trialText1.setPos((pos1, pos2))
        trialText2.setPos((pos5, pos6))
        trialText3.setPos((pos9, pos10))
        trialText4.setPos((pos13, pos14))
        trialText5.setPos((pos15, pos16))
        trialText6.setPos((pos17, pos18))
        trialText7.setPos((pos19, pos20))
        trialText8.setPos((pos21, pos22))
        trialTextA.setPos((pos3, pos4))
        trialTextB.setPos((pos7, pos8))
        trialTextC.setPos((pos11, pos12))
        trialTextD.setPos((pos23, pos24))
        trialTextE.setPos((pos25, pos26))
        trialTextF.setPos((pos27, pos28))
        trialTextG.setPos((pos29, pos30))
        trialTextH.setPos((pos31, pos32))
        # keep track of which components have finished
        trialComponents = [trialMouse, trialCursor, trialTarget1, trialTarget2, trialTarget3, trialTarget4, trialTarget5, trialTarget6, trialTarget7, trialTarget8, trialTargetA, trialTargetB, trialTargetC, trialTargetD, trialTargetE, trialTargetF, trialTargetG, trialTargetH, trialText1, trialText2, trialText3, trialText4, trialText5, trialText6, trialText7, trialText8, trialTextA, trialTextB, trialTextC, trialTextD, trialTextE, trialTextF, trialTextG, trialTextH]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            steps.append(trialStep)
            
            if trialStep == 1:
                CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTarget1.pos[0])**2 + (trialCursor.pos[1]-trialTarget1.pos[1])**2)
                if (CursorTargetDistance < .05):
                    targetOpac1 = 0
                    trialStep = 2
                    shapeList.append(trialTarget1)
                    
            if trialStep == 2:
                CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTargetA.pos[0])**2 + (trialCursor.pos[1]-trialTargetA.pos[1])**2)
                if (CursorTargetDistance < .05):
                    targetOpacA = 0
                    trialStep = 3
                    shapeList.append(trialTargetA)
                    
            if trialStep == 3:
                CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTarget2.pos[0])**2 + (trialCursor.pos[1]-trialTarget2.pos[1])**2)
                if (CursorTargetDistance < .05):
                    targetOpac2 = 0
                    trialStep = 4
                    shapeList.append(trialTargetA)
                    shapeList.append(trialTarget2)
                    
            if trialStep == 4:
                CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTargetB.pos[0])**2 + (trialCursor.pos[1]-trialTargetB.pos[1])**2)
                if (CursorTargetDistance < .05):
                    targetOpacB = 0
                    trialStep = 5
                    shapeList.append(trialTarget2)
                    shapeList.append(trialTargetB)
            
            if trialStep == 5:
                CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTarget3.pos[0])**2 + (trialCursor.pos[1]-trialTarget3.pos[1])**2)
                if (CursorTargetDistance < .05):
                    targetOpac3 = 0
                    trialStep = 6
                    shapeList.append(trialTargetB)
                    shapeList.append(trialTarget3)
                    
            if trialStep == 6:
                CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTargetC.pos[0])**2 + (trialCursor.pos[1]-trialTargetC.pos[1])**2)
                if (CursorTargetDistance < .05):
                    targetOpacC = 0
                    trialStep = 7
                    shapeList.append(trialTarget3)
                    shapeList.append(trialTargetC)
            
            if trialStep == 7:
                CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTarget4.pos[0])**2 + (trialCursor.pos[1]-trialTarget4.pos[1])**2)
                if (CursorTargetDistance < .05):
                    targetOpac4 = 0
                    trialStep = 8
                    shapeList.append(trialTargetC)
                    shapeList.append(trialTarget4)
                    
            if trialStep == 8:
                CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTargetD.pos[0])**2 + (trialCursor.pos[1]-trialTargetD.pos[1])**2)
                if (CursorTargetDistance < .05):
                    targetOpacD = 0
                    trialStep = 9
                    shapeList.append(trialTarget4)
                    shapeList.append(trialTargetD)
                    
            if trialStep == 9:
                CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTarget5.pos[0])**2 + (trialCursor.pos[1]-trialTarget5.pos[1])**2)
                if (CursorTargetDistance < .05):
                    targetOpac5 = 0
                    trialStep = 10
                    shapeList.append(trialTargetD)
                    shapeList.append(trialTarget5)
            
            if trialStep == 10:
                CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTargetE.pos[0])**2 + (trialCursor.pos[1]-trialTargetE.pos[1])**2)
                if (CursorTargetDistance < .05):
                    targetOpacE = 0
                    trialStep = 11
                    shapeList.append(trialTarget5)
                    shapeList.append(trialTargetE)
            
            if trialStep == 11:
                CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTarget6.pos[0])**2 + (trialCursor.pos[1]-trialTarget6.pos[1])**2)
                if (CursorTargetDistance < .05):
                    targetOpac6 = 0
                    trialStep = 12
                    shapeList.append(trialTargetE)
                    shapeList.append(trialTarget6)
            
            if trialStep == 12:
                CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTargetF.pos[0])**2 + (trialCursor.pos[1]-trialTargetF.pos[1])**2)
                if (CursorTargetDistance < .05):
                    targetOpacF = 0
                    trialStep = 13
                    shapeList.append(trialTarget6)
                    shapeList.append(trialTargetF)
                    
            if trialStep == 13:
                CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTarget7.pos[0])**2 + (trialCursor.pos[1]-trialTarget7.pos[1])**2)
                if (CursorTargetDistance < .05):
                    targetOpac7 = 0
                    trialStep = 14
                    shapeList.append(trialTargetF)
                    shapeList.append(trialTarget7)
                    
            if trialStep == 14:
                CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTargetG.pos[0])**2 + (trialCursor.pos[1]-trialTargetG.pos[1])**2)
                if (CursorTargetDistance < .05):
                    targetOpacG = 0
                    trialStep = 15
                    shapeList.append(trialTarget7)
                    shapeList.append(trialTargetG)
            
            if trialStep == 15:
                CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTarget8.pos[0])**2 + (trialCursor.pos[1]-trialTarget8.pos[1])**2)
                if (CursorTargetDistance < .05):
                    targetOpac8 = 0
                    trialStep = 16
                    shapeList.append(trialTargetG)
                    shapeList.append(trialTarget8)
            
            if trialStep == 16:
                CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTargetH.pos[0])**2 + (trialCursor.pos[1]-trialTargetH.pos[1])**2)
                if (CursorTargetDistance < .05):
                    targetOpacH = 0
                    shapeList.append(trialTarget8)
                    shapeList.append(trialTargetH)
                    continueRoutine = False
                    
            drawLine(shapeList)
            
            # *trialMouse* updates
            if trialMouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialMouse.frameNStart = frameN  # exact frame index
                trialMouse.tStart = t  # local t and not account for scr refresh
                trialMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialMouse, 'tStartRefresh')  # time at next scr refresh
                trialMouse.status = STARTED
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            if trialMouse.status == STARTED:  # only update if started and not finished!
                x, y = trialMouse.getPos()
                trialMouse.x.append(x)
                trialMouse.y.append(y)
                buttons = trialMouse.getPressed()
                trialMouse.leftButton.append(buttons[0])
                trialMouse.midButton.append(buttons[1])
                trialMouse.rightButton.append(buttons[2])
                trialMouse.time.append(trialMouse.mouseClock.getTime())
            
            # *trialCursor* updates
            if trialCursor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialCursor.frameNStart = frameN  # exact frame index
                trialCursor.tStart = t  # local t and not account for scr refresh
                trialCursor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialCursor, 'tStartRefresh')  # time at next scr refresh
                trialCursor.setAutoDraw(True)
            if trialCursor.status == STARTED:  # only update if drawing
                trialCursor.setPos((trialMouse.getPos()[0], trialMouse.getPos()[1]), log=False)
            
            # *trialTarget1* updates
            if trialTarget1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTarget1.frameNStart = frameN  # exact frame index
                trialTarget1.tStart = t  # local t and not account for scr refresh
                trialTarget1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTarget1, 'tStartRefresh')  # time at next scr refresh
                trialTarget1.setAutoDraw(True)
            if trialTarget1.status == STARTED:  # only update if drawing
                trialTarget1.setOpacity(targetOpac1, log=False)
            
            # *trialTarget2* updates
            if trialTarget2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTarget2.frameNStart = frameN  # exact frame index
                trialTarget2.tStart = t  # local t and not account for scr refresh
                trialTarget2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTarget2, 'tStartRefresh')  # time at next scr refresh
                trialTarget2.setAutoDraw(True)
            if trialTarget2.status == STARTED:  # only update if drawing
                trialTarget2.setOpacity(targetOpac2, log=False)
            
            # *trialTarget3* updates
            if trialTarget3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTarget3.frameNStart = frameN  # exact frame index
                trialTarget3.tStart = t  # local t and not account for scr refresh
                trialTarget3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTarget3, 'tStartRefresh')  # time at next scr refresh
                trialTarget3.setAutoDraw(True)
            if trialTarget3.status == STARTED:  # only update if drawing
                trialTarget3.setOpacity(targetOpac3, log=False)
            
            # *trialTarget4* updates
            if trialTarget4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTarget4.frameNStart = frameN  # exact frame index
                trialTarget4.tStart = t  # local t and not account for scr refresh
                trialTarget4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTarget4, 'tStartRefresh')  # time at next scr refresh
                trialTarget4.setAutoDraw(True)
            if trialTarget4.status == STARTED:  # only update if drawing
                trialTarget4.setOpacity(targetOpac4, log=False)
            
            # *trialTarget5* updates
            if trialTarget5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTarget5.frameNStart = frameN  # exact frame index
                trialTarget5.tStart = t  # local t and not account for scr refresh
                trialTarget5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTarget5, 'tStartRefresh')  # time at next scr refresh
                trialTarget5.setAutoDraw(True)
            if trialTarget5.status == STARTED:  # only update if drawing
                trialTarget5.setOpacity(targetOpac5, log=False)
            
            # *trialTarget6* updates
            if trialTarget6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTarget6.frameNStart = frameN  # exact frame index
                trialTarget6.tStart = t  # local t and not account for scr refresh
                trialTarget6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTarget6, 'tStartRefresh')  # time at next scr refresh
                trialTarget6.setAutoDraw(True)
            if trialTarget6.status == STARTED:  # only update if drawing
                trialTarget6.setOpacity(targetOpac6, log=False)
            
            # *trialTarget7* updates
            if trialTarget7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTarget7.frameNStart = frameN  # exact frame index
                trialTarget7.tStart = t  # local t and not account for scr refresh
                trialTarget7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTarget7, 'tStartRefresh')  # time at next scr refresh
                trialTarget7.setAutoDraw(True)
            if trialTarget7.status == STARTED:  # only update if drawing
                trialTarget7.setOpacity(targetOpac7, log=False)
            
            # *trialTarget8* updates
            if trialTarget8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTarget8.frameNStart = frameN  # exact frame index
                trialTarget8.tStart = t  # local t and not account for scr refresh
                trialTarget8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTarget8, 'tStartRefresh')  # time at next scr refresh
                trialTarget8.setAutoDraw(True)
            if trialTarget8.status == STARTED:  # only update if drawing
                trialTarget8.setOpacity(targetOpac8, log=False)
            
            # *trialTargetA* updates
            if trialTargetA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTargetA.frameNStart = frameN  # exact frame index
                trialTargetA.tStart = t  # local t and not account for scr refresh
                trialTargetA.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTargetA, 'tStartRefresh')  # time at next scr refresh
                trialTargetA.setAutoDraw(True)
            if trialTargetA.status == STARTED:  # only update if drawing
                trialTargetA.setOpacity(targetOpacA, log=False)
            
            # *trialTargetB* updates
            if trialTargetB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTargetB.frameNStart = frameN  # exact frame index
                trialTargetB.tStart = t  # local t and not account for scr refresh
                trialTargetB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTargetB, 'tStartRefresh')  # time at next scr refresh
                trialTargetB.setAutoDraw(True)
            if trialTargetB.status == STARTED:  # only update if drawing
                trialTargetB.setOpacity(targetOpacB, log=False)
            
            # *trialTargetC* updates
            if trialTargetC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTargetC.frameNStart = frameN  # exact frame index
                trialTargetC.tStart = t  # local t and not account for scr refresh
                trialTargetC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTargetC, 'tStartRefresh')  # time at next scr refresh
                trialTargetC.setAutoDraw(True)
            if trialTargetC.status == STARTED:  # only update if drawing
                trialTargetC.setOpacity(targetOpacC, log=False)
            
            # *trialTargetD* updates
            if trialTargetD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTargetD.frameNStart = frameN  # exact frame index
                trialTargetD.tStart = t  # local t and not account for scr refresh
                trialTargetD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTargetD, 'tStartRefresh')  # time at next scr refresh
                trialTargetD.setAutoDraw(True)
            if trialTargetD.status == STARTED:  # only update if drawing
                trialTargetD.setOpacity(targetOpacD, log=False)
            
            # *trialTargetE* updates
            if trialTargetE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTargetE.frameNStart = frameN  # exact frame index
                trialTargetE.tStart = t  # local t and not account for scr refresh
                trialTargetE.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTargetE, 'tStartRefresh')  # time at next scr refresh
                trialTargetE.setAutoDraw(True)
            if trialTargetE.status == STARTED:  # only update if drawing
                trialTargetE.setOpacity(targetOpacE, log=False)
            
            # *trialTargetF* updates
            if trialTargetF.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTargetF.frameNStart = frameN  # exact frame index
                trialTargetF.tStart = t  # local t and not account for scr refresh
                trialTargetF.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTargetF, 'tStartRefresh')  # time at next scr refresh
                trialTargetF.setAutoDraw(True)
            if trialTargetF.status == STARTED:  # only update if drawing
                trialTargetF.setOpacity(targetOpacF, log=False)
            
            # *trialTargetG* updates
            if trialTargetG.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTargetG.frameNStart = frameN  # exact frame index
                trialTargetG.tStart = t  # local t and not account for scr refresh
                trialTargetG.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTargetG, 'tStartRefresh')  # time at next scr refresh
                trialTargetG.setAutoDraw(True)
            if trialTargetG.status == STARTED:  # only update if drawing
                trialTargetG.setOpacity(targetOpacG, log=False)
            
            # *trialTargetH* updates
            if trialTargetH.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTargetH.frameNStart = frameN  # exact frame index
                trialTargetH.tStart = t  # local t and not account for scr refresh
                trialTargetH.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTargetH, 'tStartRefresh')  # time at next scr refresh
                trialTargetH.setAutoDraw(True)
            if trialTargetH.status == STARTED:  # only update if drawing
                trialTargetH.setOpacity(targetOpacH, log=False)
            
            # *trialText1* updates
            if trialText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialText1.frameNStart = frameN  # exact frame index
                trialText1.tStart = t  # local t and not account for scr refresh
                trialText1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialText1, 'tStartRefresh')  # time at next scr refresh
                trialText1.setAutoDraw(True)
            
            # *trialText2* updates
            if trialText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialText2.frameNStart = frameN  # exact frame index
                trialText2.tStart = t  # local t and not account for scr refresh
                trialText2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialText2, 'tStartRefresh')  # time at next scr refresh
                trialText2.setAutoDraw(True)
            
            # *trialText3* updates
            if trialText3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialText3.frameNStart = frameN  # exact frame index
                trialText3.tStart = t  # local t and not account for scr refresh
                trialText3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialText3, 'tStartRefresh')  # time at next scr refresh
                trialText3.setAutoDraw(True)
            
            # *trialText4* updates
            if trialText4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialText4.frameNStart = frameN  # exact frame index
                trialText4.tStart = t  # local t and not account for scr refresh
                trialText4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialText4, 'tStartRefresh')  # time at next scr refresh
                trialText4.setAutoDraw(True)
            
            # *trialText5* updates
            if trialText5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialText5.frameNStart = frameN  # exact frame index
                trialText5.tStart = t  # local t and not account for scr refresh
                trialText5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialText5, 'tStartRefresh')  # time at next scr refresh
                trialText5.setAutoDraw(True)
            
            # *trialText6* updates
            if trialText6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialText6.frameNStart = frameN  # exact frame index
                trialText6.tStart = t  # local t and not account for scr refresh
                trialText6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialText6, 'tStartRefresh')  # time at next scr refresh
                trialText6.setAutoDraw(True)
            
            # *trialText7* updates
            if trialText7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialText7.frameNStart = frameN  # exact frame index
                trialText7.tStart = t  # local t and not account for scr refresh
                trialText7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialText7, 'tStartRefresh')  # time at next scr refresh
                trialText7.setAutoDraw(True)
            
            # *trialText8* updates
            if trialText8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialText8.frameNStart = frameN  # exact frame index
                trialText8.tStart = t  # local t and not account for scr refresh
                trialText8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialText8, 'tStartRefresh')  # time at next scr refresh
                trialText8.setAutoDraw(True)
            
            # *trialTextA* updates
            if trialTextA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTextA.frameNStart = frameN  # exact frame index
                trialTextA.tStart = t  # local t and not account for scr refresh
                trialTextA.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTextA, 'tStartRefresh')  # time at next scr refresh
                trialTextA.setAutoDraw(True)
            
            # *trialTextB* updates
            if trialTextB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTextB.frameNStart = frameN  # exact frame index
                trialTextB.tStart = t  # local t and not account for scr refresh
                trialTextB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTextB, 'tStartRefresh')  # time at next scr refresh
                trialTextB.setAutoDraw(True)
            
            # *trialTextC* updates
            if trialTextC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTextC.frameNStart = frameN  # exact frame index
                trialTextC.tStart = t  # local t and not account for scr refresh
                trialTextC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTextC, 'tStartRefresh')  # time at next scr refresh
                trialTextC.setAutoDraw(True)
            
            # *trialTextD* updates
            if trialTextD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTextD.frameNStart = frameN  # exact frame index
                trialTextD.tStart = t  # local t and not account for scr refresh
                trialTextD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTextD, 'tStartRefresh')  # time at next scr refresh
                trialTextD.setAutoDraw(True)
            
            # *trialTextE* updates
            if trialTextE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTextE.frameNStart = frameN  # exact frame index
                trialTextE.tStart = t  # local t and not account for scr refresh
                trialTextE.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTextE, 'tStartRefresh')  # time at next scr refresh
                trialTextE.setAutoDraw(True)
            
            # *trialTextF* updates
            if trialTextF.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTextF.frameNStart = frameN  # exact frame index
                trialTextF.tStart = t  # local t and not account for scr refresh
                trialTextF.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTextF, 'tStartRefresh')  # time at next scr refresh
                trialTextF.setAutoDraw(True)
            
            # *trialTextG* updates
            if trialTextG.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTextG.frameNStart = frameN  # exact frame index
                trialTextG.tStart = t  # local t and not account for scr refresh
                trialTextG.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTextG, 'tStartRefresh')  # time at next scr refresh
                trialTextG.setAutoDraw(True)
            
            # *trialTextH* updates
            if trialTextH.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTextH.frameNStart = frameN  # exact frame index
                trialTextH.tStart = t  # local t and not account for scr refresh
                trialTextH.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTextH, 'tStartRefresh')  # time at next scr refresh
                trialTextH.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('step', steps)  
        # store data for trials (TrialHandler)
        trials.addData('trialMouse.x', trialMouse.x)
        trials.addData('trialMouse.y', trialMouse.y)
        trials.addData('trialMouse.leftButton', trialMouse.leftButton)
        trials.addData('trialMouse.midButton', trialMouse.midButton)
        trials.addData('trialMouse.rightButton', trialMouse.rightButton)
        trials.addData('trialMouse.time', trialMouse.time)
        trials.addData('trialMouse.started', trialMouse.tStartRefresh)
        trials.addData('trialMouse.stopped', trialMouse.tStopRefresh)
        trials.addData('trialCursor.started', trialCursor.tStartRefresh)
        trials.addData('trialCursor.stopped', trialCursor.tStopRefresh)
        trials.addData('trialTarget1.started', trialTarget1.tStartRefresh)
        trials.addData('trialTarget1.stopped', trialTarget1.tStopRefresh)
        trials.addData('trialTarget2.started', trialTarget2.tStartRefresh)
        trials.addData('trialTarget2.stopped', trialTarget2.tStopRefresh)
        trials.addData('trialTarget3.started', trialTarget3.tStartRefresh)
        trials.addData('trialTarget3.stopped', trialTarget3.tStopRefresh)
        trials.addData('trialTarget4.started', trialTarget4.tStartRefresh)
        trials.addData('trialTarget4.stopped', trialTarget4.tStopRefresh)
        trials.addData('trialTarget5.started', trialTarget5.tStartRefresh)
        trials.addData('trialTarget5.stopped', trialTarget5.tStopRefresh)
        trials.addData('trialTarget6.started', trialTarget6.tStartRefresh)
        trials.addData('trialTarget6.stopped', trialTarget6.tStopRefresh)
        trials.addData('trialTarget7.started', trialTarget7.tStartRefresh)
        trials.addData('trialTarget7.stopped', trialTarget7.tStopRefresh)
        trials.addData('trialTarget8.started', trialTarget8.tStartRefresh)
        trials.addData('trialTarget8.stopped', trialTarget8.tStopRefresh)
        trials.addData('trialTargetA.started', trialTargetA.tStartRefresh)
        trials.addData('trialTargetA.stopped', trialTargetA.tStopRefresh)
        trials.addData('trialTargetB.started', trialTargetB.tStartRefresh)
        trials.addData('trialTargetB.stopped', trialTargetB.tStopRefresh)
        trials.addData('trialTargetC.started', trialTargetC.tStartRefresh)
        trials.addData('trialTargetC.stopped', trialTargetC.tStopRefresh)
        trials.addData('trialTargetD.started', trialTargetD.tStartRefresh)
        trials.addData('trialTargetD.stopped', trialTargetD.tStopRefresh)
        trials.addData('trialTargetE.started', trialTargetE.tStartRefresh)
        trials.addData('trialTargetE.stopped', trialTargetE.tStopRefresh)
        trials.addData('trialTargetF.started', trialTargetF.tStartRefresh)
        trials.addData('trialTargetF.stopped', trialTargetF.tStopRefresh)
        trials.addData('trialTargetG.started', trialTargetG.tStartRefresh)
        trials.addData('trialTargetG.stopped', trialTargetG.tStopRefresh)
        trials.addData('trialTargetH.started', trialTargetH.tStartRefresh)
        trials.addData('trialTargetH.stopped', trialTargetH.tStopRefresh)
        trials.addData('trialText1.started', trialText1.tStartRefresh)
        trials.addData('trialText1.stopped', trialText1.tStopRefresh)
        trials.addData('trialText2.started', trialText2.tStartRefresh)
        trials.addData('trialText2.stopped', trialText2.tStopRefresh)
        trials.addData('trialText3.started', trialText3.tStartRefresh)
        trials.addData('trialText3.stopped', trialText3.tStopRefresh)
        trials.addData('trialText4.started', trialText4.tStartRefresh)
        trials.addData('trialText4.stopped', trialText4.tStopRefresh)
        trials.addData('trialText5.started', trialText5.tStartRefresh)
        trials.addData('trialText5.stopped', trialText5.tStopRefresh)
        trials.addData('trialText6.started', trialText6.tStartRefresh)
        trials.addData('trialText6.stopped', trialText6.tStopRefresh)
        trials.addData('trialText7.started', trialText7.tStartRefresh)
        trials.addData('trialText7.stopped', trialText7.tStopRefresh)
        trials.addData('trialText8.started', trialText8.tStartRefresh)
        trials.addData('trialText8.stopped', trialText8.tStopRefresh)
        trials.addData('trialTextA.started', trialTextA.tStartRefresh)
        trials.addData('trialTextA.stopped', trialTextA.tStopRefresh)
        trials.addData('trialTextB.started', trialTextB.tStartRefresh)
        trials.addData('trialTextB.stopped', trialTextB.tStopRefresh)
        trials.addData('trialTextC.started', trialTextC.tStartRefresh)
        trials.addData('trialTextC.stopped', trialTextC.tStopRefresh)
        trials.addData('trialTextD.started', trialTextD.tStartRefresh)
        trials.addData('trialTextD.stopped', trialTextD.tStopRefresh)
        trials.addData('trialTextE.started', trialTextE.tStartRefresh)
        trials.addData('trialTextE.stopped', trialTextE.tStopRefresh)
        trials.addData('trialTextF.started', trialTextF.tStartRefresh)
        trials.addData('trialTextF.stopped', trialTextF.tStopRefresh)
        trials.addData('trialTextG.started', trialTextG.tStartRefresh)
        trials.addData('trialTextG.stopped', trialTextG.tStopRefresh)
        trials.addData('trialTextH.started', trialTextH.tStartRefresh)
        trials.addData('trialTextH.stopped', trialTextH.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 5 repeats of 'tasks'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
