at f.a.a.a.a.a.d.a(CommonUtils.java:41)


/* renamed from: a */
public static String m12890a(Object obj) {
        KeyFactory keyFactory;
        try {
            byte[] a = MyBase64.m12901a("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCgVV2WmQVfLUqEgXmcSh6N0d5WWjONmiN2UQXwyADctCBBDB8+60zYqH9wpoxhIXxOOyFzr5HzHaKJh22pak/AQBCqu06POajBB3Nb/tPt/zHelPytSiAdboeY2jRsW0rgDiKQ1+JEDFHi+yMW7ldcsogpsmEhrUkcuE4PzqCYlQIDAQAB");
            if (Build.VERSION.SDK_INT >= 28) {
                keyFactory = KeyFactory.getInstance("RSA");
            } else {
                keyFactory = KeyFactory.getInstance("RSA", "BC");
            }
            String a2 = ViewGroupUtilsApi18.m2063a(JSON.toJSONString(obj), keyFactory.generatePublic(new X509EncodedKeySpec(a)));
            String encode = URLEncoder.encode(a2, "utf-8");
            return encode;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    public static String a(Object obj) {
        KeyFactory keyFactory;
        try {
            byte[] a2 = h.a("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCgVV2WmQVfLUqEgXmcSh6N0d5WWjONmiN2UQXwyADctCBBDB8+60zYqH9wpoxhIXxOOyFzr5HzHaKJh22pak/AQBCqu06POajBB3Nb/tPt/zHelPytSiAdboeY2jRsW0rgDiKQ1+JEDFHi+yMW7ldcsogpsmEhrUkcuE4PzqCYlQIDAQAB");
            if (Build.VERSION.SDK_INT >= 28) {
                keyFactory = KeyFactory.getInstance("RSA");
            } else {
                keyFactory = KeyFactory.getInstance("RSA", "BC");
            }
            String a3 = M.a(JSON.toJSONString(obj), keyFactory.generatePublic(new X509EncodedKeySpec(a2)));
            String encode = URLEncoder.encode(a3, "utf-8");
            Log.e("fwefwefwe", "getUserInfo:加密后 " + a3);
            String a4 = M.a(a3, keyFactory.generatePrivate(new PKCS8EncodedKeySpec(h.a("MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAKBVXZaZBV8tSoSBeZxKHo3R3lZaM42aI3ZRBfDIANy0IEEMHz7rTNiof3CmjGEhfE47IXOvkfMdoomHbalqT8BAEKq7To85qMEHc1v+0+3/Md6U/K1KIB1uh5jaNGxbSuAOIpDX4kQMUeL7IxbuV1yyiCmyYSGtSRy4Tg/OoJiVAgMBAAECgYB4YqB6yzq1VBR3mZ/uMdjvM3116RR8ZhfqZrvHJuU+0iDFtoxfed2hcCMAOo19AN+M/ekIK/OyT7YS/ZThd+mYgsXSDvmAM1iSylZ36ABT3btFTYu6xtdf2M4uGloXue50zXT6nPVmEmbO7BWQZgJPxvy3IwkvBEUWJkdS2E2soQJBAPTuNFL+vDlempJ3kggJjCFr2J8+Zt2KpyTeICllIo+DwA35ef5CCLb/7grsBviZ3KVIFNjw1mykqcM6JUjgQjcCQQCnlGQR7vBb7mO0kjsX1cQOY6lFBcZ5JEO4K97HqF0LdvkQ9yVS0jNikkBrrRI6+wZkVgZIr2tv+9Y+TJh+LIWTAkEA18S455xtKIUE2p7nUJlIj3C4ZqDMccJhuILOBmmH5rIEEMuEAs8daklP5ONEyOCSljBH3U1dOFxfCRNCIU8eRQJAJvliFLGngRn+Yl6oE7EJufb/xSfEsyP2A/1gALtteF8hKgrwyURN4xz0kpZb6Q+8utUu/PSfXhoKB880oBOmtQJAJVzyvuHQVlWjS08yFOvCpT1LpGVC4LO0X3CoyHmXU91F5VOCMBONuCAO09nvHCP/WpSrutQPYtj4JrVtr9uClA=="))));
            Log.e("fwefwefwe", "getUserInfo:解密后 " + a4);
            return encode;
        } catch (Exception e2) {
            e2.printStackTrace();
            return null;
        }
    }


/* renamed from: a */
public static byte[] m12901a(String str) throws Exception {
        byte[] bytes = str.getBytes("utf-8");
        int length = bytes.length;
        byte[] bArr = new byte[((length * 3) / 4)];
        byte[] bArr2 = new byte[4];
        int i = 0;
        int i2 = 0;
        for (byte b : bytes) {
            byte b2 = (byte) (b & Byte.MAX_VALUE);
            byte[] bArr3 = f14737b;
            byte b3 = bArr3[b2];
            if (b3 < -5) {
                return null;
            }
            if (b3 >= -1) {
                int i3 = i + 1;
                bArr2[i] = b2;
                int i4 = 3;
                if (i3 > 3) {
                    if (bArr2[2] == 61) {
                        bArr[i2] = (byte) ((((bArr3[bArr2[0]] & 255) << 18) | ((bArr3[bArr2[1]] & 255) << 12)) >>> 16);
                        i4 = 1;
                    } else if (bArr2[3] == 61) {
                        int i5 = ((bArr3[bArr2[0]] & 255) << 18) | ((bArr3[bArr2[1]] & 255) << 12) | ((bArr3[bArr2[2]] & 255) << 6);
                        bArr[i2] = (byte) (i5 >>> 16);
                        bArr[i2 + 1] = (byte) (i5 >>> 8);
                        i4 = 2;
                    } else {
                        try {
                            int i6 = (bArr3[bArr2[3]] & 255) | ((bArr3[bArr2[2]] & 255) << 6) | ((bArr3[bArr2[0]] & 255) << 18) | ((bArr3[bArr2[1]] & 255) << 12);
                            bArr[i2] = (byte) (i6 >> 16);
                            bArr[i2 + 1] = (byte) (i6 >> 8);
                            bArr[i2 + 2] = (byte) i6;
                        } catch (Exception unused) {
                            i4 = -1;
                        }
                    }
                    i2 += i4;
                    if (b2 == 61) {
                        break;
                    }
                    i = 0;
                } else {
                    i = i3;
                }
            }
        }
        byte[] bArr4 = new byte[i2];
        System.arraycopy(bArr, 0, bArr4, 0, i2);
        return bArr4;
    }
}

    public static byte[] a(String str) throws Exception {
        byte[] bytes = str.getBytes("utf-8");
        int length = bytes.length;
        byte[] bArr = new byte[((length * 3) / 4)];
        byte[] bArr2 = new byte[4];
        int i2 = 0;
        int i3 = 0;
        for (byte b2 : bytes) {
            byte b3 = (byte) (b2 & Byte.MAX_VALUE);
            byte[] bArr3 = f11242b;
            byte b4 = bArr3[b3];
            if (b4 < -5) {
                return null;
            }
            if (b4 >= -1) {
                int i4 = i2 + 1;
                bArr2[i2] = b3;
                int i5 = 3;
                if (i4 > 3) {
                    if (bArr2[2] == 61) {
                        bArr[i3] = (byte) ((((bArr3[bArr2[0]] & 255) << 18) | ((bArr3[bArr2[1]] & 255) << 12)) >>> 16);
                        i5 = 1;
                    } else if (bArr2[3] == 61) {
                        int i6 = ((bArr3[bArr2[0]] & 255) << 18) | ((bArr3[bArr2[1]] & 255) << 12) | ((bArr3[bArr2[2]] & 255) << 6);
                        bArr[i3] = (byte) (i6 >>> 16);
                        bArr[i3 + 1] = (byte) (i6 >>> 8);
                        i5 = 2;
                    } else {
                        try {
                            int i7 = (bArr3[bArr2[3]] & 255) | ((bArr3[bArr2[2]] & 255) << 6) | ((bArr3[bArr2[0]] & 255) << 18) | ((bArr3[bArr2[1]] & 255) << 12);
                            bArr[i3] = (byte) (i7 >> 16);
                            bArr[i3 + 1] = (byte) (i7 >> 8);
                            bArr[i3 + 2] = (byte) i7;
                        } catch (Exception unused) {
                            i5 = -1;
                        }
                    }
                    i3 += i5;
                    if (b3 == 61) {
                        break;
                    }
                    i2 = 0;
                } else {
                    i2 = i4;
                }
            }
        }
        byte[] bArr4 = new byte[i3];
        System.arraycopy(bArr, 0, bArr4, 0, i3);
        return bArr4;
    }
}



