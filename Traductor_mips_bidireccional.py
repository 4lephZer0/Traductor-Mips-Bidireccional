
def Rtipe_separator():

    list_bin.append(binstr[0:5])
    list_bin.append(binstr[5:10])
    list_bin.append(binstr[10:15])
    list_bin.append(binstr[15:20])
    list_bin.append(binstr[20:26]) 

def Itipe_separator():

    list_bin.append(binstr[0:5])
    list_bin.append(binstr[5:10])
    list_bin.append(binstr[10:26])

def Jtipe_separator():

    list_bin.append(binstr[0:26])

def Rtipe_Func():

    inst = ""    
    inst = inst + list_Rfunct[int(list_bin[5], 2)] + " "
    
    if (inst == "jr"):  
        inst = inst + register_list[int(list_bin[1], 2)]
        
    elif ((inst == "sll") or (inst == "srl") or (inst == "sra")):  
        inst = inst + register_list[int(list_bin[3], 2)] + ", " + register_list[int(list_bin[2], 2)] + ", " + int(list_bin[4], 2)
        
    elif ((inst == "mfhi") or (inst == "mflo")):
        inst = inst + register_list[int(list_bin[3], 2)]
        
    elif ((inst == "div") or (inst == "divu") or (inst == "mult") or (inst == "multu")):
        inst = inst + register_list[int(list_bin[1], 2)] + ", " + register_list[int(list_bin[2], 2)]
        
    else:
        inst = inst + register_list[int(list_bin[3], 2)] + ", " + register_list[int(list_bin[1], 2)] + ", " + register_list[int(list_bin[2], 2)]

    return inst

def Itipe_Func():
    
    inst = ""    
    inst = inst + list_JandI_funct[int(list_bin[0], 2)] + " "
    
    if (inst == "lui"):
        inst = inst + register_list[int(list_bin[2], 2)] + ", " + hex(int(list_bin[3], 2))
        
    elif (list_JandI_funct.index(inst) > 31):
        inst = inst + register_list[int(list_bin[2], 2)] + ", " + hex(int(list_bin[3], 2)) + "(" + register_list[int(list_bin[1], 2)] + ")"
        
    elif ((list_JandI_funct.index(inst) > 7) and (list_JandI_funct.index(inst) < 15)):
        inst = inst + register_list[int(list_bin[2], 2)] + ", " + register_list[int(list_bin[1], 2)] + ", " + hex(int(list_bin[3], 2))
        
    elif ((list_JandI_funct.index(inst) > 3) and (list_JandI_funct.index(inst) < 8)):
        inst = inst + register_list[int(list_bin[1], 2)] + ", " + register_list[int(list_bin[2], 2)] + ", LABEL"
        
    return inst

def Jtipe_Func():
    
    inst = ""    
    inst = inst + list_JandI_funct[int(list_bin[0], 2)] + " LABEL"
            
    return inst 

def MFC0tipe_Func():
    
    inst = ""    
    inst = inst + "mfc0 " + register_list[int(list_bin[3], 2)] + ", " + register_list[int(list_bin[1], 2)]
            
    return inst 

