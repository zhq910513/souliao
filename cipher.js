Java.perform(function() {
    //Base64
    var base64=Java.use('android.util.Base64');
    var string=Java.use('java.lang.String');
    /*base64.encode.overload('[B', 'int', 'int', 'int').implementation = function(){
        send("=================base64 encode====================");
        send(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));
        send(arguments[0]);
        send(arguments[1]);
        send(arguments[2]);
        send(arguments[3]);
        var data=this.encode(arguments[0],arguments[1],arguments[2],arguments[3])
        send("base64:"+string.$new(data));
        return data;
    }*/

    /*base64.decode.overload('[B', 'int', 'int', 'int').implementation = function(){
        send("=================base64 decode====================");
        send(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));
        send(arguments[0]);
        send(arguments[1]);
        send(arguments[2]);
        send(arguments[3]);
        var data=this.decode(arguments[0],arguments[1],arguments[2],arguments[3])
        send("base64:"+string.$new(data));
        return data;
    }*/


    // MD SHA
    var messageDigest=Java.use('java.security.MessageDigest');
    // update
    for(var i = 0; i < messageDigest.update.overloads.length; i++){
        messageDigest.update.overloads[i].implementation = function(){
            var name=this.getAlgorithm()
            send("================="+name+"====================");
            send(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));
            if(arguments.length == 1){
                send(arguments[0]);
                this.update(arguments[0]);
            }else if(arguments.length == 3){
                send(arguments[0]);
                send(arguments[1]);
                send(arguments[2]);
                this.update(arguments[0],arguments[1],arguments[2]);
            }
        }
    }
    // digest
    for(var i = 0; i < messageDigest.digest.overloads.length; i++){
        messageDigest.digest.overloads[i].implementation = function(){
            var name=this.getAlgorithm()
            send("================="+name+"====================");
            send(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));
            if(arguments.length == 0){
                var data=this.digest();
                send(data);
                return data;
            }else if(arguments.length == 1){
                send(arguments[0]);
                var data=this.digest(arguments[0]);
                send(data);
                return data;
            }else if(arguments.length == 3){
                send(arguments[0]);
                send(arguments[1]);
                send(arguments[2]);
                var data=this.digest(arguments[0],arguments[1],arguments[2]);
                send(data);
                return data;
            }
        }
    }

    //MAC
    var mac=Java.use('javax.crypto.Mac');
    for(var i = 0; i < mac.doFinal.overloads.length; i++){
        mac.doFinal.overloads[i].implementation = function(){
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
            }
        }
    }

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

    //KEY
    var secretKey=Java.use('javax.crypto.spec.SecretKeySpec');
    for(var i = 0; i < secretKey.$init.overloads.length; i++){
        secretKey.$init.overloads[i].implementation = function(){
            var name=this.getAlgorithm()
            send("=================KEY====================");
            //send(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));
            if(arguments.length == 2){
                send(arguments[0]);
                send(arguments[1]);
                this.$init(arguments[0],arguments[1]);
            }else if(arguments.length == 4){
                send(arguments[0]);
                send(arguments[1]);
                send(arguments[2]);
                send(arguments[3]);
                this.$init(arguments[0],arguments[1],arguments[2],arguments[3]);
            }
        }
    }
    //IV
    //DES KEY
    //DESede KEY
    //PBE KEY salt
});