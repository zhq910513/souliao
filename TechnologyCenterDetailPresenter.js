Java.perform(function(){
    console.warn("*** Start Hook ***")

<<<<<<< HEAD
    var hookSig = Java.use('f.a.a.a.a.a.d');
    hookSig.a.implementation = function(arr){
=======
    var hookSig = Java.use('f.a.a.a.a.l.a.Fd');
    hookSig.a.overload('java.util.HashMap').implementation = function(arr){
>>>>>>> 2cbb6951e7e22ff4a25a6f459cfcece96873236e
        var Map = Java.use('java.util.HashMap');
        console.error("************* args_map 传入值 *************")
        var args_map = Java.cast(arr, Map);
        console.log(args_map.toString())
    }
})