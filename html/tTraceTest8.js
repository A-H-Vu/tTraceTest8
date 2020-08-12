/******************** 
 * Ttracetest8 Test *
 ********************/

import { PsychoJS } from './lib/core-2020.1.js';
import * as core from './lib/core-2020.1.js';
import { TrialHandler } from './lib/data-2020.1.js';
import { Scheduler } from './lib/util-2020.1.js';
import * as util from './lib/util-2020.1.js';
import * as visual from './lib/visual-2020.1.js';
import * as sound from './lib/sound-2020.1.js';

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
let expName = 'tTraceTest8';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

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
flowScheduler.add(setupRoutineBegin());
flowScheduler.add(setupRoutineEachFrame());
flowScheduler.add(setupRoutineEnd());
const tasksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(tasksLoopBegin, tasksLoopScheduler);
flowScheduler.add(tasksLoopScheduler);
flowScheduler.add(tasksLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.3';
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


var setupClock;
var thisExp;
var win;
var event;
var shuffle;
var pi;
var sin;
var cos;
var sqrt;
var randint;
var posArray1;
var posArray2;
var instrClock;
var instrText;
var instrResp;
var trialClock;
var drawLine;
var trialMouse;
var trialCursor;
var trialTarget1;
var trialTarget2;
var trialTarget3;
var trialTarget4;
var trialTarget5;
var trialTarget6;
var trialTarget7;
var trialTarget8;
var trialTargetA;
var trialTargetB;
var trialTargetC;
var trialTargetD;
var trialTargetE;
var trialTargetF;
var trialTargetG;
var trialTargetH;
var trialText1;
var trialText2;
var trialText3;
var trialText4;
var trialText5;
var trialText6;
var trialText7;
var trialText8;
var trialTextA;
var trialTextB;
var trialTextC;
var trialTextD;
var trialTextE;
var trialTextF;
var trialTextG;
var trialTextH;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "setup"
  setupClock = new util.Clock();
  // Code to fix reference errors in JS
  thisExp = psychoJS.experiment;
  win = psychoJS.window;
  event = psychoJS.eventManager;
  Array.prototype.append = [].push;
  shuffle = util.shuffle;
  document.documentElement.style.cursor = 'none';
  // Math related fixes
  pi = Math.PI;
  sin = Math.sin;
  cos = Math.cos;
  sqrt = Math.sqrt;
  randint = function(min, maxplusone) {
    return Math.floor(Math.random() * (maxplusone - min) ) + min;
  }
  shuffle = util.shuffle;
  posArray1 = [(- 0.05), (- 0.1), (- 0.15), (- 0.2), (- 0.25), (- 0.3), (- 0.35), (- 0.4), 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4];
  posArray2 = [(- 0.05), (- 0.1), (- 0.15), (- 0.2), (- 0.25), (- 0.3), (- 0.35), (- 0.4), 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4];
  
  // Initialize components for Routine "instr"
  instrClock = new util.Clock();
  shuffle(posArray1);
  shuffle(posArray2);
  
  instrText = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrText',
    text: 'The order is 1, A, 2, B, 3, C, 4, D, 5, E, 6, F, 7, G, 8, H. Press space to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  instrResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  drawLine = function (shapeList) {
      var lines, pos1, pos2;
      lines = [];
      if ((! (shapeList.length % 2))) {
          while (shapeList.length) {
              pos1 = shapeList.pop();
              pos2 = shapeList.pop();
              var newLine = new visual.ShapeStim({ 
                  win: win,
                  vertices: [ pos1.pos, pos2.pos ],
              });
              lines.append(newLine);
          }
      }
      if (lines.length) {
          for (var line, _pj_c = 0, _pj_a = lines, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
              line = _pj_a[_pj_c];
              line.setAutoDraw(true);
          }
      }
  }
  trialMouse = new core.Mouse({
    win: psychoJS.window,
  });
  trialMouse.mouseClock = new util.Clock();
  trialCursor = new visual.Polygon ({
    win: psychoJS.window, name: 'trialCursor', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  trialTarget1 = new visual.Polygon ({
    win: psychoJS.window, name: 'trialTarget1', 
    edges: 180, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1.0, depth: -3, interpolate: true,
  });
  
  trialTarget2 = new visual.Polygon ({
    win: psychoJS.window, name: 'trialTarget2', 
    edges: 180, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1.0, depth: -4, interpolate: true,
  });
  
  trialTarget3 = new visual.Polygon ({
    win: psychoJS.window, name: 'trialTarget3', 
    edges: 180, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1.0, depth: -5, interpolate: true,
  });
  
  trialTarget4 = new visual.Polygon ({
    win: psychoJS.window, name: 'trialTarget4', 
    edges: 180, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1.0, depth: -6, interpolate: true,
  });
  
  trialTarget5 = new visual.Polygon ({
    win: psychoJS.window, name: 'trialTarget5', 
    edges: 180, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1.0, depth: -7, interpolate: true,
  });
  
  trialTarget6 = new visual.Polygon ({
    win: psychoJS.window, name: 'trialTarget6', 
    edges: 180, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1.0, depth: -8, interpolate: true,
  });
  
  trialTarget7 = new visual.Polygon ({
    win: psychoJS.window, name: 'trialTarget7', 
    edges: 180, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1.0, depth: -9, interpolate: true,
  });
  
  trialTarget8 = new visual.Polygon ({
    win: psychoJS.window, name: 'trialTarget8', 
    edges: 180, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1.0, depth: -10, interpolate: true,
  });
  
  trialTargetA = new visual.Polygon ({
    win: psychoJS.window, name: 'trialTargetA', 
    edges: 180, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1.0, depth: -11, interpolate: true,
  });
  
  trialTargetB = new visual.Polygon ({
    win: psychoJS.window, name: 'trialTargetB', 
    edges: 180, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1.0, depth: -12, interpolate: true,
  });
  
  trialTargetC = new visual.Polygon ({
    win: psychoJS.window, name: 'trialTargetC', 
    edges: 180, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1.0, depth: -13, interpolate: true,
  });
  
  trialTargetD = new visual.Polygon ({
    win: psychoJS.window, name: 'trialTargetD', 
    edges: 180, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1.0, depth: -14, interpolate: true,
  });
  
  trialTargetE = new visual.Polygon ({
    win: psychoJS.window, name: 'trialTargetE', 
    edges: 180, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1.0, depth: -15, interpolate: true,
  });
  
  trialTargetF = new visual.Polygon ({
    win: psychoJS.window, name: 'trialTargetF', 
    edges: 180, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1.0, depth: -16, interpolate: true,
  });
  
  trialTargetG = new visual.Polygon ({
    win: psychoJS.window, name: 'trialTargetG', 
    edges: 180, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1.0, depth: -17, interpolate: true,
  });
  
  trialTargetH = new visual.Polygon ({
    win: psychoJS.window, name: 'trialTargetH', 
    edges: 180, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1.0, depth: -18, interpolate: true,
  });
  
  trialText1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialText1',
    text: '1',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -20.0 
  });
  
  trialText2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialText2',
    text: '2',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -21.0 
  });
  
  trialText3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialText3',
    text: '3',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -22.0 
  });
  
  trialText4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialText4',
    text: '4',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -23.0 
  });
  
  trialText5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialText5',
    text: '5',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -24.0 
  });
  
  trialText6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialText6',
    text: '6',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -25.0 
  });
  
  trialText7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialText7',
    text: '7',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -26.0 
  });
  
  trialText8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialText8',
    text: '8',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -27.0 
  });
  
  trialTextA = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialTextA',
    text: 'A',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -28.0 
  });
  
  trialTextB = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialTextB',
    text: 'B',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -29.0 
  });
  
  trialTextC = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialTextC',
    text: 'C',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -30.0 
  });
  
  trialTextD = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialTextD',
    text: 'D',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -31.0 
  });
  
  trialTextE = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialTextE',
    text: 'E',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -32.0 
  });
  
  trialTextF = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialTextF',
    text: 'F',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -33.0 
  });
  
  trialTextG = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialTextG',
    text: 'G',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -34.0 
  });
  
  trialTextH = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialTextH',
    text: 'H',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -35.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var setupComponents;
function setupRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'setup'-------
    t = 0;
    setupClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    setupComponents = [];
    
    for (const thisComponent of setupComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function setupRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'setup'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = setupClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of setupComponents)
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


function setupRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'setup'-------
    for (const thisComponent of setupComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var tasks;
var currentLoop;
function tasksLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  tasks = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 5, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'tasks'
  });
  psychoJS.experiment.addLoop(tasks); // add the loop to the experiment
  currentLoop = tasks;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTask of tasks) {
    const snapshot = tasks.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(instrRoutineBegin(snapshot));
    thisScheduler.add(instrRoutineEachFrame(snapshot));
    thisScheduler.add(instrRoutineEnd(snapshot));
    const trialsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(trialsLoopBegin, trialsLoopScheduler);
    thisScheduler.add(trialsLoopScheduler);
    thisScheduler.add(trialsLoopEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    const snapshot = trials.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trialRoutineBegin(snapshot));
    thisScheduler.add(trialRoutineEachFrame(snapshot));
    thisScheduler.add(trialRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


function tasksLoopEnd() {
  psychoJS.experiment.removeLoop(tasks);

  return Scheduler.Event.NEXT;
}


var pos1;
var pos2;
var pos3;
var pos4;
var pos5;
var pos6;
var pos7;
var pos8;
var pos9;
var pos10;
var pos11;
var pos12;
var pos13;
var pos14;
var pos15;
var pos16;
var pos17;
var pos18;
var pos19;
var pos20;
var pos21;
var pos22;
var pos23;
var pos24;
var pos25;
var pos26;
var pos27;
var pos28;
var pos29;
var pos30;
var pos31;
var pos32;
var _instrResp_allKeys;
var instrComponents;
function instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr'-------
    t = 0;
    instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    shuffle(posArray1);
    shuffle(posArray2);
    pos1 = posArray1[0];
    pos2 = posArray2[0];
    pos3 = posArray1[1];
    pos4 = posArray2[1];
    pos5 = posArray1[2];
    pos6 = posArray2[2];
    pos7 = posArray1[3];
    pos8 = posArray2[3];
    pos9 = posArray1[4];
    pos10 = posArray2[4];
    pos11 = posArray1[5];
    pos12 = posArray2[5];
    pos13 = posArray1[6];
    pos14 = posArray2[6];
    pos15 = posArray1[7];
    pos16 = posArray2[7];
    pos17 = posArray1[8];
    pos18 = posArray2[8];
    pos19 = posArray1[9];
    pos20 = posArray2[9];
    pos21 = posArray1[10];
    pos22 = posArray2[10];
    pos23 = posArray1[11];
    pos24 = posArray2[11];
    pos25 = posArray1[12];
    pos26 = posArray2[12];
    pos27 = posArray1[13];
    pos28 = posArray2[13];
    pos29 = posArray1[14];
    pos30 = posArray2[14];
    pos31 = posArray1[15];
    pos32 = posArray2[15];
    
    instrResp.keys = undefined;
    instrResp.rt = undefined;
    _instrResp_allKeys = [];
    // keep track of which components have finished
    instrComponents = [];
    instrComponents.push(instrText);
    instrComponents.push(instrResp);
    
    for (const thisComponent of instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instrText* updates
    if (t >= 0.0 && instrText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrText.tStart = t;  // (not accounting for frame time here)
      instrText.frameNStart = frameN;  // exact frame index
      
      instrText.setAutoDraw(true);
    }

    
    // *instrResp* updates
    if (t >= 0.0 && instrResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrResp.tStart = t;  // (not accounting for frame time here)
      instrResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instrResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instrResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instrResp.clearEvents(); });
    }

    if (instrResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instrResp.getKeys({keyList: ['space'], waitRelease: false});
      _instrResp_allKeys = _instrResp_allKeys.concat(theseKeys);
      if (_instrResp_allKeys.length > 0) {
        instrResp.keys = _instrResp_allKeys[_instrResp_allKeys.length - 1].name;  // just the last key pressed
        instrResp.rt = _instrResp_allKeys[_instrResp_allKeys.length - 1].rt;
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
    for (const thisComponent of instrComponents)
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


function instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr'-------
    for (const thisComponent of instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var targetOpac1;
var targetOpac2;
var targetOpac3;
var targetOpac4;
var targetOpac5;
var targetOpac6;
var targetOpac7;
var targetOpac8;
var targetOpacA;
var targetOpacB;
var targetOpacC;
var targetOpacD;
var targetOpacE;
var targetOpacF;
var targetOpacG;
var targetOpacH;
var trialStep;
var steps;
var shapeList;
var gotValidClick;
var trialComponents;
function trialRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    trialCursor.pos = [1.5, 1.5];
    trialMouse.pos = [1.5, 1.5];
    targetOpac1 = 0.25;
    targetOpac2 = 0.25;
    targetOpac3 = 0.25;
    targetOpac4 = 0.25;
    targetOpac5 = 0.25;
    targetOpac6 = 0.25;
    targetOpac7 = 0.25;
    targetOpac8 = 0.25;
    targetOpacA = 0.25;
    targetOpacB = 0.25;
    targetOpacC = 0.25;
    targetOpacD = 0.25;
    targetOpacE = 0.25;
    targetOpacF = 0.25;
    targetOpacG = 0.25;
    targetOpacH = 0.25;
    trialStep = 1;
    steps = [];
    shapeList = [];
    
    // setup some python lists for storing info about the trialMouse
    // current position of the mouse:
    trialMouse.x = [];
    trialMouse.y = [];
    trialMouse.leftButton = [];
    trialMouse.midButton = [];
    trialMouse.rightButton = [];
    trialMouse.time = [];
    gotValidClick = false; // until a click is received
    trialMouse.mouseClock.reset();
    trialTarget1.setPos([pos1, pos2]);
    trialTarget2.setPos([pos5, pos6]);
    trialTarget3.setPos([pos9, pos10]);
    trialTarget4.setPos([pos13, pos14]);
    trialTarget5.setPos([pos15, pos16]);
    trialTarget6.setPos([pos17, pos18]);
    trialTarget7.setPos([pos19, pos20]);
    trialTarget8.setPos([pos21, pos22]);
    trialTargetA.setPos([pos3, pos4]);
    trialTargetB.setPos([pos7, pos8]);
    trialTargetC.setPos([pos11, pos12]);
    trialTargetD.setPos([pos23, pos24]);
    trialTargetE.setPos([pos25, pos26]);
    trialTargetF.setPos([pos27, pos28]);
    trialTargetG.setPos([pos29, pos30]);
    trialTargetH.setPos([pos31, pos32]);
    trialText1.setPos([pos1, pos2]);
    trialText2.setPos([pos5, pos6]);
    trialText3.setPos([pos9, pos10]);
    trialText4.setPos([pos13, pos14]);
    trialText5.setPos([pos15, pos16]);
    trialText6.setPos([pos17, pos18]);
    trialText7.setPos([pos19, pos20]);
    trialText8.setPos([pos21, pos22]);
    trialTextA.setPos([pos3, pos4]);
    trialTextB.setPos([pos7, pos8]);
    trialTextC.setPos([pos11, pos12]);
    trialTextD.setPos([pos23, pos24]);
    trialTextE.setPos([pos25, pos26]);
    trialTextF.setPos([pos27, pos28]);
    trialTextG.setPos([pos29, pos30]);
    trialTextH.setPos([pos31, pos32]);
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(trialMouse);
    trialComponents.push(trialCursor);
    trialComponents.push(trialTarget1);
    trialComponents.push(trialTarget2);
    trialComponents.push(trialTarget3);
    trialComponents.push(trialTarget4);
    trialComponents.push(trialTarget5);
    trialComponents.push(trialTarget6);
    trialComponents.push(trialTarget7);
    trialComponents.push(trialTarget8);
    trialComponents.push(trialTargetA);
    trialComponents.push(trialTargetB);
    trialComponents.push(trialTargetC);
    trialComponents.push(trialTargetD);
    trialComponents.push(trialTargetE);
    trialComponents.push(trialTargetF);
    trialComponents.push(trialTargetG);
    trialComponents.push(trialTargetH);
    trialComponents.push(trialText1);
    trialComponents.push(trialText2);
    trialComponents.push(trialText3);
    trialComponents.push(trialText4);
    trialComponents.push(trialText5);
    trialComponents.push(trialText6);
    trialComponents.push(trialText7);
    trialComponents.push(trialText8);
    trialComponents.push(trialTextA);
    trialComponents.push(trialTextB);
    trialComponents.push(trialTextC);
    trialComponents.push(trialTextD);
    trialComponents.push(trialTextE);
    trialComponents.push(trialTextF);
    trialComponents.push(trialTextG);
    trialComponents.push(trialTextH);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var CursorTargetDistance;
var prevButtonState;
function trialRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    steps.append(trialStep);
    if ((trialStep === 1)) {
        CursorTargetDistance = Math.sqrt((Math.pow((trialCursor.pos[0] - trialTarget1.pos[0]), 2) + Math.pow((trialCursor.pos[1] - trialTarget1.pos[1]), 2)));
        if ((CursorTargetDistance < 0.05)) {
            targetOpac1 = 0;
            trialStep = 2;
            shapeList.append(trialTarget1);
        }
    }
    if ((trialStep === 2)) {
        CursorTargetDistance = Math.sqrt((Math.pow((trialCursor.pos[0] - trialTargetA.pos[0]), 2) + Math.pow((trialCursor.pos[1] - trialTargetA.pos[1]), 2)));
        if ((CursorTargetDistance < 0.05)) {
            targetOpacA = 0;
            trialStep = 3;
            shapeList.append(trialTargetA);
        }
    }
    if ((trialStep === 3)) {
        CursorTargetDistance = Math.sqrt((Math.pow((trialCursor.pos[0] - trialTarget2.pos[0]), 2) + Math.pow((trialCursor.pos[1] - trialTarget2.pos[1]), 2)));
        if ((CursorTargetDistance < 0.05)) {
            targetOpac2 = 0;
            trialStep = 4;
            shapeList.append(trialTargetA);
            shapeList.append(trialTarget2);
        }
    }
    if ((trialStep === 4)) {
        CursorTargetDistance = Math.sqrt((Math.pow((trialCursor.pos[0] - trialTargetB.pos[0]), 2) + Math.pow((trialCursor.pos[1] - trialTargetB.pos[1]), 2)));
        if ((CursorTargetDistance < 0.05)) {
            targetOpacB = 0;
            trialStep = 5;
            shapeList.append(trialTarget2);
            shapeList.append(trialTargetB);
        }
    }
    if ((trialStep === 5)) {
        CursorTargetDistance = Math.sqrt((Math.pow((trialCursor.pos[0] - trialTarget3.pos[0]), 2) + Math.pow((trialCursor.pos[1] - trialTarget3.pos[1]), 2)));
        if ((CursorTargetDistance < 0.05)) {
            targetOpac3 = 0;
            trialStep = 6;
            shapeList.append(trialTargetB);
            shapeList.append(trialTarget3);
        }
    }
    if ((trialStep === 6)) {
        CursorTargetDistance = Math.sqrt((Math.pow((trialCursor.pos[0] - trialTargetC.pos[0]), 2) + Math.pow((trialCursor.pos[1] - trialTargetC.pos[1]), 2)));
        if ((CursorTargetDistance < 0.05)) {
            targetOpacC = 0;
            trialStep = 7;
            shapeList.append(trialTarget3);
            shapeList.append(trialTargetC);
        }
    }
    if ((trialStep === 7)) {
        CursorTargetDistance = Math.sqrt((Math.pow((trialCursor.pos[0] - trialTarget4.pos[0]), 2) + Math.pow((trialCursor.pos[1] - trialTarget4.pos[1]), 2)));
        if ((CursorTargetDistance < 0.05)) {
            targetOpac4 = 0;
            trialStep = 8;
            shapeList.append(trialTargetC);
            shapeList.append(trialTarget4);
        }
    }
    if ((trialStep === 8)) {
        CursorTargetDistance = Math.sqrt((Math.pow((trialCursor.pos[0] - trialTargetD.pos[0]), 2) + Math.pow((trialCursor.pos[1] - trialTargetD.pos[1]), 2)));
        if ((CursorTargetDistance < 0.05)) {
            targetOpacD = 0;
            trialStep = 9;
            shapeList.append(trialTarget4);
            shapeList.append(trialTargetD);
        }
    }
    if ((trialStep === 9)) {
        CursorTargetDistance = Math.sqrt((Math.pow((trialCursor.pos[0] - trialTarget5.pos[0]), 2) + Math.pow((trialCursor.pos[1] - trialTarget5.pos[1]), 2)));
        if ((CursorTargetDistance < 0.05)) {
            targetOpac5 = 0;
            trialStep = 10;
            shapeList.append(trialTargetD);
            shapeList.append(trialTarget5);
        }
    }
    if ((trialStep === 10)) {
        CursorTargetDistance = Math.sqrt((Math.pow((trialCursor.pos[0] - trialTargetE.pos[0]), 2) + Math.pow((trialCursor.pos[1] - trialTargetE.pos[1]), 2)));
        if ((CursorTargetDistance < 0.05)) {
            targetOpacE = 0;
            trialStep = 11;
            shapeList.append(trialTarget5);
            shapeList.append(trialTargetE);
        }
    }
    if ((trialStep === 11)) {
        CursorTargetDistance = Math.sqrt((Math.pow((trialCursor.pos[0] - trialTarget6.pos[0]), 2) + Math.pow((trialCursor.pos[1] - trialTarget6.pos[1]), 2)));
        if ((CursorTargetDistance < 0.05)) {
            targetOpac6 = 0;
            trialStep = 12;
            shapeList.append(trialTargetE);
            shapeList.append(trialTarget6);
        }
    }
    if ((trialStep === 12)) {
        CursorTargetDistance = Math.sqrt((Math.pow((trialCursor.pos[0] - trialTargetF.pos[0]), 2) + Math.pow((trialCursor.pos[1] - trialTargetF.pos[1]), 2)));
        if ((CursorTargetDistance < 0.05)) {
            targetOpacF = 0;
            trialStep = 13;
            shapeList.append(trialTarget6);
            shapeList.append(trialTargetF);
        }
    }
    if ((trialStep === 13)) {
        CursorTargetDistance = Math.sqrt((Math.pow((trialCursor.pos[0] - trialTarget7.pos[0]), 2) + Math.pow((trialCursor.pos[1] - trialTarget7.pos[1]), 2)));
        if ((CursorTargetDistance < 0.05)) {
            targetOpac7 = 0;
            trialStep = 14;
            shapeList.append(trialTargetF);
            shapeList.append(trialTarget7);
        }
    }
    if ((trialStep === 14)) {
        CursorTargetDistance = Math.sqrt((Math.pow((trialCursor.pos[0] - trialTargetG.pos[0]), 2) + Math.pow((trialCursor.pos[1] - trialTargetG.pos[1]), 2)));
        if ((CursorTargetDistance < 0.05)) {
            targetOpacG = 0;
            trialStep = 15;
            shapeList.append(trialTarget7);
            shapeList.append(trialTargetG);
        }
    }
    if ((trialStep === 15)) {
        CursorTargetDistance = Math.sqrt((Math.pow((trialCursor.pos[0] - trialTarget8.pos[0]), 2) + Math.pow((trialCursor.pos[1] - trialTarget8.pos[1]), 2)));
        if ((CursorTargetDistance < 0.05)) {
            targetOpac8 = 0;
            trialStep = 16;
            shapeList.append(trialTargetG);
            shapeList.append(trialTarget8);
        }
    }
    if ((trialStep === 16)) {
        CursorTargetDistance = Math.sqrt((Math.pow((trialCursor.pos[0] - trialTargetH.pos[0]), 2) + Math.pow((trialCursor.pos[1] - trialTargetH.pos[1]), 2)));
        if ((CursorTargetDistance < 0.05)) {
            targetOpacH = 0;
            shapeList.append(trialTarget8);
            shapeList.append(trialTargetH);
            continueRoutine = false;
        }
    }
    drawLine(shapeList);
    
    // *trialMouse* updates
    if (t >= 0.0 && trialMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialMouse.tStart = t;  // (not accounting for frame time here)
      trialMouse.frameNStart = frameN;  // exact frame index
      
      trialMouse.status = PsychoJS.Status.STARTED;
      prevButtonState = [0, 0, 0];  // if now button is down we will treat as 'new' click
      }
    if (trialMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = trialMouse.getPressed();
      const xys = trialMouse.getPos();
      trialMouse.x.push(xys[0]);
      trialMouse.y.push(xys[1]);
      trialMouse.leftButton.push(buttons[0]);
      trialMouse.midButton.push(buttons[1]);
      trialMouse.rightButton.push(buttons[2]);
      trialMouse.time.push(trialMouse.mouseClock.getTime());
    }
    
    // *trialCursor* updates
    if (t >= 0.0 && trialCursor.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialCursor.tStart = t;  // (not accounting for frame time here)
      trialCursor.frameNStart = frameN;  // exact frame index
      
      trialCursor.setAutoDraw(true);
    }

    
    if (trialCursor.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialCursor.setPos([trialMouse.getPos()[0], trialMouse.getPos()[1]]);
    }
    
    // *trialTarget1* updates
    if (t >= 0.0 && trialTarget1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTarget1.tStart = t;  // (not accounting for frame time here)
      trialTarget1.frameNStart = frameN;  // exact frame index
      
      trialTarget1.setAutoDraw(true);
    }

    
    if (trialTarget1.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialTarget1.setOpacity(targetOpac1);
    }
    
    // *trialTarget2* updates
    if (t >= 0.0 && trialTarget2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTarget2.tStart = t;  // (not accounting for frame time here)
      trialTarget2.frameNStart = frameN;  // exact frame index
      
      trialTarget2.setAutoDraw(true);
    }

    
    if (trialTarget2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialTarget2.setOpacity(targetOpac2);
    }
    
    // *trialTarget3* updates
    if (t >= 0.0 && trialTarget3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTarget3.tStart = t;  // (not accounting for frame time here)
      trialTarget3.frameNStart = frameN;  // exact frame index
      
      trialTarget3.setAutoDraw(true);
    }

    
    if (trialTarget3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialTarget3.setOpacity(targetOpac3);
    }
    
    // *trialTarget4* updates
    if (t >= 0.0 && trialTarget4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTarget4.tStart = t;  // (not accounting for frame time here)
      trialTarget4.frameNStart = frameN;  // exact frame index
      
      trialTarget4.setAutoDraw(true);
    }

    
    if (trialTarget4.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialTarget4.setOpacity(targetOpac4);
    }
    
    // *trialTarget5* updates
    if (t >= 0.0 && trialTarget5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTarget5.tStart = t;  // (not accounting for frame time here)
      trialTarget5.frameNStart = frameN;  // exact frame index
      
      trialTarget5.setAutoDraw(true);
    }

    
    if (trialTarget5.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialTarget5.setOpacity(targetOpac5);
    }
    
    // *trialTarget6* updates
    if (t >= 0.0 && trialTarget6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTarget6.tStart = t;  // (not accounting for frame time here)
      trialTarget6.frameNStart = frameN;  // exact frame index
      
      trialTarget6.setAutoDraw(true);
    }

    
    if (trialTarget6.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialTarget6.setOpacity(targetOpac6);
    }
    
    // *trialTarget7* updates
    if (t >= 0.0 && trialTarget7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTarget7.tStart = t;  // (not accounting for frame time here)
      trialTarget7.frameNStart = frameN;  // exact frame index
      
      trialTarget7.setAutoDraw(true);
    }

    
    if (trialTarget7.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialTarget7.setOpacity(targetOpac7);
    }
    
    // *trialTarget8* updates
    if (t >= 0.0 && trialTarget8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTarget8.tStart = t;  // (not accounting for frame time here)
      trialTarget8.frameNStart = frameN;  // exact frame index
      
      trialTarget8.setAutoDraw(true);
    }

    
    if (trialTarget8.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialTarget8.setOpacity(targetOpac8);
    }
    
    // *trialTargetA* updates
    if (t >= 0.0 && trialTargetA.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTargetA.tStart = t;  // (not accounting for frame time here)
      trialTargetA.frameNStart = frameN;  // exact frame index
      
      trialTargetA.setAutoDraw(true);
    }

    
    if (trialTargetA.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialTargetA.setOpacity(targetOpacA);
    }
    
    // *trialTargetB* updates
    if (t >= 0.0 && trialTargetB.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTargetB.tStart = t;  // (not accounting for frame time here)
      trialTargetB.frameNStart = frameN;  // exact frame index
      
      trialTargetB.setAutoDraw(true);
    }

    
    if (trialTargetB.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialTargetB.setOpacity(targetOpacB);
    }
    
    // *trialTargetC* updates
    if (t >= 0.0 && trialTargetC.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTargetC.tStart = t;  // (not accounting for frame time here)
      trialTargetC.frameNStart = frameN;  // exact frame index
      
      trialTargetC.setAutoDraw(true);
    }

    
    if (trialTargetC.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialTargetC.setOpacity(targetOpacC);
    }
    
    // *trialTargetD* updates
    if (t >= 0.0 && trialTargetD.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTargetD.tStart = t;  // (not accounting for frame time here)
      trialTargetD.frameNStart = frameN;  // exact frame index
      
      trialTargetD.setAutoDraw(true);
    }

    
    if (trialTargetD.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialTargetD.setOpacity(targetOpacD);
    }
    
    // *trialTargetE* updates
    if (t >= 0.0 && trialTargetE.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTargetE.tStart = t;  // (not accounting for frame time here)
      trialTargetE.frameNStart = frameN;  // exact frame index
      
      trialTargetE.setAutoDraw(true);
    }

    
    if (trialTargetE.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialTargetE.setOpacity(targetOpacE);
    }
    
    // *trialTargetF* updates
    if (t >= 0.0 && trialTargetF.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTargetF.tStart = t;  // (not accounting for frame time here)
      trialTargetF.frameNStart = frameN;  // exact frame index
      
      trialTargetF.setAutoDraw(true);
    }

    
    if (trialTargetF.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialTargetF.setOpacity(targetOpacF);
    }
    
    // *trialTargetG* updates
    if (t >= 0.0 && trialTargetG.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTargetG.tStart = t;  // (not accounting for frame time here)
      trialTargetG.frameNStart = frameN;  // exact frame index
      
      trialTargetG.setAutoDraw(true);
    }

    
    if (trialTargetG.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialTargetG.setOpacity(targetOpacG);
    }
    
    // *trialTargetH* updates
    if (t >= 0.0 && trialTargetH.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTargetH.tStart = t;  // (not accounting for frame time here)
      trialTargetH.frameNStart = frameN;  // exact frame index
      
      trialTargetH.setAutoDraw(true);
    }

    
    if (trialTargetH.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialTargetH.setOpacity(targetOpacH);
    }
    
    // *trialText1* updates
    if (t >= 0.0 && trialText1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialText1.tStart = t;  // (not accounting for frame time here)
      trialText1.frameNStart = frameN;  // exact frame index
      
      trialText1.setAutoDraw(true);
    }

    
    // *trialText2* updates
    if (t >= 0.0 && trialText2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialText2.tStart = t;  // (not accounting for frame time here)
      trialText2.frameNStart = frameN;  // exact frame index
      
      trialText2.setAutoDraw(true);
    }

    
    // *trialText3* updates
    if (t >= 0.0 && trialText3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialText3.tStart = t;  // (not accounting for frame time here)
      trialText3.frameNStart = frameN;  // exact frame index
      
      trialText3.setAutoDraw(true);
    }

    
    // *trialText4* updates
    if (t >= 0.0 && trialText4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialText4.tStart = t;  // (not accounting for frame time here)
      trialText4.frameNStart = frameN;  // exact frame index
      
      trialText4.setAutoDraw(true);
    }

    
    // *trialText5* updates
    if (t >= 0.0 && trialText5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialText5.tStart = t;  // (not accounting for frame time here)
      trialText5.frameNStart = frameN;  // exact frame index
      
      trialText5.setAutoDraw(true);
    }

    
    // *trialText6* updates
    if (t >= 0.0 && trialText6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialText6.tStart = t;  // (not accounting for frame time here)
      trialText6.frameNStart = frameN;  // exact frame index
      
      trialText6.setAutoDraw(true);
    }

    
    // *trialText7* updates
    if (t >= 0.0 && trialText7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialText7.tStart = t;  // (not accounting for frame time here)
      trialText7.frameNStart = frameN;  // exact frame index
      
      trialText7.setAutoDraw(true);
    }

    
    // *trialText8* updates
    if (t >= 0.0 && trialText8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialText8.tStart = t;  // (not accounting for frame time here)
      trialText8.frameNStart = frameN;  // exact frame index
      
      trialText8.setAutoDraw(true);
    }

    
    // *trialTextA* updates
    if (t >= 0.0 && trialTextA.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTextA.tStart = t;  // (not accounting for frame time here)
      trialTextA.frameNStart = frameN;  // exact frame index
      
      trialTextA.setAutoDraw(true);
    }

    
    // *trialTextB* updates
    if (t >= 0.0 && trialTextB.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTextB.tStart = t;  // (not accounting for frame time here)
      trialTextB.frameNStart = frameN;  // exact frame index
      
      trialTextB.setAutoDraw(true);
    }

    
    // *trialTextC* updates
    if (t >= 0.0 && trialTextC.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTextC.tStart = t;  // (not accounting for frame time here)
      trialTextC.frameNStart = frameN;  // exact frame index
      
      trialTextC.setAutoDraw(true);
    }

    
    // *trialTextD* updates
    if (t >= 0.0 && trialTextD.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTextD.tStart = t;  // (not accounting for frame time here)
      trialTextD.frameNStart = frameN;  // exact frame index
      
      trialTextD.setAutoDraw(true);
    }

    
    // *trialTextE* updates
    if (t >= 0.0 && trialTextE.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTextE.tStart = t;  // (not accounting for frame time here)
      trialTextE.frameNStart = frameN;  // exact frame index
      
      trialTextE.setAutoDraw(true);
    }

    
    // *trialTextF* updates
    if (t >= 0.0 && trialTextF.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTextF.tStart = t;  // (not accounting for frame time here)
      trialTextF.frameNStart = frameN;  // exact frame index
      
      trialTextF.setAutoDraw(true);
    }

    
    // *trialTextG* updates
    if (t >= 0.0 && trialTextG.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTextG.tStart = t;  // (not accounting for frame time here)
      trialTextG.frameNStart = frameN;  // exact frame index
      
      trialTextG.setAutoDraw(true);
    }

    
    // *trialTextH* updates
    if (t >= 0.0 && trialTextH.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTextH.tStart = t;  // (not accounting for frame time here)
      trialTextH.frameNStart = frameN;  // exact frame index
      
      trialTextH.setAutoDraw(true);
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
    for (const thisComponent of trialComponents)
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


function trialRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'trial'-------
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    thisExp.addData("step", steps);
    
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('trialMouse.x', trialMouse.x);
    psychoJS.experiment.addData('trialMouse.y', trialMouse.y);
    psychoJS.experiment.addData('trialMouse.leftButton', trialMouse.leftButton);
    psychoJS.experiment.addData('trialMouse.midButton', trialMouse.midButton);
    psychoJS.experiment.addData('trialMouse.rightButton', trialMouse.rightButton);
    psychoJS.experiment.addData('trialMouse.time', trialMouse.time);
    
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  document.documentElement.style.cursor = 'auto';
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
