KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY21 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY23 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FKEY132 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

def xor(s1,s2):
    if len(s1) != len(s2):
        raise "XOR EXCEPTION: Strings are not of equal length!"

    return ''.join(format(int(a, 16) ^ int(b, 16), 'x') for a,b in zip(s1,s2))


#KEY2 = xor(KEY21,KEY1);
#print(KEY2);

#KEY3 = xor(KEY23,KEY2);
#print(KEY3);

#aux = xor(KEY1,xor(KEY2,KEY3));
#print(aux);

flag = xor(FKEY132,xor(KEY1,KEY23));
flag = bytes.fromhex(flag);
print(flag);


#key1b = int(KEY1, 16);
#print(key1b);

#key21b = int(KEY21, 16);
#print(key21b);

#key23b = int(KEY23, 16);
#print(key23b);

#keyf123b = int(FKEY132, 16);
#print(keyf123b);
