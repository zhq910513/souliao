Java.perform(function(){
    console.warn("*** Start Hook ***")

    var hookSig = Java.use('f.a.a.a.a.l.a.Fd');
    hookSig.a.overload('java.util.HashMap').implementation = function(arr){
        var Map = Java.use('java.util.HashMap');
        console.error("************* args_map 传入值 *************")
        var args_map = Java.cast(arr, Map);
        console.log(args_map.toString())
    }
})