import sys, getopt, os
from aeneas.executetask import ExecuteTask
from aeneas.task import Task
from pydub import AudioSegment

inputsound = ''
inputtext = ''
outputdir = ''

def chopsounds():
    # create Task object
    config_string = u"task_language=eng|is_text_type=plain|os_task_file_format=json"
    task = Task(config_string=config_string)
    task.audio_file_path_absolute = inputsound
    task.text_file_path_absolute = inputtext

    # process Task
    ExecuteTask(task).execute()

    # Carve wav file into fragments
    sound = AudioSegment.from_wav(inputsound)
    for fragment in task.sync_map_leaves():
        if fragment.length > 0.0:
            fsound = sound[float(fragment.begin)*1000:float(fragment.end)*1000]
            fsound.export(outputdir+"/"+fragment.identifier+".wav",format="wav")

def main(argv):
    global inputsound
    global inputtext
    global outputdir
    try:
        opts, args = getopt.getopt(argv,"hs:t:o:",["inputsound=","inputtext=","outputdir="])
    except getopt.GetoptError:
        print ('soundify.py -s <inputsound> -t <inputtext> -o <outputdir>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('soundify.py -s <inputsound> -t inputtext -o <outputdir>')
            sys.exit()
        elif opt in ("-s", "--inputsound"):
            inputsound = arg
            print ('Input sound:', inputsound)
        elif opt in ("-t", "--inputtext"):
            inputtext = arg
            print ('Input sound:', inputtext)            
        elif opt in ("-o", "--outputdir"):
            outputdir = arg
            print('Output Dir:', outputdir)
    if inputsound=='' or inputtext=='':
        print ('soundify.py -s <inputsound> -t <inputtext> -o <outputdir>')
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
    chopsounds()
