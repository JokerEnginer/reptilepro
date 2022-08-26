# 1 . 找到未加密的参数
# 2. 想办法把参数进行加密（必须参考网易的逻辑），params==>encText， encSeckey==>encSecKey
# (windows.asrsea()
# 3 .请求到网易，拿到评论信息

from Crypto.Cipher import AES
from base64 import b64encode
import requests
import json
url = 'https://music.163.com/weapi/comment/resource/comments/get'
# 请求方式post

data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1973027248",
    "threadId": "R_SO_4_1973027248"
}
e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
i = "QXyoIzDpu6TktI0o"

def get_encSecKey():
    return '"c72f8a786e4d477871dc643519d0f9a203a1ca1d448b624ea30faa32f97b81d03eac4ee43692ab264f62218affb0b2fe2e711bc66ab0bbe925200b695cab0660396ccb276ce735223692f4bf7b47f2b38bacbea25b94c6de9a022c8eb959df9974df9f3d624c46d98087d7953812caf00a327c7150e88db86371a5cf544cd063"'

def get_params(data):
    first = enc_params(data,g)
    second = enc_params(first,i)
    return second

def to16(data):
    pad = 16-len(data)%16
    data += chr(pad)*pad
    return data

def enc_params(data,key): # 加密过程
    iv = '0102030405060708'
    data = to16(data)
    aes = AES.new(key=key.encode('utf-8'),IV=iv.encode('utf-8'),mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode('utf-8'))
    return str(b64encode(bs))

resp = requests.post(url=url, data={
    "params":json.dumps(data),
    "encSecKey":get_encSecKey()
})

print(resp.text)













'''
function a(a) { # a=16
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)   # 循环16次
            e = Math.random() * b.length,  # 得到随机数
            e = Math.floor(e),              # 随机数取整
            c += b.charAt(e);               # 得到字符串，
        return c # 返回长度为16的字符串
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
'''





