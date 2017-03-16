function ModelClock(options) {//options = {'length':<minutes>}
    this._time = 0;//по идее для моделе не важно время начала
    this._endTime = options.length;
    this._statusClock; //'working' || 'timeIsOver'
    }
ModelClock.prototype.renderingTime = function(nextTime) {
    if(this._time < this._endTime){
        this._time +=nextTime;
        this._statusClock = 'working';
    }
    else {
        this._statusClock = 'timeIsOver';
    }
};
ModelClock.prototype.startTime = function() {
    this._statusClock = 'working';
};
ModelClock.prototype.getTime = function() {
    return this._time;
};
ModelClock.prototype.getStatusClock = function() {
    return this._statusClock;
};
function UniformBaseGenerate(options) {//options = {'factor':<value>, 'increment':<value>, 'module:<value>', 'primary':<value>}
    this._factor = options.factor;
    this._increment = options.increment;
    this._module = options.module;
    this._previous = options.primary;
}
UniformBaseGenerate.prototype.generalValue = function() {
    this._previous = (this._factor * this._previous + this._increment) % this._module;
    return Math.round(((this._previous + 1) / (this._module + 1))*1000) / 1000;
};
function UniformGenerate(options) { //options = {'beginInterval':<mitutes>,'endInterval':<minutes>} union options for unibase and uni
    UniformBaseGenerate.apply(this, arguments);
    this._beginInterval = options.beginInterval;
    this._lengthInterval = options.endInterval - options.beginInterval;
}
UniformGenerate.prototype = Object.create(UniformBaseGenerate.prototype);
UniformGenerate.prototype.generalValue = function() {
    var baseValue = UniformBaseGenerate.prototype.generalValue.call(this);
    return this._beginInterval + Math.round((this._lengthInterval * baseValue) * 1000) / 1000;
};

function Queue(options) { //options = {'discipline':<value>,'length':<value>}
    this._queue = [];
    this._discipline = oprions.discepline;
    this._length = options.length;
}
Queue.prototype.srtToLine = function(transactus) {
    var count = 0;
    for( var i = 0; i < this._queue.lenght; i++) {
        count++;
    }
    if(count >= this._lenght) {
        return false;
    }
    this._queue.push(transactus);
    return true;
}
Queue.prototype.getToLine = function() {
    if(this._queue == []) {
        return false;
    }
    if(this.discipline = 'FIFO') {
        var transactus = this._queue.shift();
        return transactus;
    }
    
    var transactus = this._queue.pop();
    return transactus;
};
function PointOfEntry(options) {
    this._transactusConstructor = options.transactusConstructor;
    this._distributionLaw;
    this._timeEntry;
    this._currentTime;
};
PointOfEntry.prototype.setGenerate = function(Generate) { //Generate = new UniformGenerate(options);
    this._distributionLaw = Generate;
};
PointOfEntry.prototype.getTimeEvent = function() {    
    this._timeEntry = this._distributionLaw.generalValue();
    return this._timeEntry;
};
PointOfEntry.prototype.setCurrentTime = function(time) {
    this._currentTime = time;
};
PointOfEntry.prototype.eventEntry = function() {
    if(this._currentTime == this._timeEntry) {
        var Entry = new this._transactusConstructor();
    }
    else {
        var Entry = false;
    }
    this._timeEntry = this._currentTime + this._distributionLaw.generalValue();
    return Entry;
};
function Transactus() {
    this._timeOfProcessing;
};
Transactus.prototype.setTimeOfProcessing = function(time) {
    this._timeOfProcessing = time;
};
Transactus.prototype.getTimeOfProcessing = function() {
    return this._timeOfProcessing;
};
function Barber() {
    this._status = 'Free';//or Busy
};
Barber.prototype.getStatus = function() {
    return this._status;
};
barber.prototype.setStatus = function() {
    if(this._status == 'Free') {
        this._status = 'Busy';
    }
    else {
        this._status = 'Free';
    }
};
function ModelMachine() {
};
/*/
ModelMachine.prototype.init = function () {
    this._countTime = new ModelClock({'length':480});
    this._queue = new Queue({'discipline':'FIFO','length':10});
    this._distributionLaw = new UniformGenerate({'factor':1 220 703 125, 'increment':7, 'module':2147483647, 'primary':7,'beginInterval':10,'endInterval':60});
    this._pointOfEntry = new PointOfEntry({'transactusConstructor':Transactus.prototype.constructor()});
    this._barber = new Barber();
    this._currentEvent = [];
    this._nextEvent = [];
    this._static = 0;
    this._pointOfEntry.setGenerate(this._distributionLaw);
};
ModelMachine.prototype.renderEvent = function(currentTime) {

};
ModelMachine.prototype.run = function() {
    this._countTime.startTime();
    while(this._countTime.getStatusClock() == 'working') {
        var currentTime = this._countTime.getTime();
        this._pointOfEntry.setCurrentTime(countTime);
        var nextTime = this._pointOfEntry.getTimeEvent();
        this._nextEvent.push(nextTime);
        for( var i = 0; i < this._nextEvent.length; i++) {
            if( this._nextEvent[i] == currentTime) {
                var currentEvent = this._nextEvent.splice(i,1);
                this._currentEvent.push(currentEvent);
            }
        }
        if(this._currentEvent == []) {
            continue;
        }
        if(this._barber.getStatus() == 'Free') {
            
/*/