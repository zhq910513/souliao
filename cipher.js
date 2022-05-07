function main() {

if (Java.available) {

Java.perform(function(){

const Cipher = Java.use('javax.crypto.Cipher');

Cipher.init.overload('int', 'java.security.Key', 'java.security.spec.AlgorithmParameterSpec').implementation = function (opmode, key, iv){

if (iv.$className == 'javax.crypto.spec.IvParameterSpec'){

var opmodestring = this.getOpmodeString(opmode);

var algo = this.getAlgorithm();

const keyclass = Java.use('javax.crypto.spec.SecretKeySpec');

const ivclass = Java.use('javax.crypto.spec.IvParameterSpec');

var keystoreKey = Java.cast(key, keyclass);

var ivInstance = Java.cast(iv,ivclass);

var result=this.init(opmode,key,iv);

console.log('[] opmode:'+opmodestring);

console.log('[] algorithm:'+algo);

console.log('[] key className:'+key.$className);

console.log('[] key value:'+ JSON.stringify(keystoreKey.getEncoded());

console.log('[] iv value:'+JSON.stringify(ivInstance.getIV());

}

return result;

}

})

}

}

setImmediate(main)
