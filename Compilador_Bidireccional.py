
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

def Itipe_Func():
    
    inst = ""    
    inst = inst + list_JandI_funct[int(lista_bin[0], 2)]
    
    if (inst == "lui "):
        inst = inst + register_list[int(lista_bin[2], 2)] + ", " + hex(int(lista_bin[3], 2))
        
    elif (list_JandI_funct.index(inst) > 31):
        inst = inst + register_list[int(lista_bin[2], 2)] + ", " + hex(int(lista_bin[3], 2)) + "(" + register_list[int(lista_bin[1], 2)] + ")"
        
    elif ((list_JandI_funct.index(inst) > 7) and (list_JandI_funct.index(inst) < 15)):
        inst = inst + register_list[int(lista_bin[2], 2)] + ", " + register_list[int(lista_bin[1], 2)] + ", " + hex(int(lista_bin[3], 2))
        
    elif ((list_JandI_funct.index(inst) > 3) and (list_JandI_funct.index(inst) < 8)):
        inst = inst + register_list[int(lista_bin[1], 2)] + ", " + register_list[int(lista_bin[2], 2)] + ", LABEL"
        
    return inst

def Jtipe_Func():
    
    inst = ""    
    inst = inst + list_JandI_funct[int(lista_bin[0], 2)] + ", LABEL"
            
    return inst 

def MFC0tipe_Func():
    
    inst = ""    
    inst = inst + "mfc0 " + register_list[int(lista_bin[3], 2)] + ", " + register_list[int(lista_bin[1], 2)]
            
    return inst 


inicial = "0x11280006"

## 111000
lista_bin = []

list_Rfunct = ["sll ", "", "srl ", "sra ", "sllv ", "", "srlv ", "srav ", "jr ", "jalr ", "movz ", "movn ", "syscall ", "break ", "", "sync ", "mfhi ", "mthi ",
               "mflo ", "mtlo ", "", "", "", "", "mult ", "multu ", "div ", "divu ", "", "", "", "", "add ", "addu ", "sub ", "subu ", "and ", "or ", "xor ", "nor "
               , "", "", "slt ", "sltu ", "", "", "", "", "tge ", "tgeu ", "tlt ", "tltu ", "teq ", "", "tne "]

list_JandI_funct = ["", "", "j ", "jal ", "beq ", "bne ", "blez ", "bgtz ", "addi ", "addiu ", "slti ", "sltiu ", "andi ", "ori ", "xori ", "lui ", "", "", "", "", "",
                    "", "", "", "", "", "", "", "", "", "", "", "lb ", "lh" , "lwl ", "lw ", "lbu ", "lhu ", "lwr ", "", "sb ", "sh ", "swl ", "sw ", "", "", "swr ", 
                    "cache ", "ll ", "lwc1 ", "", "", "", "lwc2 ", "pref ", "", "ldc1 ", "ldc2 ", "", "sc", "swc1 ", "swc2 ", "", "", "sdc1 ", "sdc2 "]

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
    print("\nInstruccion:", Jtipe_Func(), "\n")
    
elif((lista_bin[0] == "010000")):
    Rtipe_separator()
    print("\nInstruccion:", MFC0tipe_Func(), "\n")
    
else:
    Itipe_separator()
    print("\nInstruccion:", Itipe_Func(), "\n")