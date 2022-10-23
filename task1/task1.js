/************** 
 * Task1 Test *
 **************/

import { PsychoJS } from './lib/core-2021.1.4.js';
import * as core from './lib/core-2021.1.4.js';
import { TrialHandler } from './lib/data-2021.1.4.js';
import { Scheduler } from './lib/util-2021.1.4.js';
import * as visual from './lib/visual-2021.1.4.js';
import * as sound from './lib/sound-2021.1.4.js';
import * as util from './lib/util-2021.1.4.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'task1';  // from the Builder filename that created this script
let expInfo = {'session': '1', 'exp_id': '', 'age': '', 'sex(M or F)': ''};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(StartRoutineBegin());
flowScheduler.add(StartRoutineEachFrame());
flowScheduler.add(StartRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

function experimentInit() {
  // Initialize components for Routine "Start"
  StartClock = new util.Clock();
  textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox',
    text: 'Hi. Thanks for participating in this experiment. \nIn this experiment, there is 2 kind of trials: Observational, and Private. In Observational trial, an abstract picture of the demonstrator is shown on the left side of the screen and then you can see that the domonstrator\'s action but not reward. In private trials,an abstract picture of You is shown on the right side of the screen and then you should choose between action a or d with pressing the "a" or "d" button on the keyboard after seeing "Go!" signal. Therefore you can see the reward correspond to your action. The goal of experiment is to get more rewards. \nThe more rewards you get, you earn more money(actually I\'ll pay to you after creating my owncrypto token. My pleasure :D )  \nIt can take your time for about 10 mins(100 trials) \nWhenever you read the description, you can press the "f" to start the experiment. \n',
    font: 'Open Sans',
    pos: [0, 0.35], letterHeight: 0.05,
    size: [1.75, 0.3],  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    bold: false, italic: false,
    opacity: undefined,
    padding: undefined,
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Private_Observational_trial"
  Private_Observational_trialClock = new util.Clock();
  import {choice, choices, randint, sample} from 'random';
  var actions, best_action, block_type, learning_type, p1, p2, p_reward, probs_a, probs_d, reward_a, reward_d, rewards, state, trial, trials_type, worst_action;
  trial = 0;
  function create_trials(state) {
      var x;
      x = (["Observational", "Private"] * 20);
      if ((state === 1)) {
          block_type = ((["Private"] * 20) + (["Social"] * 80));
          learning_type = (((["PL"] * 20) + (["UD"] * 40)) + (["SD"] * 40));
          trials_type = (((["Private"] * 20) + sample(x, {"k": x.length})) + sample(x, {"k": x.length}));
      }
      if ((state === 2)) {
          block_type = ((["Private"] * 20) + (["Social"] * 80));
          learning_type = (((["PL"] * 20) + (["SD"] * 40)) + (["UD"] * 40));
          trials_type = (((["Private"] * 20) + sample(x, {"k": x.length})) + sample(x, {"k": x.length}));
      }
      if ((state === 3)) {
          block_type = (((["Social"] * 40) + (["Private"] * 20)) + (["Social"] * 40));
          learning_type = (((["UD"] * 40) + (["PL"] * 20)) + (["SD"] * 40));
          trials_type = ((sample(x, {"k": x.length}) + (["Private"] * 20)) + sample(x, {"k": x.length}));
      }
      if ((state === 4)) {
          block_type = (((["Social"] * 40) + (["Private"] * 20)) + (["Social"] * 40));
          learning_type = (((["SD"] * 40) + (["PL"] * 20)) + (["UD"] * 40));
          trials_type = ((sample(x, {"k": x.length}) + (["Private"] * 20)) + sample(x, {"k": x.length}));
      }
      if ((state === 5)) {
          block_type = ((["Social"] * 80) + (["Private"] * 20));
          learning_type = (((["UD"] * 40) + (["SD"] * 40)) + (["PL"] * 20));
          trials_type = ((sample(x, {"k": x.length}) + sample(x, {"k": x.length})) + (["Private"] * 20));
      }
      if ((state === 6)) {
          block_type = ((["Social"] * 80) + (["Private"] * 20));
          learning_type = (((["SD"] * 40) + ["UD"]) + (["PL"] * 20));
          trials_type = ((sample(x, {"k": x.length}) + sample(x, {"k": x.length})) + (["Private"] * 20));
      }
      return [block_type, learning_type, trials_type];
  }
  state = randint(1, 6);
  [block_type, learning_type, trials_type] = create_trials(state);
  actions = ["a", "d"];
  rewards = [1, (- 1)];
  p1 = 0.7;
  p2 = 0.3;
  p_reward = {"a": choice([p1, p2])};
  p_reward["d"] = (1 - p_reward["a"]);
  probs_a = [p_reward["a"], (1 - p_reward["a"])];
  probs_d = [p_reward["d"], (1 - p_reward["d"])];
  if ((p_reward["a"] > p_reward["d"])) {
      best_action = "a";
      worst_action = "d";
  } else {
      best_action = "d";
      worst_action = "a";
  }
  class MultinomialReward {
      constructor(rewards, probs) {
          this.rewards = rewards;
          this.probs = probs;
      }
      get_reward() {
          return choices(this.rewards, {"weights": this.probs, "k": 1})[0];
      }
  }
  reward_a = new MultinomialReward(rewards, probs_a);
  reward_d = new MultinomialReward(rewards, probs_d);
  
  person = new visual.ImageStim({
    win : psychoJS.window,
    name : 'person', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'A  or  D',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'GO!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  line = new visual.ShapeStim ({
    win: psychoJS.window, name: 'line', 
    vertices: [[-[0.7, 0.7][0]/2.0, 0], [+[0.7, 0.7][0]/2.0, 0]],
    ori: 90.0, pos: [0, 0],
    lineWidth: 2.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -7.0 
  });
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  line_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'line_2', 
    vertices: [[-[0.7, 0.7][0]/2.0, 0], [+[0.7, 0.7][0]/2.0, 0]],
    ori: 90.0, pos: [0, 0],
    lineWidth: 2.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.075,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function StartRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Start'-------
    t = 0;
    StartClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    StartComponents = [];
    StartComponents.push(textbox);
    StartComponents.push(key_resp_2);
    
    for (const thisComponent of StartComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function StartRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Start'-------
    // get current time
    t = StartClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textbox* updates
    if (frameN >= 0.0 && textbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox.tStart = t;  // (not accounting for frame time here)
      textbox.frameNStart = frameN;  // exact frame index
      
      textbox.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['enter', 'f'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of StartComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function StartRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Start'-------
    for (const thisComponent of StartComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "Start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 100, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    const snapshot = trials.getSnapshot();
    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(Private_Observational_trialRoutineBegin(snapshot));
    trialsLoopScheduler.add(Private_Observational_trialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(Private_Observational_trialRoutineEnd(snapshot));
    trialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
    trialsLoopScheduler.add(feedbackRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(feedbackRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

function Private_Observational_trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Private_Observational_trial'-------
    t = 0;
    Private_Observational_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    trial = (trial + 1);
    blc_type = block_type[(trial - 1)];
    lrn_type = learning_type[(trial - 1)];
    trial_type = trials_type[(trial - 1)];
    image_paths = ["images/Observational_trial.png", "images/Private_trial.png"];
    image_path = (("images/" + trial_type) + "_trial.png");
    if ((trial_type === "Observational")) {
        x_image = (- 0.5);
        identity = "Demonstrator";
    } else {
        x_image = 0.5;
        identity = "You";
    }
    action = "NA";
    if ((trial_type === "Observational")) {
        if ((lrn_type === "SD")) {
            action = choices([best_action, worst_action], {"weights": [0.8, 0.2], "k": 1})[0];
        } else {
            if ((lrn_type === "UD")) {
                action = choices([best_action, worst_action], {"weights": [0.2, 0.8], "k": 1})[0];
            }
        }
    }
    thisExp.addData("block_type", blc_type);
    thisExp.addData("learning_type", lrn_type);
    thisExp.addData("trial_type", trial_type);
    thisExp.addData("image_path", image_path);
    thisExp.addData("x_image", x_image);
    thisExp.addData("trial", trial);
    
    person.setPos([x_image, 0.1]);
    person.setImage(image_path);
    text.setPos([x_image, (- 0.2)]);
    text_2.setPos([x_image, (- 0.3)]);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    text_4.setPos([x_image, (- 0.2)]);
    text_4.setText(("action: " + action.toString()));
    text_5.setPos([x_image, 0.4]);
    text_5.setText(identity);
    // keep track of which components have finished
    Private_Observational_trialComponents = [];
    Private_Observational_trialComponents.push(person);
    Private_Observational_trialComponents.push(text);
    Private_Observational_trialComponents.push(text_2);
    Private_Observational_trialComponents.push(key_resp);
    Private_Observational_trialComponents.push(text_4);
    Private_Observational_trialComponents.push(line);
    Private_Observational_trialComponents.push(text_5);

    
    
    for (const thisComponent of Private_Observational_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function Private_Observational_trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Private_Observational_trial'-------
    // get current time
    t = Private_Observational_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *person* updates
    if (t >= 0.5 && person.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      person.tStart = t;  // (not accounting for frame time here)
      person.frameNStart = frameN;  // exact frame index
      
      person.setAutoDraw(true);
    }

    
    // *text* updates
    if (t >= 1.5 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 1.5 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    
    // *text_2* updates
    if (t >= 2.25 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    frameRemains = 2.25 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_2.setAutoDraw(false);
    }
    
    // *key_resp* updates
    if (t >= 2.75 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['a', 'd'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[0].name;  // just the first key pressed
        key_resp.rt = _key_resp_allKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_4* updates
    if (t >= 3.25 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    frameRemains = 3.25 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_4.setAutoDraw(false);
    }
    
    // *line* updates
    if (t >= 0.0 && line.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      line.tStart = t;  // (not accounting for frame time here)
      line.frameNStart = frameN;  // exact frame index
      
      line.setAutoDraw(true);
    }

    
    // *text_5* updates
    if (t >= 0.5 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Private_Observational_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Private_Observational_trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Private_Observational_trial'-------
    for (const thisComponent of Private_Observational_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "Private_Observational_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function feedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'feedback'-------
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    thisExp.addData("reward_a", p_reward["a"]);
    thisExp.addData("reward_d", p_reward["d"]);
    if ((trial_type === "Private")) {
        if ((key_resp.keys[0] === "a")) {
            reward = reward_a.get_reward().toString();
        } else {
            reward = reward_d.get_reward().toString();
        }
    } else {
        reward = "?";
    }
    thisExp.addData("reward", reward);
    
    image.setPos([x_image, 0.1]);
    text_3.setPos([x_image, (- 0.2)]);
    text_3.setText(("Rew:" + reward));
    text_6.setPos([x_image, 0.4]);
    text_6.setText(identity);
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(image);
    feedbackComponents.push(text_3);
    feedbackComponents.push(line_2);
    feedbackComponents.push(text_6);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function feedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'feedback'-------
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image.setAutoDraw(false);
    }
    
    if (image.status === PsychoJS.Status.STARTED){ // only update if being drawn
      image.setImage(image_path, false);
    }
    
    // *text_3* updates
    if (t >= 0.5 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    frameRemains = 0.5 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_3.setAutoDraw(false);
    }
    
    // *line_2* updates
    if (t >= 0.0 && line_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      line_2.tStart = t;  // (not accounting for frame time here)
      line_2.frameNStart = frameN;  // exact frame index
      
      line_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (line_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      line_2.setAutoDraw(false);
    }
    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_6.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function feedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'feedback'-------
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}

function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
