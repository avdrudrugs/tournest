this._s=this._s||{};(function(_){var window=this;
try{
_.crb=function(a){this.Zm=a};
}catch(e){_._DumpException(e)}
try{
var drb=function(a){_.ao.call(this,a.Ka);var b=this;this.window=a.service.window.get();this.wa=this.Zm();this.oa=window.orientation;this.ka=function(){var c=b.Zm(),d=b.kEb()&&90===Math.abs(window.orientation)&&b.oa===-1*window.orientation;b.oa=window.orientation;if(c!==b.wa||d){b.wa=c;d=_.bb(b.Ne);for(var e=d.next();!e.done;e=d.next()){e=e.value;var f=new _.crb(c);try{e(f)}catch(g){_.ca(g)}}}};this.Ne=new Set;this.window.addEventListener("resize",this.ka);this.kEb()&&this.window.addEventListener("orientationchange",
this.ka)};_.F(drb,_.ao);drb.nb=_.ao.nb;drb.Ha=function(){return{service:{window:_.bo}}};drb.prototype.addListener=function(a){this.Ne.add(a)};drb.prototype.removeListener=function(a){this.Ne.delete(a)};
drb.prototype.Zm=function(){if(erb()){var a=_.El(this.window);a=new _.kl(a.width,Math.round(a.width*this.window.innerHeight/this.window.innerWidth))}else a=this.Vb()||(_.ja()?erb():this.window.visualViewport)?_.El(this.window):new _.kl(this.window.innerWidth,this.window.innerHeight);return a.height<a.width};drb.prototype.destroy=function(){this.window.removeEventListener("resize",this.ka);this.window.removeEventListener("orientationchange",this.ka)};var erb=function(){return _.ja()&&_.cf.tK()&&!navigator.userAgent.includes("GSA")};
drb.prototype.Vb=function(){return _.frb};drb.prototype.kEb=function(){return"orientation"in window};_.frb=!1;_.co(_.UTa,drb);
_.frb=!0;
}catch(e){_._DumpException(e)}
try{
_.x("aLUfP");

_.y();
}catch(e){_._DumpException(e)}
})(this._s);
// Google Inc.
