import base64

string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

string2 = string[::-1];
ascii_string = bytes.fromhex(string);
base64_string = base64.b64encode(ascii_string);

print(base64_string);
