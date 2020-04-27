#!/usr/bin/python

import sys, getopt, os
import nltk
from nltk import tokenize
nltk.download('punkt')

inputfile = ''
outputfile = ''
gutenberg = False

def gutenlinemake():
    ifile = open(inputfile,"r")
    tmp = open("tmp.txt","w+")
    ofile = open(outputfile,"w")
    start = False
    end = False
    for aline in ifile:
        val = aline.split()
        if len(val)>4 and val[0]=="End" and val[1]=="of" and val[2]=="the" and val[3]=="Project" and val[4]=="Gutenberg":
            end = True
        elif len(val)>2 and val[0]=="*" and val[1]=="*":
            print('ignoring:',aline)
        elif len(val)>0 and start and not end:
            tmp.write(aline.rstrip()+' ')
        elif len(val)>4 and val[0]=="***" and val[1]=="START" and val[2]=="OF" and val[3]=="THIS" and val[4]=="PROJECT":
            start = True

    #splitup lines by sentences
    tmp.seek(0)
    count = 1
    for sentence in tokenize.sent_tokenize(tmp.read()):
        #ofile.write(inputfile+"-"+'{:05d}'.format(count)+"|"+sentence+'\n')
        ofile.write(sentence+'\n')
        count += 1
    tmp.truncate()
    tmp.close()
    os.remove("tmp.txt")

    ifile.close()
    ofile.close()

def linemake():
    ifile = open(inputfile,"r")
    ofile = open(outputfile,"w")
    count = 1
    for sentence in tokenize.sent_tokenize(ifile.read()): 
        #ofile.write(inputfile+"-"+'{:05d}'.format(count)+"|"+sentence+'\n')
        ofile.write(sentence+'\n')
        count += 1
    ifile.close()
    ofile.close()

def main(argv):
    global inputfile
    global outputfile
    global gutenberg
    try:
        opts, args = getopt.getopt(argv,"hi:o:g",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('textify.py -i <inputfile> -o <outputfile>')
        print ('add a -g or --gutenberg to remove legal cruft from the text ebook')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('textify.py -g -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            print ('Input file:', inputfile)
        elif opt in ("-o", "--ofile"):
            outputfile = arg
            print ('Output file:', outputfile)
        elif opt in ("-g"):
            gutenberg = True
            print ('gutenberg:', gutenberg)
    if not inputfile or not outputfile:
        print ('textify.py -i <inputfile> -o <outputfile>')
        print ('add a -g or --gutenberg to remove legal cruft from the text ebook')
        sys.exit(2)        
        
if __name__ == "__main__":
    main(sys.argv[1:])
    if gutenberg:
        gutenlinemake()
    else:
        linemake()