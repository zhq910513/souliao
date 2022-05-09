import java.io.ByteArrayOutputStream;
import javax.crypto.Cipher;


public static String a() throws Exception {
    str = '{"a":"8.0","b":{"a":"65493","actionType":"3.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"2412","d":"1","strTime":"1652064519516"}}'
    publicKey = {"algorithm":"RSA","encoded":[48,-127,-97,48,13,6,9,42,-122,72,-122,-9,13,1,1,1,5,0,3,-127,-115,0,48,-127,-119,2,-127,-127,0,-96,85,93,-106,-103,5,95,45,74,-124,-127,121,-100,74,30,-115,-47,-34,86,90,51,-115,-102,35,118,81,5,-16,-56,0,-36,-76,32,65,12,31,62,-21,76,-40,-88,127,112,-90,-116,97,33,124,78,59,33,115,-81,-111,-13,29,-94,-119,-121,109,-87,106,79,-64,64,16,-86,-69,78,-113,57,-88,-63,7,115,91,-2,-45,-19,-1,49,-34,-108,-4,-83,74,32,29,110,-121,-104,-38,52,108,91,74,-32,14,34,-112,-41,-30,68,12,81,-30,-5,35,22,-18,87,92,-78,-120,41,-78,97,33,-83,73,28,-72,78,15,-50,-96,-104,-107,2,3,1,0,1],"format":"X.509","modulus":112589984008212718692705259193944372249782211112088510987075898768994940950434990803948711201570710932916881147902507799109684598069324212146298434886616356316597578161839553557185767404108919194503230088104598642071102679172856797188445394861990619673071701814921024243375551997130470844682603957499090475157,"publicExponent":65537}
    byte[] bArr;
    byte[] bytes = str.getBytes("utf-8");
    Cipher instance = Cipher.getInstance("RSA/None/PKCS1Padding");
    instance.init(1, publicKey);
    int length = bytes.length;
    ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
    int i2 = 0;
    int i3 = 0;
    while (true) {
        int i4 = length - i2;
        if (i4 > 0) {
            if (i4 > 117) {
                bArr = instance.doFinal(bytes, i2, 117);
            } else {
                bArr = instance.doFinal(bytes, i2, i4);
            }
            byteArrayOutputStream.write(bArr, 0, bArr.length);
            i3++;
            i2 = i3 * 117;
        } else {
            byte[] byteArray = byteArrayOutputStream.toByteArray();
            byteArrayOutputStream.close();
            return h(byteArray);
        }
    }
}


public static String h(byte[] bArr) throws Exception {
    int length = bArr.length;
    int i2 = (length * 4) / 3;
    byte[] bArr2 = new byte[((length % 3 > 0 ? 4 : 0) + i2 + (i2 / 76))];
    int i3 = length - 2;
    int i4 = 0;
    int i5 = 0;
    int i6 = 0;
    while (i4 < i3) {
        a(bArr, i4 + 0, 3,
        , i5);
        i6 += 4;
        if (i6 == 76) {
            bArr2[i5 + 4] = 10;
            i5++;
            i6 = 0;
        }
        i4 += 3;
        i5 += 4;
    }
    if (i4 < length) {
        a(bArr, 0 + i4, length - i4, bArr2, i5);
        i5 += 4;
    }
    return new String(bArr2, 0, i5, "iso-8859-1");
}
