function CoffeMachine(power){
    this._power = power;
    this._waterAmount = 0;
    this.WATER_HEAT_CAPACITY = 4200;
};
CoffeMachine.prototype.getTimeToBoil = function(){
    return this._waterAmount * this.WATER_HEAT_CAPACITY *80 / this._power 
};
CoffeMachine.prototype.run = function(){
    if(this._waterAmount != 0){
        return function(){
            setTimeout(function(){alert("Готово!");},this.getTimeToBoil());}
    }
    else {
        alert("Сначала залейте воду!!");
    }
};
CoffeMachine.prototype.setAmount = function(amount){
    this._waterAmount += amount;
};

function Clock(options){
    this.template = options.template;
    this.timer;
};
Clock.prototype.render = function() {
    var date = new Date();
    var hours = date.getHours();
    
    if(hours < 10)
        hours = '0' + hours;

    var minuts = date.getMinutes();
    
    if(minuts < 10)
        minutes = '0' + minuts;
     
    var sec = date.getSeconds();
    
    if(sec < 10) 
        sec = '0' + sec;
    var output = this.template.replace('h',hours).replace('m',minuts).replace('s',sec);
    
    
    console.log(output);
};

Clock.prototype.stop = function() {
    clearInterval(this.timer);
};

Clock.prototype.start = function() {
    this.render();
    var self = this;
    this.timer = setInterval(function(){self.render();},1000);
}

function ExtendedClock(options) {
    Clock.apply(this,arguments);
}
ExtendedClock.prototype = Object.create(Clock.prototype);
ExtendedClock.prototype.constructor = ExtendedClock;
ExtendedClock.prototype.start = function(precision) {
    this.render;
    var self = this;
    this.timer = setInterval(function(){self.render();},precision);
}