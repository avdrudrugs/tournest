"use strict";this.default_IdentityRotateCookiesHttp=this.default_IdentityRotateCookiesHttp||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){("undefined"!==typeof globalThis?globalThis:"undefined"!==typeof self?self:this)._F_toggles=a||[]};(0,_._F_toggles_initialize)([0xc0, ]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var r=function(a){return ba?q?q.brands.some(function(b){return(b=b.brand)&&-1!=b.indexOf(a)}):!1:!1},v=function(a){var b;a:{if(b=u.navigator)if(b=b.userAgent)break a;b=""}return-1!=b.indexOf(a)},x=function(){return ba?!!q&&0<q.brands.length:!1},y=function(){return x()?r("Chromium"):(v("Chrome")||v("CriOS"))&&!(x()?0:v("Edge"))||v("Silk")},z=function(){return"function"===typeof BigInt},E=function(a){var b=0>a;a=Math.abs(a);var c=a>>>0;a=Math.floor((a-c)/4294967296);b&&(c=A(B(c,a)),b=c.next().value,
a=c.next().value,c=b);C=c>>>0;D=a>>>0},da=function(a,b){b>>>=0;a>>>=0;if(2097151>=b)var c=""+(4294967296*b+a);else z()?c=""+(BigInt(b)<<BigInt(32)|BigInt(a)):(c=(a>>>24|b<<8)&16777215,b=b>>16&65535,a=(a&16777215)+6777216*c+6710656*b,c+=8147497*b,b*=2,1E7<=a&&(c+=Math.floor(a/1E7),a%=1E7),1E7<=c&&(b+=Math.floor(c/1E7),c%=1E7),c=b+ca(c)+ca(a));return c},ca=function(a){a=String(a);return"0000000".slice(a.length)+a},ea=function(){var a=C,b=D;b&2147483648?z()?a=""+(BigInt(b|0)<<BigInt(32)|BigInt(a>>>0)):
(b=A(B(a,b)),a=b.next().value,b=b.next().value,a="-"+da(a,b)):a=da(a,b);return a},B=function(a,b){b=~b;a?a=~a+1:b+=1;return[a,b]},fa=function(a){var b=F(a);1!==(b&1)&&(Object.isFrozen(a)&&(a=Array.prototype.slice.call(a)),G(a,b|1))},ia=function(){var a=[];ha(a,1);return a},H=function(a){a=a>>14&1023;return 0===a?536870912:a},ka=function(a){return!(!a||"object"!==typeof a||a.K!==ja)},I=function(a){return null!==a&&"object"===typeof a&&!Array.isArray(a)&&a.constructor===Object},J=function(a,b,c){if(!Array.isArray(a)||
a.length)return!1;var d=F(a);if(d&1)return!0;if(!(b&&(Array.isArray(b)?b.includes(c):b.has(c))))return!1;G(a,d|1);return!0},K=function(a){a=Error(a);a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity="warning";return a},ma=function(a){var b=typeof a;return"number"===b?Number.isFinite(a):"string"!==b?!1:la.test(a)},na=function(a){return"-"===a[0]?20>a.length?!0:20===a.length&&-922337<Number(a.substring(0,7)):19>a.length?!0:19===
a.length&&922337>Number(a.substring(0,6))},oa=function(a){a=Math.trunc(a);if(!Number.isSafeInteger(a)){E(a);var b=C,c=D;if(a=c&2147483648)b=~b+1>>>0,c=~c>>>0,0==b&&(c=c+1>>>0);b=4294967296*c+(b>>>0);a=a?-b:b}return a},pa=function(a){var b=Math.trunc(Number(a));if(Number.isSafeInteger(b))return String(b);b=a.indexOf(".");-1!==b&&(a=a.substring(0,b));if(!na(a)){if(16>a.length)E(Number(a));else if(z())a=BigInt(a),C=Number(a&BigInt(4294967295))>>>0,D=Number(a>>BigInt(32)&BigInt(4294967295));else{b=+("-"===
a[0]);D=C=0;for(var c=a.length,d=b,g=(c-b)%6+b;g<=c;d=g,g+=6)d=Number(a.slice(d,g)),D*=1E6,C=1E6*C+d,4294967296<=C&&(D+=Math.trunc(C/4294967296),D>>>=0,C>>>=0);b&&(b=A(B(C,D)),a=b.next().value,b=b.next().value,C=a,D=b)}a=ea()}return a},M=function(a,b,c){null==a&&(a=L);L=void 0;if(null==a){var d=96;c?(a=[c],d|=512):a=[];b&&(d=d&-16760833|(b&1023)<<14)}else{if(!Array.isArray(a))throw Error();d=F(a);if(d&64)return a;d|=64;if(c&&(d|=512,c!==a[0]))throw Error();a:{c=a;var g=c.length;if(g){var h=g-1;if(I(c[h])){d|=
256;b=h-(+!!(d&512)-1);if(1024<=b)throw Error();d=d&-16760833|(b&1023)<<14;break a}}if(b){b=Math.max(b,g-(+!!(d&512)-1));if(1024<b)throw Error();d=d&-16760833|(b&1023)<<14}}}G(a,d);return a},ra=function(a,b){return qa(b)},qa=function(a){switch(typeof a){case "number":return isFinite(a)?a:String(a);case "boolean":return a?1:0;case "object":if(a){if(Array.isArray(a))return sa||!J(a,void 0,9999)?a:void 0;if(ta&&null!=a&&a instanceof Uint8Array){if(ua){for(var b="",c=0,d=a.length-10240;c<d;)b+=String.fromCharCode.apply(null,
a.subarray(c,c+=10240));b+=String.fromCharCode.apply(null,c?a.subarray(c):a);a=btoa(b)}else{void 0===b&&(b=0);if(!N){N={};c="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split("");d=["+/=","+/","-_=","-_.","-_"];for(var g=0;5>g;g++){var h=c.concat(d[g].split(""));va[g]=h;for(var e=0;e<h.length;e++){var f=h[e];void 0===N[f]&&(N[f]=e)}}}b=va[b];c=Array(Math.floor(a.length/3));d=b[64]||"";for(g=h=0;h<a.length-2;h+=3){var k=a[h],l=a[h+1];f=a[h+2];e=b[k>>2];k=b[(k&3)<<4|l>>4];l=b[(l&
15)<<2|f>>6];f=b[f&63];c[g++]=e+k+l+f}e=0;f=d;switch(a.length-h){case 2:e=a[h+1],f=b[(e&15)<<2]||d;case 1:a=a[h],c[g]=b[a>>2]+b[(a&3)<<4|e>>4]+f+d}a=c.join("")}return a}}}return a},xa=function(a,b,c,d,g,h){if(null!=a){if(Array.isArray(a))a=g&&0==a.length&&F(a)&1?void 0:h&&F(a)&2?a:wa(a,b,c,void 0!==d,g,h);else if(I(a)){var e={},f;for(f in a)e[f]=xa(a[f],b,c,d,g,h);a=e}else a=b(a,d);return a}},wa=function(a,b,c,d,g,h){var e=d||c?F(a):0;d=d?!!(e&32):void 0;a=Array.prototype.slice.call(a);for(var f=
0;f<a.length;f++)a[f]=xa(a[f],b,c,d,g,h);c&&c(e,a);return a},za=function(a){return a.H===ya?a.toJSON():qa(a)},Ca=function(a,b,c){var d=a.constructor.L,g=O(c?a.j:b),h=H(g),e=!1;if(d&&sa){if(!c){b=Array.prototype.slice.call(b);var f;if(b.length&&I(f=b[b.length-1]))for(e=0;e<d.length;e++)if(d[e]>=h){Object.assign(b[b.length-1]={},f);break}e=!0}h=b;c=!c;f=O(a.j);a=H(f);f=+!!(f&512)-1;for(var k,l,m=0;m<d.length;m++)if(l=d[m],l<a){l+=f;var p=h[l];null==p?h[l]=c?Q:ia():c&&p!==Q&&fa(p)}else k||(p=void 0,
h.length&&I(p=h[h.length-1])?k=p:h.push(k={})),p=k[l],null==k[l]?k[l]=c?Q:ia():c&&p!==Q&&fa(p)}k=b.length;if(!k)return b;var t;if(I(h=b[k-1])){a:{var n=h;c={};a=!1;for(var w in n){f=n[w];if(Array.isArray(f)){m=f;if(!Aa&&J(f,d,+w)||!Ba&&ka(f)&&0===f.size)f=null;f!=m&&(a=!0)}null!=f?c[w]=f:a=!0}if(a){for(var P in c){n=c;break a}n=null}}n!=h&&(t=!0);k--}for(g=+!!(g&512)-1;0<k;k--){w=k-1;h=b[w];if(!(null==h||!Aa&&J(h,d,w-g)||!Ba&&ka(h)&&0===h.size))break;var $a=!0}if(!t&&!$a)return b;var aa;e?aa=b:aa=
Array.prototype.slice.call(b,0,k);b=aa;e&&(b.length=k);n&&b.push(n);return b},Da=function(a){var b=0;return function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}}},Ea="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;a[b]=c.value;return a},Fa=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=
a[b];if(c&&c.Math==Math)return c}throw Error("a");},R=Fa(this),S=function(a,b){if(b)a:{var c=R;a=a.split(".");for(var d=0;d<a.length-1;d++){var g=a[d];if(!(g in c))break a;c=c[g]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&null!=b&&Ea(c,a,{configurable:!0,writable:!0,value:b})}},A=function(a){var b="undefined"!=typeof Symbol&&Symbol.iterator&&a[Symbol.iterator];if(b)return b.call(a);if("number"==typeof a.length)return{next:Da(a)};throw Error("b`"+String(a));},Ga="function"==typeof Object.create?Object.create:
function(a){var b=function(){};b.prototype=a;return new b},Ha;if("function"==typeof Object.setPrototypeOf)Ha=Object.setPrototypeOf;else{var Ia;a:{var Ja={a:!0},Ka={};try{Ka.__proto__=Ja;Ia=Ka.a;break a}catch(a){}Ia=!1}Ha=Ia?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError("c`"+a);return a}:null}
var La=Ha,Ma=function(a,b){a.prototype=Ga(b.prototype);a.prototype.constructor=a;if(La)La(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.M=b.prototype};
S("Promise",function(a){function b(){this.g=null}function c(e){return e instanceof g?e:new g(function(f){f(e)})}if(a)return a;b.prototype.h=function(e){if(null==this.g){this.g=[];var f=this;this.i(function(){f.o()})}this.g.push(e)};var d=R.setTimeout;b.prototype.i=function(e){d(e,0)};b.prototype.o=function(){for(;this.g&&this.g.length;){var e=this.g;this.g=[];for(var f=0;f<e.length;++f){var k=e[f];e[f]=null;try{k()}catch(l){this.m(l)}}}this.g=null};b.prototype.m=function(e){this.i(function(){throw e;
})};var g=function(e){this.h=0;this.i=void 0;this.g=[];this.v=!1;var f=this.m();try{e(f.resolve,f.reject)}catch(k){f.reject(k)}};g.prototype.m=function(){function e(l){return function(m){k||(k=!0,l.call(f,m))}}var f=this,k=!1;return{resolve:e(this.C),reject:e(this.o)}};g.prototype.C=function(e){if(e===this)this.o(new TypeError("d"));else if(e instanceof g)this.F(e);else{a:switch(typeof e){case "object":var f=null!=e;break a;case "function":f=!0;break a;default:f=!1}f?this.B(e):this.u(e)}};g.prototype.B=
function(e){var f=void 0;try{f=e.then}catch(k){this.o(k);return}"function"==typeof f?this.G(f,e):this.u(e)};g.prototype.o=function(e){this.A(2,e)};g.prototype.u=function(e){this.A(1,e)};g.prototype.A=function(e,f){if(0!=this.h)throw Error("e`"+e+"`"+f+"`"+this.h);this.h=e;this.i=f;2===this.h&&this.D();this.I()};g.prototype.D=function(){var e=this;d(function(){if(e.J()){var f=R.console;"undefined"!==typeof f&&f.error(e.i)}},1)};g.prototype.J=function(){if(this.v)return!1;var e=R.CustomEvent,f=R.Event,
k=R.dispatchEvent;if("undefined"===typeof k)return!0;"function"===typeof e?e=new e("unhandledrejection",{cancelable:!0}):"function"===typeof f?e=new f("unhandledrejection",{cancelable:!0}):(e=R.document.createEvent("CustomEvent"),e.initCustomEvent("unhandledrejection",!1,!0,e));e.promise=this;e.reason=this.i;return k(e)};g.prototype.I=function(){if(null!=this.g){for(var e=0;e<this.g.length;++e)h.h(this.g[e]);this.g=null}};var h=new b;g.prototype.F=function(e){var f=this.m();e.s(f.resolve,f.reject)};
g.prototype.G=function(e,f){var k=this.m();try{e.call(f,k.resolve,k.reject)}catch(l){k.reject(l)}};g.prototype.then=function(e,f){function k(t,n){return"function"==typeof t?function(w){try{l(t(w))}catch(P){m(P)}}:n}var l,m,p=new g(function(t,n){l=t;m=n});this.s(k(e,l),k(f,m));return p};g.prototype.catch=function(e){return this.then(void 0,e)};g.prototype.s=function(e,f){function k(){switch(l.h){case 1:e(l.i);break;case 2:f(l.i);break;default:throw Error("f`"+l.h);}}var l=this;null==this.g?h.h(k):
this.g.push(k);this.v=!0};g.resolve=c;g.reject=function(e){return new g(function(f,k){k(e)})};g.race=function(e){return new g(function(f,k){for(var l=A(e),m=l.next();!m.done;m=l.next())c(m.value).s(f,k)})};g.all=function(e){var f=A(e),k=f.next();return k.done?c([]):new g(function(l,m){function p(w){return function(P){t[w]=P;n--;0==n&&l(t)}}var t=[],n=0;do t.push(void 0),n++,c(k.value).s(p(t.length-1),m),k=f.next();while(!k.done)})};return g});
var Na="function"==typeof Object.assign?Object.assign:function(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(d)for(var g in d)Object.prototype.hasOwnProperty.call(d,g)&&(a[g]=d[g])}return a};S("Object.assign",function(a){return a||Na});S("Math.trunc",function(a){return a?a:function(b){b=Number(b);if(isNaN(b)||Infinity===b||-Infinity===b||0===b)return b;var c=Math.floor(Math.abs(b));return 0>b?-c:c}});
S("Object.is",function(a){return a?a:function(b,c){return b===c?0!==b||1/b===1/c:b!==b&&c!==c}});S("Array.prototype.includes",function(a){return a?a:function(b,c){var d=this;d instanceof String&&(d=String(d));var g=d.length;c=c||0;for(0>c&&(c=Math.max(c+g,0));c<g;c++){var h=d[c];if(h===b||Object.is(h,b))return!0}return!1}});
S("String.prototype.includes",function(a){return a?a:function(b,c){if(null==this)throw new TypeError("g`includes");if(b instanceof RegExp)throw new TypeError("h`includes");return-1!==this.indexOf(b,c||0)}});S("Number.isFinite",function(a){return a?a:function(b){return"number"!==typeof b?!1:!isNaN(b)&&Infinity!==b&&-Infinity!==b}});S("Number.MAX_SAFE_INTEGER",function(){return 9007199254740991});S("Number.isInteger",function(a){return a?a:function(b){return Number.isFinite(b)?b===Math.floor(b):!1}});
S("Number.isSafeInteger",function(a){return a?a:function(b){return Number.isInteger(b)&&Math.abs(b)<=Number.MAX_SAFE_INTEGER}});S("Number.isNaN",function(a){return a?a:function(b){return"number"===typeof b&&isNaN(b)}});var u=this||self,Oa=function(a,b){a:{var c=["WIZ_global_data","oxN3nb"];for(var d=u,g=0;g<c.length;g++)if(d=d[c[g]],null==d){c=null;break a}c=d}a=c&&c[a];return null!=a?a:b},T=u._F_toggles||[];var Pa=!!(T[0]&128),Qa=!!(T[0]&4),Ra=!!(T[0]&256),Sa=!!(T[0]&2);var ba=Pa?Ra:Oa(610401301,!1),Ta=Pa?Qa||!Sa:Oa(572417392,!0);var q,Ua=u.navigator;q=Ua?Ua.userAgentData||null:null;var Va=x()?!1:v("Trident")||v("MSIE");!v("Android")||y();y();v("Safari")&&(y()||(x()?0:v("Coast"))||(x()?0:v("Opera"))||(x()?0:v("Edge"))||(x()?r("Microsoft Edge"):v("Edg/"))||x()&&r("Opera"));var va={},N=null;var ta="undefined"!==typeof Uint8Array,ua=!Va&&"function"===typeof btoa;var Ba=!Ta,Aa=!Ta;var C=0,D=0;var U;U="function"===typeof Symbol&&"symbol"===typeof Symbol()?Symbol():void 0;var ha=U?function(a,b){a[U]|=b}:function(a,b){void 0!==a.l?a.l|=b:Object.defineProperties(a,{l:{value:b,configurable:!0,writable:!0,enumerable:!1}})},F=U?function(a){return a[U]|0}:function(a){return a.l|0},O=U?function(a){return a[U]}:function(a){return a.l},G=U?function(a,b){a[U]=b}:function(a,b){void 0!==a.l?a.l=b:Object.defineProperties(a,{l:{value:b,configurable:!0,writable:!0,enumerable:!1}})};var ya={},ja={},Wa,sa=!Ta,Q,Xa=[];G(Xa,55);Q=Object.freeze(Xa);Object.freeze(new function(){});Object.freeze(new function(){});var la=/^-?([1-9][0-9]*|0)(\.[0-9]+)?$/;var L;var Ya=function(a,b,c){var d=a.j,g=O(d);if(g&2)throw Error();a:{var h=H(g);if(b>=h){var e=g;if(g&256)var f=d[d.length-1];else{if(null==c)break a;f=d[h+(+!!(g&512)-1)]={};e|=256}f[b]=c;b<h&&(d[b+(+!!(g&512)-1)]=void 0);e!==g&&G(d,e)}else d[b+(+!!(g&512)-1)]=c,g&256&&(c=d[d.length-1],b in c&&delete c[b])}return a},Za=function(a){var b=void 0===b?0:b;a=a.j;a:{var c=O(a);if(1>=H(c)){if(c&256){a=a[a.length-1][1];break a}}else if(c=1+(+!!(c&512)-1),c<a.length){a=a[c];break a}a=void 0}a=null==a?a:ma(a)?
"number"===typeof a?oa(a):pa(a):void 0;return null!=a?a:b},ab=function(a,b,c){if(null!=c){if("number"!==typeof c)throw K("int32");if(!Number.isFinite(c))throw K("int32");c|=0}Ya(a,b,c)};var V=function(a,b,c){this.j=M(a,b,c)};V.prototype.toJSON=function(){if(Wa)var a=Ca(this,this.j,!1);else a=wa(this.j,za,void 0,void 0,!1,!1),a=Ca(this,a,!0);return a};var bb=function(a){Wa=!0;try{return JSON.stringify(a.toJSON(),ra)}finally{Wa=!1}};V.prototype.H=ya;V.prototype.toString=function(){return Ca(this,this.j,!1).toString()};var cb=function(a){this.j=M(a)};Ma(cb,V);var db=function(a){this.j=M(a,0,"identity.hfcr")};Ma(db,V);var eb=function(a){return function(b){if(null==b||""==b)b=new a;else{b=JSON.parse(b);if(!Array.isArray(b))throw Error(void 0);ha(b,32);L=b;b=new a(b);L=void 0}return b}}(db);var fb=function(a,b,c,d,g,h){this.u=a;this.i=b;this.o=c;this.h=d;this.g=g;this.m=h};fb.prototype.start=function(){var a=this;if("undefined"!==typeof fetch)if(gb()){var b=hb(),c=Date.now();b&&b>c+1E3*this.g&&(b=Date.now()+1E3*this.g,W(b));var d=function(){ib(a).then(function(){a.m||setTimeout(d,1E3*a.g)})};setTimeout(function(){d()},b&&b>c?b-c:0)}else jb(this)};
var jb=function(a){var b=kb(a);a.m||b.then(function(){var c=function(){kb(a).then(function(){setTimeout(c,1E3*a.g)})};setTimeout(function(){c()},1E3*a.g)})},kb=function(a){var b=lb(a);return mb(b).then(function(c){c=nb(Za(c));c!==a.g&&(a.g=c)}).catch(function(){a.g*=2})},ib=function(a){var b=hb();if(!b||Date.now()>=b){var c=Math.floor(1E3*Math.random());return new Promise(function(d){setTimeout(function(){var g=hb();!g||Date.now()>=g?d(ob(a)):d()},c)})}return Promise.resolve()},mb=function(a){a={method:"POST",
credentials:"same-origin",cache:"no-store",mode:"same-origin",headers:{"Content-Type":"application/json"},body:bb(a)};if("undefined"!==typeof AbortController){var b=new AbortController;setTimeout(function(){b.abort()},3E4);a.signal=b.signal}return fetch(new Request("/RotateCookies",a)).then(function(c){return c.text()}).then(function(c){return eb(JSON.stringify(JSON.parse(c.substring(5))[0]))})},lb=function(a){var b=new cb;var c=a.u;if(null!=c){var d=!!d;if(!ma(c))throw K("int64");"string"===typeof c?
c=pa(c):d?(c=Math.trunc(c),Number.isSafeInteger(c)?c=String(c):(d=String(c),na(d)?c=d:(E(c),c=ea()))):c=oa(c)}b=Ya(b,2,c);0!==a.i&&ab(b,1,a.i);0!==a.o&&ab(b,3,a.o);0!==a.h&&ab(b,4,a.h);return b},ob=function(a){W(Date.now()+1E3*a.g);var b=lb(a);return mb(b).then(function(c){c=nb(Za(c));c!==a.g&&(W(Date.now()+1E3*c),a.g=c)}).catch(function(){a.g*=2;W(Date.now()+1E3*a.g)})},gb=function(){try{var a=window.localStorage;if(!a)return!1;a.setItem("cookieRotationStorageAccessTest","1");a.removeItem("cookieRotationStorageAccessTest");
return!0}catch(b){return!1}},nb=function(a){60>a&&(a=60);return a},hb=function(){try{var a=window.localStorage.getItem("nextRotationAttemptTs");if(!a)return null;var b=Math.floor(Number(a));return Number.isNaN(b)?null:b}catch(c){return null}},W=function(a){try{window.localStorage.setItem("nextRotationAttemptTs",a.toString())}catch(b){}};var pb=function(a,b,c,d,g,h){(new fb(a,b,c,d,g,h)).start()},X=["init"],Y=u;X[0]in Y||"undefined"==typeof Y.execScript||Y.execScript("var "+X[0]);for(var Z;X.length&&(Z=X.shift());)X.length||void 0===pb?Y[Z]&&Y[Z]!==Object.prototype[Z]?Y=Y[Z]:Y=Y[Z]={}:Y[Z]=pb;
}catch(e){_._DumpException(e)}
}).call(this,this.default_IdentityRotateCookiesHttp);
// Google Inc.