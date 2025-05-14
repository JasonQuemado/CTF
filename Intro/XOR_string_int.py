string = "label";
integer = 13;

int_string = [ord(i) for i in string];
#int_string = [bin(i)[2:] for i in int_string];
print(int_string);

#int_integer = bin(integer)[2:];
#int_integer = int_integer.zfill(len(int_string));

#final_int = [int(s) ^ int(i) for s, i in zip(int_string, int_integer)];
final_int = [s ^ integer for s in int_string]

print(f"Resultado de la operación XOR: {final_int}");

final_string = ''.join(chr(f) for f in final_int);

print(f"Cadena final: {final_string}");
