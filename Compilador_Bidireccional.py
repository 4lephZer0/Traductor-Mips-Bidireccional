



def Rtipe_separator():

    lista_bin.append(binstr[0:5])
    lista_bin.append(binstr[5:10])
    lista_bin.append(binstr[10:15])
    lista_bin.append(binstr[15:20])
    lista_bin.append(binstr[20:26])
    

def Itipe_separator():

    lista_bin.append(binstr[0:5])
    lista_bin.append(binstr[5:10])
    lista_bin.append(binstr[10:26])

def Jtipe_separator():

    lista_bin.append(binstr[0:26])

def Rtipe_Func():

    inst = ""    
    inst = inst + list_Rfunct[int(lista_bin[5], 2)]
    
    if (inst == "jr "):
        
        inst = inst + register_list[int(lista_bin[1], 2)]
        
    elif ((inst == "sll ") or (inst == "srl ") or (inst == "sra ")):
        
        inst = inst + register_list[int(lista_bin[3], 2)] + ", " + register_list[int(lista_bin[2], 2)] + ", " + int(lista_bin[4], 2)
        
    elif ((inst == "mfhi ") or (inst == "mflo ")):
        
        inst = inst + register_list[int(lista_bin[3], 2)]
        
    elif ((inst == "div ") or (inst == "divu ") or (inst == "mult ") or (inst == "multu ")):
        
        inst = inst + register_list[int(lista_bin[1], 2)] + ", " + register_list[int(lista_bin[2], 2)]
        
    else:
        
        inst = inst + register_list[int(lista_bin[3], 2)] + ", " + register_list[int(lista_bin[1], 2)] + ", " + register_list[int(lista_bin[2], 2)]

    return inst

inicial = "0x00851020"

lista_bin = []

list_Rfunct = ["sll ", "", "srl ", "sra ", "", "", "", "", "jr ", "", "", "", "", "", "", "", "mfhi ", "", "mflo ", "", "", "", "",
               "", "mult ", "multu ", "div ", "divu ", "", "", "", "", "add ", "addu ", "sub ", "subu ", "and ", "or ", "", "nor ", "", "", "slt ", "sltu "]

register_list = ["$zero", "$at", "$v0", "$v1", "$a0", "$a1", "$a2", "$a3", "$t0", "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7"
                , "$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7", "$t8", "$t9", "$k0", "$k1", "$gp", "$sp", "$fp", "$ra"]
binstr = ""

print ("\nInicial:", inicial)
inicial = inicial[2:]

for i in range (0,4):

    resultado = str("{0:08b}".format(int(inicial[0:2], 16)))
    binstr = binstr + resultado
    inicial = inicial[2:]

lista_bin.append(binstr[0:6])
binstr = binstr[6:]

if (lista_bin[0] == "000000"):
    Rtipe_separator()
    print("\nInstruccion:", Rtipe_Func(), "\n")


elif((lista_bin[0] == "000010") or (lista_bin[0] == "000011")):
    Jtipe_separator()

else:
    Itipe_separator()