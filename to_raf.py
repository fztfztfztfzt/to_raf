"""
The RAF file works for the DG4602.
powered by Polaris
"""
import numpy as np

def arb_to_raf(filename):
    infile = open(filename+'.arb')
    for i in range(8):
        temp = infile.readline()
        if i==6:
            point = int(temp.split(':')[1])
    signal = []
    for i in range(point):
        signal.append(int(infile.readline()))
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
    """
    if len(signal)!=8192:
        print "length should be 8192"
        return
    """
    signal = np.array(signal,dtype=float)
    # Shift and convert the signal
    signal = signal - signal.min()
    signal = ((signal/signal.max()) * int("3fff", 16)).astype('int16')
    # Write the signal as binary.
    fp = open(filename+".RAF", "w")
    signal.tofile(fp)

def main():
    while True:
        filename = raw_input("input file name:")
        filename = filename.split('.')
        if filename[1]=='arb' or filename[1]=='ARB':
            arb_to_raf(filename[0])
        elif filename[1]=='txt' or filename[1]=='TXT':
            txt_to_raf(filename[0])
        elif filename[1]=='csv' or filename[1]=='CSV':
            csv_to_raf(filename[0])
        else:
            print "ERROR"
    return

if __name__ == "__main__":
    main()
