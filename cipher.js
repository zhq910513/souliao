Java.perform(function() {
    // DES DESede AES PBE RSA
    var cipher=Java.use('javax.crypto.Cipher');
     for(var i = 0; i < cipher.doFinal.overloads.length; i++){
        cipher.doFinal.overloads[i].implementation = function(){
            var name=this.getAlgorithm()
            send("================="+name+"====================");
            send(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));
            if(arguments.length == 0){
                var data=this.doFinal();
                send(data);
                return data;
            }else if(arguments.length == 1){
                send(arguments[0]);
                var data=this.doFinal(arguments[0]);
                send(data);
                return data;
            }else if(arguments.length == 2){
                send(arguments[0]);
                send(arguments[1]);
                var data=this.doFinal(arguments[0],arguments[1]);
                send(data);
                return data;
            }else if(arguments.length == 3){
                send(arguments[0]);
                send(arguments[1]);
                send(arguments[2]);
                var data=this.doFinal(arguments[0],arguments[1],arguments[2]);
                send(data);
                return data;
            }else if(arguments.length == 5){
                send(arguments[0]);
                send(arguments[1]);
                send(arguments[2]);
                send(arguments[3]);
                send(arguments[4]);
                var data=this.doFinal(arguments[0],arguments[1],arguments[2],arguments[3],arguments[4]);
                send(data);
                return data;
            }else{
                send(arguments[0]);
                send(arguments[1]);
                send(arguments[2]);
                send(arguments[3]);
                var data=this.doFinal(arguments[0],arguments[1],arguments[2],arguments[3]);
                send(data);
                return data;
            }
        }
    }
});