def RfunctoHex():
    
    out_hex = ""
    out_hex = out_hex + "000000"

    
    if (list_inst[0] == "jr"):
        out_hex = out_hex + ZeroExtend(str(bin(register_list.index(list_inst[1])))[2:], 5)
        out_hex = out_hex + "000000000000000"
        out_hex = out_hex + ZeroExtend(str(bin(list_Rfunct.index(list_inst[0])))[2:], 6)
        
        
    elif ((list_inst[0] == "sll") or (list_inst[0] == "srl ") or (list_inst[0] == "sra ")):
        
        out_hex = out_hex + "00000"
        out_hex = out_hex + ZeroExtend(str(bin(register_list.index(list_inst[1])))[2:], 5)
        out_hex = out_hex + ZeroExtend(str(bin(register_list.index(list_inst[2])))[2:], 5)
        out_hex = out_hex + ZeroExtend(str(bin(register_list.index(list_inst[3])))[2:], 5)
        out_hex = out_hex + ZeroExtend(str(bin(list_Rfunct.index(list_inst[0])))[2:], 6)
        
    elif ((list_inst[0] == "mfhi") or (list_inst[0] == "mflo")):
        
        out_hex = out_hex + "0000000000"
        out_hex = out_hex + ZeroExtend(str(bin(register_list.index(list_inst[1])))[2:], 5)
        out_hex = out_hex + "00000"
        out_hex = out_hex + ZeroExtend(str(bin(list_Rfunct.index(list_inst[0])))[2:], 6)
        
        
    elif ((list_inst[0] == "div") or (list_inst[0] == "divu") or (list_inst[0] == "mult") or (list_inst[0] == "multu")):
        
        out_hex = out_hex + ZeroExtend(str(bin(register_list.index(list_inst[1])))[2:], 5)
        out_hex = out_hex + ZeroExtend(str(bin(register_list.index(list_inst[2])))[2:], 5)
        out_hex = out_hex + "0000000000"
        out_hex = out_hex + ZeroExtend(str(bin(list_Rfunct.index(list_inst[0])))[2:], 6)
        
    else:
        
        out_hex = out_hex + ZeroExtend(str(bin(register_list.index(list_inst[2])))[2:], 5)
        out_hex = out_hex + ZeroExtend(str(bin(register_list.index(list_inst[3])))[2:], 5)
        out_hex = out_hex + ZeroExtend(str(bin(register_list.index(list_inst[1])))[2:], 5)
        out_hex = out_hex + "00000"
        out_hex = out_hex + ZeroExtend(str(bin(list_Rfunct.index(list_inst[0])))[2:], 6)
    
    List_aux_creator(out_hex, (len(out_hex)//4))  
    out_hex = ""
    
    for i in range(0, len(list_aux)):
        
        out_hex = out_hex + list_aux[i]
        
    out_hex = "0x" + out_hex
    
    return out_hex

def ZeroExtend(stringBin, bitsExtends):
    
    while (len(stringBin) < bitsExtends):
        
        stringBin = "0" + stringBin
        
    return stringBin
    
def List_aux_creator(out_hex, len_out_hex):
    
    for i in range(0,len_out_hex):
        
       list_aux.append(str(hex(int(out_hex[0:4], 2)))[2:])
       out_hex = out_hex[4:]
    
     
    

inicial = "add $t0, $s0, $s1"
final_hex = ""

list_bin = []
list_inst = []
list_aux =[]

list_Rfunct = ["sll", "", "srl", "sra", "sllv", "", "srlv", "srav", "jr", "jalr", "movz", "movn", "syscall", "break", "", "sync", "mfhi", "mthi",
               "mflo", "mtlo", "", "", "", "", "mult", "multu", "div", "divu", "", "", "", "", "add", "addu", "sub", "subu", "and", "or", "xor", "nor"
               , "", "", "slt", "sltu", "", "", "", "", "tge", "tgeu", "tlt", "tltu", "teq", "", "tne"]

list_JandI_funct = ["", "", "j", "jal", "beq", "bne", "blez", "bgtz", "addi", "addiu", "slti", "sltiu", "andi", "ori", "xori", "lui", "", "", "", "", "",
                    "", "", "", "", "", "", "", "", "", "", "", "lb", "lh" , "lwl", "lw", "lbu", "lhu", "lwr", "", "sb", "sh", "swl", "sw", "", "", "swr", 
                    "cache", "ll", "lwc1", "", "", "", "lwc2", "pref", "", "ldc1", "ldc2", "", "sc", "swc1", "swc2", "", "", "sdc1", "sdc2"]

register_list = ["$zero", "$at", "$v0", "$v1", "$a0", "$a1", "$a2", "$a3", "$t0", "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7"
                , "$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7", "$t8", "$t9", "$k0", "$k1", "$gp", "$sp", "$fp", "$ra"]

binstr = ""

caso = 1

if (caso == 0):
    
    print("\nInicio:", inicial)
    inicial = inicial[2:]

    for i in range (0,4):

        resultado = str("{0:08b}".format(int(inicial[0:2], 16)))
        binstr = binstr + resultado
        inicial = inicial[2:]

    list_bin.append(binstr[0:6])
    binstr = binstr[6:]

    if (list_bin[0] == "000000"):
        Rtipe_separator()
        salida = Rtipe_Func()

    elif((list_bin[0] == "000010") or (list_bin[0] == "000011")):
        Jtipe_separator()
        salida = Jtipe_Func()
            
    elif((list_bin[0] == "010000")):
        Rtipe_separator()
        salida = MFC0tipe_Func()
            
    else:
        Itipe_separator()
        salida = Itipe_Func()
        
    print("\nInstruccion:", salida, "\n")
    
if (caso == 1):
    
    print("\nInicio:", inicial)
    list_inst = inicial.split(" ")
    
    for i in range (0,len(list_inst)):
        
        list_inst[i] = list_inst[i].replace(",", "")
    
    if(list_inst[0] in list_Rfunct):
        
        final_hex = RfunctoHex()
        print("\nFinal:", final_hex, "\n")
    

print("Programa finalizado con Exito\n")