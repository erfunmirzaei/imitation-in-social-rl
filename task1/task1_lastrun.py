#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on August 01, 2021, at 11:32
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'Social Reinforcement Learning'  # from the Builder filename that created this script
expInfo = {'session': '1', 'exp_id': '', 'age': '', 'sex(M or F)': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['exp_id'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\University\\M.Sc\\Term 2\\Principles of Cognitive Science\\Uni\\HWs\\HW1\\task1\\task1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
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

# Initialize components for Routine "Start"
StartClock = core.Clock()
textbox = visual.TextBox2(
     win, text='Hi. Thanks for participating in this experiment. \nIn this experiment, there is 2 kind of trials: Observational, and Private. In Observational trial, an abstract picture of the demonstrator is shown on the left side of the screen and then you can see that the domonstrator\'s action but not reward. In private trials,an abstract picture of You is shown on the right side of the screen and then you should choose between action a or d with pressing the "a" or "d" button on the keyboard after seeing "Go!" signal. Therefore you can see the reward correspond to your action. The goal of experiment is to get more rewards. \nThe more rewards you get, you earn more money(actually I\'ll pay to you after creating my own token. My pleasure :D )  \nIt can take your time for about 10 mins(100 trials) \nWhenever you read the description, you can press the "f" to start the experiment. \n', font='Open Sans',
     pos=(0, 0.35),     letterHeight=0.05,
     size=(1.75,0.3), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='textbox',
     autoLog=True,
)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Private_Observational_trial"
Private_Observational_trialClock = core.Clock()
from random import randint,sample,choice,choices
trial = 0 

#block_types = ["Social", "Private"]
#learning_types = ["PL","SD","UD"]
#trial_types = ["Observational","Private"]
def create_trials(state):
    x = ["Observational","Private"] * 20
    if state == 1:
        block_type = ["Private"] * 20 + ["Social"] * 80
        learning_type = ["PL"] * 20 + ["UD"] * 40 + ["SD"] * 40
        trials_type = ["Private"] * 20 + sample(x, k=len(x)) + sample(x, k=len(x))
    if state == 2:
        block_type = ["Private"] * 20 + ["Social"] * 80
        learning_type = ["PL"] * 20 + ["SD"] * 40 + ["UD"] * 40
        trials_type = ["Private"] * 20 + sample(x, k=len(x)) + sample(x, k=len(x))
    if state == 3:
        block_type = ["Social"] * 40 + ["Private"] * 20 + ["Social"] * 40
        learning_type = ["UD"] * 40 + ["PL"] * 20 + ["SD"] * 40
        trials_type = sample(x, k=len(x)) + ["Private"] * 20 + sample(x, k=len(x))
    if state == 4:
        block_type = ["Social"] * 40 + ["Private"] * 20 + ["Social"] * 40
        learning_type = ["SD"] * 40 + ["PL"] * 20 + ["UD"] * 40
        trials_type = sample(x, k=len(x)) + ["Private"] * 20 + sample(x, k=len(x))
    if state == 5:
        block_type =   ["Social"] * 80 + ["Private"] * 20 
        learning_type = ["UD"] * 40 + ["SD"] * 40 + ["PL"] * 20 
        trials_type = sample(x, k=len(x)) + sample(x, k=len(x)) + ["Private"] * 20 
    if state == 6:
        block_type =   ["Social"] * 80 + ["Private"] * 20 
        learning_type = ["SD"] * 40 + ["UD"] + ["PL"] * 20  
        trials_type = sample(x, k=len(x)) + sample(x, k=len(x)) + ["Private"] * 20 
    return block_type , learning_type, trials_type 
# There is 6 states in each session:
# State 1: P, UD , SD
# State 2: P, SD , UD
# State 3: UD , P, SD
# State 4: SD , P, UD
# State 5: UD, SD , P
# State 6: SD, UD , P
state = randint(1,6)
block_type, learning_type, trials_type = create_trials(state)

actions = ['a', 'd']
rewards = [1,-1] 
p1 = 0.7
p2 = 0.3
p_reward= {'a' : choice([p1,p2])}
p_reward['d'] = 1 - p_reward['a']
probs_a = [p_reward['a'],1 - p_reward['a']]
probs_d = [p_reward['d'],1 - p_reward['d']]
if p_reward['a'] > p_reward['d']:
    best_action = 'a'
    worst_action = 'd'
else :
    best_action = 'd'
    worst_action = 'a'
class MultinomialReward():
    def __init__(self, rewards, probs):
        self.rewards = rewards
        self.probs = probs

    def get_reward(self):
        return choices(self.rewards, weights = self.probs, k = 1)[0]

reward_a = MultinomialReward(rewards,probs_a)
reward_d = MultinomialReward(rewards,probs_d)





person = visual.ImageStim(
    win=win,
    name='person', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text = visual.TextStim(win=win, name='text',
    text='A  or  D',
    font='Arial',
    pos=[0,0], height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='GO!',
    font='Arial',
    pos=[0,0], height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Arial',
    pos=[0,0], height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
line = visual.Line(
    win=win, name='line',
    start=(-(0.7, 0.7)[0]/2.0, 0), end=(+(0.7, 0.7)[0]/2.0, 0),
    ori=90.0, pos=(0, 0),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-6.0, interpolate=True)
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Arial',
    pos=[0,0], height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Arial',
    pos=[0,0], height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
line_2 = visual.Line(
    win=win, name='line_2',
    start=(-(0.7, 0.7)[0]/2.0, 0), end=(+(0.7, 0.7)[0]/2.0, 0),
    ori=90.0, pos=(0, 0),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-3.0, interpolate=True)
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Arial',
    pos=[0,0], height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Start"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
StartComponents = [textbox, key_resp_2]
for thisComponent in StartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Start"-------
while continueRoutine:
    # get current time
    t = StartClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textbox* updates
    if textbox.status == NOT_STARTED and frameN >= 0.0:
        # keep track of start time/frame for later
        textbox.frameNStart = frameN  # exact frame index
        textbox.tStart = t  # local t and not account for scr refresh
        textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
        textbox.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['enter', 'f'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start"-------
for thisComponent in StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textbox.started', textbox.tStartRefresh)
thisExp.addData('textbox.stopped', textbox.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=100.0, method='random', 
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
    
    # ------Prepare to start Routine "Private_Observational_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    trial = trial + 1
    blc_type = block_type[trial-1]
    lrn_type = learning_type[trial-1]
    trial_type = trials_type[trial-1]
    image_paths = ["images/Observational_trial.png","images/Private_trial.png"]
    image_path = "images/" + trial_type + "_trial.png" 
    if trial_type == "Observational":
        x_image = -0.5
        identity = "Demonstrator"
    else : 
        x_image = 0.5
        identity = "You"
        
    action = 'NA'
    if trial_type == "Observational":
        if lrn_type == "SD":
            action = choices([best_action, worst_action], weights = [0.8,0.2], k = 1)[0]
        elif lrn_type == "UD":
            action = choices([best_action, worst_action], weights = [0.2,0.8], k = 1)[0]
    # store in the data:
    thisExp.addData('block_type', blc_type)
    thisExp.addData('learning_type', lrn_type)
    thisExp.addData('trial_type', trial_type)
    thisExp.addData('image_path', image_path)
    thisExp.addData('x_image', x_image)
    thisExp.addData('trial', trial)
    person.setPos((x_image, 0.1))
    person.setImage(image_path)
    text.setPos((x_image, -0.2))
    text_2.setPos((x_image,-0.3))
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    text_4.setPos((x_image, -0.2))
    text_4.setText("action: " + str(action))
    text_5.setPos((x_image, 0.4))
    text_5.setText(identity)
    # keep track of which components have finished
    Private_Observational_trialComponents = [person, text, text_2, key_resp, text_4, line, text_5]
    for thisComponent in Private_Observational_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Private_Observational_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Private_Observational_trial"-------
    while continueRoutine:
        # get current time
        t = Private_Observational_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Private_Observational_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *person* updates
        if person.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            person.frameNStart = frameN  # exact frame index
            person.tStart = t  # local t and not account for scr refresh
            person.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(person, 'tStartRefresh')  # time at next scr refresh
            person.setAutoDraw(True)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 2.25-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 2.75-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            if trial_type != "Observational": key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['a', 'd'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                key_resp.rt = _key_resp_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 3.25-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            if trial_type == "Observational": text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *line* updates
        if line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            line.frameNStart = frameN  # exact frame index
            line.tStart = t  # local t and not account for scr refresh
            line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(line, 'tStartRefresh')  # time at next scr refresh
            line.setAutoDraw(True)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        if trial_type == "Observational" and t > 4.5:
            continueRoutine = False 
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        if trial_type == "Observational": 
            Private_Observational_trial_Components = [person, text, text_2, text_4]
        elif  trial_type == "Private":
            Private_Observational_trial_Components = [person, text, text_2, key_resp]
        for thisComponent in Private_Observational_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Private_Observational_trial"-------
    for thisComponent in Private_Observational_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('person.started', person.tStartRefresh)
    trials.addData('person.stopped', person.tStopRefresh)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    trials.addData('text_2.started', text_2.tStartRefresh)
    trials.addData('text_2.stopped', text_2.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    trials.addData('text_4.started', text_4.tStartRefresh)
    trials.addData('text_4.stopped', text_4.tStopRefresh)
    trials.addData('line.started', line.tStartRefresh)
    trials.addData('line.stopped', line.tStopRefresh)
    trials.addData('text_5.started', text_5.tStartRefresh)
    trials.addData('text_5.stopped', text_5.tStopRefresh)
    # the Routine "Private_Observational_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # store it in the data:
    thisExp.addData('reward_a', p_reward['a'])
    thisExp.addData('reward_d', p_reward['d'])
    if trial_type == "Private":
        if key_resp.keys[0] == 'a':
            reward = str(reward_a.get_reward())
        else:
            reward = str(reward_d.get_reward()) 
    else:
        reward = "?"
    
    thisExp.addData('reward', reward)
    image.setPos((x_image, 0.1))
    text_3.setPos((x_image, -0.2))
    text_3.setText("Rew:" + reward
)
    text_6.setPos((x_image, 0.4))
    text_6.setText(identity)
    # keep track of which components have finished
    feedbackComponents = [image, text_3, line_2, text_6]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        if image.status == STARTED:  # only update if drawing
            image.setImage(image_path)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # *line_2* updates
        if line_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            line_2.frameNStart = frameN  # exact frame index
            line_2.tStart = t  # local t and not account for scr refresh
            line_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(line_2, 'tStartRefresh')  # time at next scr refresh
            line_2.setAutoDraw(True)
        if line_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > line_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                line_2.tStop = t  # not accounting for scr refresh
                line_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(line_2, 'tStopRefresh')  # time at next scr refresh
                line_2.setAutoDraw(False)
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    trials.addData('text_3.started', text_3.tStartRefresh)
    trials.addData('text_3.stopped', text_3.tStopRefresh)
    trials.addData('line_2.started', line_2.tStartRefresh)
    trials.addData('line_2.stopped', line_2.tStopRefresh)
    trials.addData('text_6.started', text_6.tStartRefresh)
    trials.addData('text_6.stopped', text_6.tStopRefresh)
    thisExp.nextEntry()
    
# completed 100.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