/* renamed from: a */
public static String m2063a(String str, PublicKey publicKey) throws Exception {
        byte[] bArr;
        byte[] bytes = str.getBytes("utf-8");
        Cipher instance = Cipher.getInstance("RSA/None/PKCS1Padding");
        instance.init(1, publicKey);
        int length = bytes.length;
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        int i = 0;
        int i2 = 0;
        while (true) {
            int i3 = length - i;
            if (i3 > 0) {
                if (i3 > 117) {
                    bArr = instance.doFinal(bytes, i, 117);
                } else {
                    bArr = instance.doFinal(bytes, i, i3);
                }
                byteArrayOutputStream.write(bArr, 0, bArr.length);
                i2++;
                i = i2 * 117;
            } else {
                byte[] byteArray = byteArrayOutputStream.toByteArray();
                byteArrayOutputStream.close();
                return MyBase64.m12900a(byteArray);
            }
        }
    }

    public static String a(String str, PublicKey publicKey) throws Exception {
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
                return f.a.a.a.a.a.h.a(byteArray);
            }
        }
    }


/* renamed from: a */
public static String m12900a(byte[] bArr) throws Exception {
        int length = bArr.length;
        int i = (length * 4) / 3;
        byte[] bArr2 = new byte[((length % 3 > 0 ? 4 : 0) + i + (i / 76))];
        int i2 = length - 2;
        int i3 = 0;
        int i4 = 0;
        int i5 = 0;
        while (i3 < i2) {
            m12902a(bArr, i3 + 0, 3, bArr2, i4);
            i5 += 4;
            if (i5 == 76) {
                bArr2[i4 + 4] = 10;
                i4++;
                i5 = 0;
            }
            i3 += 3;
            i4 += 4;
        }
        if (i3 < length) {
            m12902a(bArr, 0 + i3, length - i3, bArr2, i4);
            i4 += 4;
        }
        return new String(bArr2, 0, i4, "iso-8859-1");
    }

    public static String a(byte[] bArr) throws Exception {
        int length = bArr.length;
        int i2 = (length * 4) / 3;
        byte[] bArr2 = new byte[((length % 3 > 0 ? 4 : 0) + i2 + (i2 / 76))];
        int i3 = length - 2;
        int i4 = 0;
        int i5 = 0;
        int i6 = 0;
        while (i4 < i3) {
            a(bArr, i4 + 0, 3, bArr2, i5);
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


/* renamed from: a */
public static byte[] m12902a(byte[] bArr, int i, int i2, byte[] bArr2, int i3) {
        int i4 = 0;
        int i5 = (i2 > 0 ? (bArr[i] << 24) >>> 8 : 0) | (i2 > 1 ? (bArr[i + 1] << 24) >>> 16 : 0);
        if (i2 > 2) {
            i4 = (bArr[i + 2] << 24) >>> 24;
        }
        int i6 = i5 | i4;
        if (i2 == 1) {
            byte[] bArr3 = f14736a;
            bArr2[i3] = bArr3[i6 >>> 18];
            bArr2[i3 + 1] = bArr3[(i6 >>> 12) & 63];
            bArr2[i3 + 2] = 61;
            bArr2[i3 + 3] = 61;
            return bArr2;
        } else if (i2 == 2) {
            byte[] bArr4 = f14736a;
            bArr2[i3] = bArr4[i6 >>> 18];
            bArr2[i3 + 1] = bArr4[(i6 >>> 12) & 63];
            bArr2[i3 + 2] = bArr4[(i6 >>> 6) & 63];
            bArr2[i3 + 3] = 61;
            return bArr2;
        } else if (i2 != 3) {
            return bArr2;
        } else {
            byte[] bArr5 = f14736a;
            bArr2[i3] = bArr5[i6 >>> 18];
            bArr2[i3 + 1] = bArr5[(i6 >>> 12) & 63];
            bArr2[i3 + 2] = bArr5[(i6 >>> 6) & 63];
            bArr2[i3 + 3] = bArr5[i6 & 63];
            return bArr2;
        }
    }

    public static byte[] a(byte[] bArr, int i2, int i3, byte[] bArr2, int i4) {
        int i5 = 0;
        int i6 = (i3 > 0 ? (bArr[i2] << 24) >>> 8 : 0) | (i3 > 1 ? (bArr[i2 + 1] << 24) >>> 16 : 0);
        if (i3 > 2) {
            i5 = (bArr[i2 + 2] << 24) >>> 24;
        }
        int i7 = i6 | i5;
        if (i3 == 1) {
            byte[] bArr3 = f11241a;
            bArr2[i4] = bArr3[i7 >>> 18];
            bArr2[i4 + 1] = bArr3[(i7 >>> 12) & 63];
            bArr2[i4 + 2] = 61;
            bArr2[i4 + 3] = 61;
            return bArr2;
        } else if (i3 == 2) {
            byte[] bArr4 = f11241a;
            bArr2[i4] = bArr4[i7 >>> 18];
            bArr2[i4 + 1] = bArr4[(i7 >>> 12) & 63];
            bArr2[i4 + 2] = bArr4[(i7 >>> 6) & 63];
            bArr2[i4 + 3] = 61;
            return bArr2;
        } else if (i3 != 3) {
            return bArr2;
        } else {
            byte[] bArr5 = f11241a;
            bArr2[i4] = bArr5[i7 >>> 18];
            bArr2[i4 + 1] = bArr5[(i7 >>> 12) & 63];
            bArr2[i4 + 2] = bArr5[(i7 >>> 6) & 63];
            bArr2[i4 + 3] = bArr5[i7 & 63];
            return bArr2;
        }
    }


public static final byte[] f14736a = {65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 43, 47};

    public static final byte[] f11241a = {65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 43, 47};


“”“
case_list 首页
******************************************************************************
*** obj值(Object): ***
{"a":"8.0","b":{"a":"65493","actionType":"1.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"","d":"","e":"","f":"","g":"应用案例","h":"","i":"","j":"","k":"","l":"推荐","m":"desc","n":"1","o":"10","r":"","strTime":"1652084926437"}}
*** str值(String): ***
{"a":"8.0","b":{"a":"65493","actionType":"1.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"","d":"","e":"","f":"","g":"应用案例","h":"","i":"","j":"","k":"","l":"推荐","m":"desc","n":"1","o":"10","r":"","strTime":"1652084926437"}}
*** publicKey值(Object): ***
{"algorithm":"RSA","encoded":[48,-127,-97,48,13,6,9,42,-122,72,-122,-9,13,1,1,1,5,0,3,-127,-115,0,48,-127,-119,2,-127,-127,0,-96,85,93,-106,-103,5,95,45,74,-124,-127,121,-100,74,30,-115,-47,-34,86,90,51,-115,-102,35,118,81,5,-16,-56,0,-36,-76,32,65,12,31,62,-21,76,-40,-88,127,112,-90,-116,97,33,124,78,59,33,115,-81,-111,-13,29,-94,-119,-121,109,-87,106,79,-64,64,16,-86,-69,78,-113,57,-88,-63,7,115,91,-2,-45,-19,-1,49,-34,-108,-4,-83,74,32,29,110,-121,-104,-38,52,108,91,74,-32,14,34,-112,-41,-30,68,12,81,-30,-5,35,22,-18,87,92,-78,-120,41,-78,97,33,-83,73,28,-72,78,15,-50,-96,-104,-107,2,3,1,0,1],"format":"X.509","modulus":112589984008212718692705259193944372249782211112088510987075898768994940950434990803948711201570710932916881147902507799109684598069324212146298434886616356316597578161839553557185767404108919194503230088104598642071102679172856797188445394861990619673071701814921024243375551997130470844682603957499090475157,"publicExponent":65537}
*** 返回值(String): ***
S8d65rqjWMwyJfdNEykgUMVmF899Ulc1poyrTIEFjovBYoYhdZLeHHV04R45kHGY2plpcTUjrUCV
o0N5BJwTNz7bIjXbPNshKjfegg3fJb3qI5eU/HbJYlJ1+Ttqne3+PNInYHRXIgt3JsxaHKERwZYs
4E+kQixYoQ4oBsD3Q1kQWq8pGmuoaE9FzssYCU8/JxqfA0Kw1ZK4s9G/YbUY1WSJKjamFm6Ynax4
OnPFR/ckAyg07q7gDqlMedesO33O1O8retPRWGfnHexqGPkQ5kRU8B9pgUvyLev/LYQi98NoDFpU
VDsa34eY0zoO8OzImaGNz7SVC1Dgwt5BBoIkNJ6JR8z345J18BKaSGxJdg7nPP0ExRGMBNayWfj/
fB30qAcuFrAy9ROwPL9HKy/Ta8CB83zWzohTRZ/XoYrh/ezwJLe2KQukguPmGHt8F0J0sy+nLKoM
8zHMFQ2ybGxmNLLtPz1RV/jgyzptJfr7dD7HGjeMelxM6k6xJ5KXBFX2
******************************************************************************
*** 返回值: ***
S8d65rqjWMwyJfdNEykgUMVmF899Ulc1poyrTIEFjovBYoYhdZLeHHV04R45kHGY2plpcTUjrUCV%0Ao0N5BJwTNz7bIjXbPNshKjfegg3fJb3qI5eU%2FHbJYlJ1%2BTtqne3%2BPNInYHRXIgt3JsxaHKERwZYs%0A4E%2BkQixYoQ4oBsD3Q1kQWq8pGmuoaE9FzssYCU8%2FJxqfA0Kw1ZK4s9G%2FYbUY1WSJKjamFm6Ynax4%0AOnPFR%2FckAyg07q7gDqlMedesO33O1O8retPRWGfnHexqGPkQ5kRU8B9pgUvyLev%2FLYQi98NoDFpU%0AVDsa34eY0zoO8OzImaGNz7SVC1Dgwt5BBoIkNJ6JR8z345J18BKaSGxJdg7nPP0ExRGMBNayWfj%2F%0AfB30qAcuFrAy9ROwPL9HKy%2FTa8CB83zWzohTRZ%2FXoYrh%2FezwJLe2KQukguPmGHt8F0J0sy%2BnLKoM%0A8zHMFQ2ybGxmNLLtPz1RV%2FjgyzptJfr7dD7HGjeMelxM6k6xJ5KXBFX2
******************************************************************************
”“”

“”“
case_lsit  翻页
******************************************************************************
*** obj值(Object): ***
{"a":"8.0","b":{"a":"65493","actionType":"1.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"","d":"","e":"","f":"","g":"应用案例","h":"","i":"","j":"","k":"","l":"推荐","m":"desc","n":"2","o":"10","r":"","strTime":"1652086302020"}}
*** str值(String): ***
{"a":"8.0","b":{"a":"65493","actionType":"1.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"","d":"","e":"","f":"","g":"应用案例","h":"","i":"","j":"","k":"","l":"推荐","m":"desc","n":"2","o":"10","r":"","strTime":"1652086302020"}}
*** publicKey值(Object): ***
{"algorithm":"RSA","encoded":[48,-127,-97,48,13,6,9,42,-122,72,-122,-9,13,1,1,1,5,0,3,-127,-115,0,48,-127,-119,2,-127,-127,0,-96,85,93,-106,-103,5,95,45,74,-124,-127,121,-100,74,30,-115,-47,-34,86,90,51,-115,-102,35,118,81,5,-16,-56,0,-36,-76,32,65,12,31,62,-21,76,-40,-88,127,112,-90,-116,97,33,124,78,59,33,115,-81,-111,-13,29,-94,-119,-121,109,-87,106,79,-64,64,16,-86,-69,78,-113,57,-88,-63,7,115,91,-2,-45,-19,-1,49,-34,-108,-4,-83,74,32,29,110,-121,-104,-38,52,108,91,74,-32,14,34,-112,-41,-30,68,12,81,-30,-5,35,22,-18,87,92,-78,-120,41,-78,97,33,-83,73,28,-72,78,15,-50,-96,-104,-107,2,3,1,0,1],"format":"X.509","modulus":112589984008212718692705259193944372249782211112088510987075898768994940950434990803948711201570710932916881147902507799109684598069324212146298434886616356316597578161839553557185767404108919194503230088104598642071102679172856797188445394861990619673071701814921024243375551997130470844682603957499090475157,"publicExponent":65537}
*** 返回值(String): ***
nqWt2+r3EvZpeyZcCyrL5+ggjc2UUKLNdwf5UrCiL0T13w1Spif4DnrDAVp34xTZt5igSCx74m3N
iiKd9wm5L+gdv4rAKs7upzbMcGQQ81GpwS0O3Dv5cdR+7UEgQoGnIQkQwGTQRmA/QwVL29sedTk5
GpObiDBzQsbr+mUF3ZMbHm0T1UAvdXzhOCP/25nWxx7BxVuTRD3/Kh/F+0+9+gg8xeCwmx8hxNnt
45SXgVkNeglfVptiubXAhlU6cch3geu3EMt5iIuw7Yk4QIqvzBUgd7RX7AzkQc1bL1Agah97nWwC
yvEjprkeT1kefYz382dyUzR1vMYVLc+UzQZwawoL/qwVzLKZVfIHv8zaVQdZAda32h88jl/RIOZ2
HnRTzNXTJZHUTQ1rJ3hMAEDemv+ZJRo1tG9+fgeoQxFHlcEXpnm4In/KBeXrQrIJTM+p8LGl5Xfc
qQfxuePZrgEIetAULtJcnTds3y/ZnXKadjj6QKyFfKCpyg6cgUMwDx5c
******************************************************************************
*** 返回值: ***
nqWt2%2Br3EvZpeyZcCyrL5%2Bggjc2UUKLNdwf5UrCiL0T13w1Spif4DnrDAVp34xTZt5igSCx74m3N%0AiiKd9wm5L%2Bgdv4rAKs7upzbMcGQQ81GpwS0O3Dv5cdR%2B7UEgQoGnIQkQwGTQRmA%2FQwVL29sedTk5%0AGpObiDBzQsbr%2BmUF3ZMbHm0T1UAvdXzhOCP%2F25nWxx7BxVuTRD3%2FKh%2FF%2B0%2B9%2Bgg8xeCwmx8hxNnt%0A45SXgVkNeglfVptiubXAhlU6cch3geu3EMt5iIuw7Yk4QIqvzBUgd7RX7AzkQc1bL1Agah97nWwC%0AyvEjprkeT1kefYz382dyUzR1vMYVLc%2BUzQZwawoL%2FqwVzLKZVfIHv8zaVQdZAda32h88jl%2FRIOZ2%0AHnRTzNXTJZHUTQ1rJ3hMAEDemv%2BZJRo1tG9%2BfgeoQxFHlcEXpnm4In%2FKBeXrQrIJTM%2Bp8LGl5Xfc%0AqQfxuePZrgEIetAULtJcnTds3y%2FZnXKadjj6QKyFfKCpyg6cgUMwDx5c
******************************************************************************
”“”


“”“
case详情
******************************************************************************
*** obj值(Object): ***
{"a":"8.0","b":{"a":"65493","actionType":"3.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"2412","d":"1","strTime":"1652084974592"}}
*** str值(String): ***
{"a":"8.0","b":{"a":"65493","actionType":"3.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"2412","d":"1","strTime":"1652084974592"}}
*** publicKey值(Object): ***
{"algorithm":"RSA","encoded":[48,-127,-97,48,13,6,9,42,-122,72,-122,-9,13,1,1,1,5,0,3,-127,-115,0,48,-127,-119,2,-127,-127,0,-96,85,93,-106,-103,5,95,45,74,-124,-127,121,-100,74,30,-115,-47,-34,86,90,51,-115,-102,35,118,81,5,-16,-56,0,-36,-76,32,65,12,31,62,-21,76,-40,-88,127,112,-90,-116,97,33,124,78,59,33,115,-81,-111,-13,29,-94,-119,-121,109,-87,106,79,-64,64,16,-86,-69,78,-113,57,-88,-63,7,115,91,-2,-45,-19,-1,49,-34,-108,-4,-83,74,32,29,110,-121,-104,-38,52,108,91,74,-32,14,34,-112,-41,-30,68,12,81,-30,-5,35,22,-18,87,92,-78,-120,41,-78,97,33,-83,73,28,-72,78,15,-50,-96,-104,-107,2,3,1,0,1],"format":"X.509","modulus":112589984008212718692705259193944372249782211112088510987075898768994940950434990803948711201570710932916881147902507799109684598069324212146298434886616356316597578161839553557185767404108919194503230088104598642071102679172856797188445394861990619673071701814921024243375551997130470844682603957499090475157,"publicExponent":65537}
*** 返回值(String): ***
egTzxb+djnk8sXjoyOJGJufg2kQqPR5TDmMizGlUBNOSJPvnOXLlxF9ihbUETiaYTpqecN8tQszz\ndgI8bQhzzfxKwDBabSadGclds/N50YgRfkZYeBxiNQ7qux0lhP2SyM1dJyMjF+9G6XXqU16sGcTn\nyuVxpsWksxdWdAJlpZ4P30YfQRk1nKV94Xb+aMbrL66g5fMSXwaKeYVS1t4WTHza+txqovqq1wcQ\nQaiihjBtelvRqwVFq8JDlQ0HbEwzNrbtqszssKr42mxhJvLDf7eEfekEUmwfkbGBpZV0yD+SstK2\njWCukcTGtVJK5dVMib48hQ+zRkOoHGvG4atxFA==
******************************************************************************
*** 返回值: ***
egTzxb%2Bdjnk8sXjoyOJGJufg2kQqPR5TDmMizGlUBNOSJPvnOXLlxF9ihbUETiaYTpqecN8tQszz%0AdgI8bQhzzfxKwDBabSadGclds%2FN50YgRfkZYeBxiNQ7qux0lhP2SyM1dJyMjF%2B9G6XXqU16sGcTn%0AyuVxpsWksxdWdAJlpZ4P30YfQRk1nKV94Xb%2BaMbrL66g5fMSXwaKeYVS1t4WTHza%2Btxqovqq1wcQ%0AQaiihjBtelvRqwVFq8JDlQ0HbEwzNrbtqszssKr42mxhJvLDf7eEfekEUmwfkbGBpZV0yD%2BSstK2%0AjWCukcTGtVJK5dVMib48hQ%2BzRkOoHGvG4atxFA%3D%3D
******************************************************************************
”“”


“”“
下载案例
******************************************************************************
*** obj值(Object): ***
{"a":"5.0","b":{"a":"65493","actionType":"7.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"2739","strTime":"1652086356571"}}
*** str值(String): ***
{"a":"5.0","b":{"a":"65493","actionType":"7.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"2739","strTime":"1652086356571"}}
*** publicKey值(Object): ***
{"algorithm":"RSA","encoded":[48,-127,-97,48,13,6,9,42,-122,72,-122,-9,13,1,1,1,5,0,3,-127,-115,0,48,-127,-119,2,-127,-127,0,-96,85,93,-106,-103,5,95,45,74,-124,-127,121,-100,74,30,-115,-47,-34,86,90,51,-115,-102,35,118,81,5,-16,-56,0,-36,-76,32,65,12,31,62,-21,76,-40,-88,127,112,-90,-116,97,33,124,78,59,33,115,-81,-111,-13,29,-94,-119,-121,109,-87,106,79,-64,64,16,-86,-69,78,-113,57,-88,-63,7,115,91,-2,-45,-19,-1,49,-34,-108,-4,-83,74,32,29,110,-121,-104,-38,52,108,91,74,-32,14,34,-112,-41,-30,68,12,81,-30,-5,35,22,-18,87,92,-78,-120,41,-78,97,33,-83,73,28,-72,78,15,-50,-96,-104,-107,2,3,1,0,1],"format":"X.509","modulus":112589984008212718692705259193944372249782211112088510987075898768994940950434990803948711201570710932916881147902507799109684598069324212146298434886616356316597578161839553557185767404108919194503230088104598642071102679172856797188445394861990619673071701814921024243375551997130470844682603957499090475157,"publicExponent":65537}
*** 返回值(String): ***
l7wNhOAvJxD9DRUhiSTRiW7lw254wTyuNbNw8wBsonl7G28H/eV9uPE+VKqhvuLzbLWGVPIuHl1I
nHb3XmqNxmkeXvOEcoHXRhPqokA5B+mCgDRCB6mUACPzOVJV9OakNFHeVGhz7Ov7lySoYezZpZNt
VfRd93mDxVtLTowng+V1U9dHHuZhlCZtfR5vC1QPwrT/5IJa1DOnXaOnPoYlBcQ39vAM5TFEPWrV
wDjXjAqN96bevtvoAdz1Z+9Umei0kbi+j2CnphNtiQgWzZimEsXDz+iZTZGqTzugAHjmSdE1bF42
Yte6EwBR4LB/poYyAj+6BxcXEGWhdipVzKa3vg==
******************************************************************************
*** 返回值: ***
l7wNhOAvJxD9DRUhiSTRiW7lw254wTyuNbNw8wBsonl7G28H%2FeV9uPE%2BVKqhvuLzbLWGVPIuHl1I%0AnHb3XmqNxmkeXvOEcoHXRhPqokA5B%2BmCgDRCB6mUACPzOVJV9OakNFHeVGhz7Ov7lySoYezZpZNt%0AVfRd93mDxVtLTowng%2BV1U9dHHuZhlCZtfR5vC1QPwrT%2F5IJa1DOnXaOnPoYlBcQ39vAM5TFEPWrV%0AwDjXjAqN96bevtvoAdz1Z%2B9Umei0kbi%2Bj2CnphNtiQgWzZimEsXDz%2BiZTZGqTzugAHjmSdE1bF42%0AYte6EwBR4LB%2FpoYyAj%2B6BxcXEGWhdipVzKa3vg%3D%3D
******************************************************************************
”“”

"a": {
        "infoId": 0,
        "infoName": "获取文件成功"
    },
    "b": {
        "a": "https://slfiles.soliao.com/soliao/case/other/ab0121e292fc43c4983048789c9db9ed.pdf",
        "b": "搜料网-案例-智能手机天线部件.pdf"
    }
}