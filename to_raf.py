"""
The RAF file works for the DG4602.
powered by Polaris
"""
import numpy as np
import pylab as plt
import sys

def draw(signal):
    X = np.r_[0:len(signal)]
    plt.plot(X,signal)
    plt.show()
    return

def arb_to_raf(filename):
    infile = open(filename+'.arb')
    for i in range(8):
        temp = infile.readline()
        if i==6:
            point = int(temp.split(':')[1])
    signal = []
    for i in range(point):
        signal.append(float(infile.readline()))
    to_raf(signal,filename)
    infile.close()
    return

def txt_to_raf(filename):
    infile = open(filename+'.txt')
    signal = []
    for i in range(8):
        temp = infile.readline()
        if i==1:
            point = int(temp)
    for i in range(point):
        if i==int(infile.readline()):
            signal.append(float(infile.readline()))
    to_raf(signal,filename)
    infile.close()
    return

def csv_to_raf(filename):
    infile = open(filename+'.csv')
    signal = []
    infile.readline()
    point = int(infile.readline().split(',')[3].split(':')[1])
    infile.readline()
    for i in range(point):
        temp = infile.readline().split(',')
        if i+1==int(temp[0]):
            signal.append(float(temp[1]))
    to_raf(signal,filename)
    infile.close()
    return

def to_raf(signal,filename):
    """Convert the signal (already the correct length) to a RAF file."""
    signal = np.array(signal,dtype=float)
    # Shift and convert the signal
    signal = signal - signal.min()
    signal = ((signal/signal.max()) * int("3fff", 16)).astype('int16')
    # Write the signal as binary.
    fp = open(filename+".RAF", "wb")
    draw(signal)
    signal.tofile(fp)

def main():
    filename = []
    if len(sys.argv)>1:
        for i in range(1,len(sys.argv)):
            filename.append(sys.argv[i])
    else:
        filename = raw_input("input file name[use space to split]:").split(' ')
    for i in filename:
        print i
        infile = i.split('.')
        if infile[1]=='arb' or infile[1]=='ARB':
            arb_to_raf(infile[0])
        elif infile[1]=='txt' or infile[1]=='TXT':
            txt_to_raf(infile[0])
        elif infile[1]=='csv' or infile[1]=='CSV':
            csv_to_raf(infile[0])
        else:
            print "ERROR"
    return

if __name__ == "__main__":
    main()
    #plt.show()
