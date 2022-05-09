// frida -U -f io.dcloud.W2Awww.soliao.com -l D:/Projects/souliao/cipher.js --no-pause
// frida -U -f io.dcloud.W2Awww.soliao.com -l D:/Projects/souliao/TechnologyCenterDetailPresenter.js --no-pause
// adb logcat | findstr io.dcloud.W2Awww.soliao.com >D:\log.txt

// 被动调用  整体
Java.perform(function(){
    console.warn("*** Start Hook ***")

    var hook = Java.use('f.a.a.a.a.a.d');
    console.error("******************************************************************************")
    hook.a.overload('java.lang.Object').implementation = function(obj){
        console.error("*** obj值(Object): ***")
        var JSONObject = Java.use("com.alibaba.fastjson.JSONObject");
        console.error(JSONObject.toJSON(obj))

        var return_ns = this.a(obj);
        console.error("*** 返回值: ***")
        console.error(return_ns)
        console.error("******************************************************************************")
        return return_ns;
    }
})


//// 主动调用 a2    [48,-127,-97,48,13,6,9,42,-122,72,-122,-9,13,1,1,1,5,0,3,-127,-115,0,48,-127,-119,2,-127,-127,0,-96,85,93,-106,-103,5,95,45,74,-124,-127,121,-100,74,30,-115,-47,-34,86,90,51,-115,-102,35,118,81,5,-16,-56,0,-36,-76,32,65,12,31,62,-21,76,-40,-88,127,112,-90,-116,97,33,124,78,59,33,115,-81,-111,-13,29,-94,-119,-121,109,-87,106,79,-64,64,16,-86,-69,78,-113,57,-88,-63,7,115,91,-2,-45,-19,-1,49,-34,-108,-4,-83,74,32,29,110,-121,-104,-38,52,108,91,74,-32,14,34,-112,-41,-30,68,12,81,-30,-5,35,22,-18,87,92,-78,-120,41,-78,97,33,-83,73,28,-72,78,15,-50,-96,-104,-107,2,3,1,0,1]
//Java.perform(function() {
//    console.warn("*** Start Hook ***")
//    var str = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCgVV2WmQVfLUqEgXmcSh6N0d5WWjONmiN2UQXwyADctCBBDB8+60zYqH9wpoxhIXxOOyFzr5HzHaKJh22pak/AQBCqu06POajBB3Nb/tPt/zHelPytSiAdboeY2jRsW0rgDiKQ1+JEDFHi+yMW7ldcsogpsmEhrUkcuE4PzqCYlQIDAQAB"
//
//    console.error("******************************************************************************")
//    var h = Java.use('f.a.a.a.a.a.h');
//    var a2 = h.a(str);
//    console.error("*** 返回值: ***")
//    console.log(a2)
//    console.error("******************************************************************************")
//    return a2
//})


// 被动调用  a3
Java.perform(function(){
    console.warn("*** Start Hook ***")

    var hook = Java.use('a.v.M');
    console.error("******************************************************************************")
    hook.a.overload('java.lang.String', 'java.security.PublicKey').implementation = function(str, publicKey){
        console.error("*** str值(String): ***")
        console.error(str)

        console.error("*** publicKey值(Object): ***")
        var JSONObject = Java.use("com.alibaba.fastjson.JSONObject");
        console.error(JSONObject.toJSON(publicKey))

        var return_ns = this.a(str, publicKey);
        console.error("*** 返回值(String): ***")
        console.error(return_ns)
        console.error("******************************************************************************")
        return return_ns;
    }
})