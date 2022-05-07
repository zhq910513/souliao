// sig     com.yxcorp.gifshow.retrofit.k
Java.perform(function(){
    console.warn("*** Start Hook ***")

    var hookSig = Java.use('f.a.a.a.a.l.a.yd');
    hookSig.b.implementation = function(arr){
        var Map = Java.use('java.util.HashMap');
        console.error("************* args_map 传入值 *************")
        var args_map = Java.cast(arr, Map);
        console.log(args_map.toString())

        var return_sig = this.b(arr);
        console.error("***************************************** args_map 传入值 *****************************************")
        console.log(args_map.toString())
        console.error("**************************************************************************************************")
        return return_sig;
    }
})