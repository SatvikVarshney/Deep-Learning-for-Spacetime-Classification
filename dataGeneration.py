import random
import numpy as np
import csv

def WeylGeneration(sampleVec):
    weyl = [0,0,0,0,0]
    for i in range(0,5):
        if sampleVec[i] == 'N':
            weyl[i] = (random.randint(0,20)) - 10
            while weyl[i] == 0:
                weyl[i] = (random.randint(0,20)) - 10
    return weyl

def QuarticLabeling(weyl):

    w0 = weyl[4]
    w1 = -weyl[3]
    w2 = weyl[2]
    w3 = -weyl[1]
    w4 = weyl[0]

    test = [w0,-4*w1,6*w2,-4*w3,w4]

    if w0 == 0:
        w0 = w4
        w4 = 0
        w1temp = w1
        w1 = w3
        w3 = w1temp

    i = w0*w4 - 4*w1*w3 + 3*w2**2
    j = w0*(w2*w4 - w3*w3) - w1*(w1*w4 - w2*w3) + w2*(w1*w3 - w2*w2)
    g = w0**2*w3 - 3*w0*w1*w2 + 2*w1**3
    h = w0*w2 - w1**2

    if i**3 == 27*j**2:
        if i == j and i == 0:
            if g == h and g == 0:
                #print(test,'N')
                weyl.append('N')
            else:
                #print(test,'III')
                weyl.append('III')
        else:
            gtest = w0**2*i - 12*h**2
            if g == gtest and g ==0:
                #print(test,'D')
                weyl.append('D')
            else:
                #print(test,'II')
                weyl.append('II')
    else:
        #print(test,'I')
        weyl.append('I')
    return weyl

def GeneratePerSample(sampleVec,iterations,writer):
    ocnt = 0
    icnt = 0
    iicnt = 0
    iiicnt = 0
    ncnt = 0
    dcnt = 0

    state0 = ['00000']
    stateI = ['0N00N','N00N0','0N0N0','N000N']
    stateII = ['00N0N','N0N00','00NN0','0NN00']
    stateIII = ['0N000','000N0','NN000','000NN']
    stateN = ['N0000','0000N']
    stateD = ['00N00']

    i = 0
    while i < iterations:
        i += 1 
        weyl = WeylGeneration([*sampleVec])
        if sampleVec in state0:
            ocnt += 1
            weyl.append('O')
            writer.writerow(weyl)
        elif sampleVec in stateI:
            icnt += 1
            weyl.append('I')
            writer.writerow(weyl)
        elif sampleVec in stateII:
            iicnt += 1
            weyl.append("II")
            writer.writerow(weyl)
        elif sampleVec in stateIII:
            iiicnt += 1
            weyl.append("III")
            writer.writerow(weyl)
        elif sampleVec in stateN:
            ncnt += 1
            weyl.append("N")
            writer.writerow(weyl)
        elif sampleVec in stateD:
            dcnt += 1
            weyl.append("D")
            writer.writerow(weyl)
        else:
            weyl = QuarticLabeling(weyl)
            
            if weyl[5] == 'I':
                icnt += 1
                if icnt < 7500:
                    writer.writerow(weyl)
                else:
                    i -= 1
                    icnt -= 1
            elif weyl[5] == 'II':
                iicnt += 1
                writer.writerow(weyl)
            elif weyl[5] == 'III':
                iiicnt += 1
                writer.writerow(weyl)
            elif weyl[5] == 'N':
                ncnt += 1
                writer.writerow(weyl)
            else:
                dcnt += 1
                writer.writerow(weyl)

        
    print("O:",ocnt,",I:",icnt,",II:",iicnt,",III:",iiicnt,",N:",ncnt,",D:",dcnt)
    return [ocnt,icnt,iicnt,iiicnt,ncnt,dcnt]

def SingleFile(fileName,path,states):
    fileExt = '.csv'
    otot = 0
    itot = 0
    iitot = 0
    iiitot = 0
    ntot = 0
    dtot = 0
    with open(path+fileName+fileExt,'w',newline='') as f:
        writer = csv.writer(f)
        i = 0
        for state in states:
            i += 1
            amt = GeneratePerSample(state[0],state[1],writer)
            otot += amt[0]
            itot += amt[1]
            iitot += amt[2]
            iiitot += amt[3]
            ntot += amt[4]
            dtot += amt[5]
    print("O:",otot,",I:",itot,",II:",iitot,",III:",iiitot,",N:",ntot,",D:",dtot)
    print(otot + itot + iitot + iiitot + ntot + dtot)

def MultiFile(path,states):
    fileExt = '.csv'
    otot = 0
    itot = 0
    iitot = 0
    iiitot = 0
    ntot = 0
    dtot = 0
    for state in states:
        with open(path+state[0]+fileExt,'w',newline='') as f:
            writer = csv.writer(f)
            amt = GeneratePerSample(state[0],state[1],writer)
            otot += amt[0]
            itot += amt[1]
            iitot += amt[2]
            iiitot += amt[3]
            ntot += amt[4]
            dtot += amt[5]
    
    print("O:",otot,",I:",itot,",II:",iitot,",III:",iiitot,",N:",ntot,",D:",dtot)

zeroCutOff = 0.0001
states = [['00000',10000],['N0000',10000],['0000N',10000],['00N00',10000],['0N000',10000],['000N0',10000],['NN000',10000],['000NN',10000],\
        ['00N0N',10000],['N0N00',10000],['00NN0',10000],['0NN00',10000],['0N00N',10000],['N00N0',10000],['0N0N0',10000],['N000N',10000],\
        ['00NNN',10000],['NNN00',10000],['N0N0N',10000],['0N0NN',10000],['NN0N0',10000],['N00NN',10000],['NN00N',10000],['0NN0N',10000],\
        ['N0NN0',10000],['0NNN0',10000],['0NNNN',10000],['NNNN0',10000],['N0NNN',10000],['NNN0N',10000],['NN0NN',10000],['NNNNN',20000]]
fileExt = '.csv'
fileName = 'SingleFile'
path = 'E:\Documents\Fall 2022\PHYS 449\Final\\'

SingleFile(fileName,path,states)
