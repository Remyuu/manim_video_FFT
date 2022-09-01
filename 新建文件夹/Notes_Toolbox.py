bpm = 125 #why 125:
    #bpm = 1 * 1000 / 8 
timePerBeat = 60 / bpm * 1000
base_note = 60 # C4
note_name =[
    'C','D','E','F','G','A','B'
]

major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
Cmajor_notes = []
Eflatmajor_notes = []

for num in range(12):
    Cmajor_notes.append(base_note+sum(major_notes[0:num+1]))
    Eflatmajor_notes.append(base_note+3+sum(major_notes[0:num+1]))
#这里只有一个区
Cmajor = dict(zip(note_name,Cmajor_notes))
# Cmajor = {'C': 60, 'D': 62, 'E': 64, 'F': 65, 'G': 67, 'A': 69, 'B': 71}
Eflatmajor = dict(zip(note_name, Eflatmajor_notes))
# Eflatmajor = {'C': 63, 'D': 65, 'E': 67, 'F': 68, 'G': 70, 'A': 72, 'B': 74}

def get_note(note,group=0,**kw):#Group = 0 means 4Group
    global base_note,major_notes
    return base_note + group*12 + sum(major_notes[0,note])

def originToEflatMajor(list,**kw):
    Ef=[]
    for x in list:
        Ef.append(x+3)
    return Ef

#get_note(1,group=0) return 60
#get_note(2,group=0) return 62
def get_chord(name):
    chord = {
        "Major3":[0,4,7,12],#大三和弦
        "Minor3":[0,3,7,12],#小三和弦
        "Augmented3":[0,4,8,12],#增三和弦
        "Diminished3":[0,3,6,12],#减三和弦

        "M7":[0,4,7,11],#大七和弦
        "Mm7":[0,4,7,10],#属七和弦
        "m7":[0,3,7,10],#小七和弦
        "mM7":[],
        #...
    }
    return chord[name]
#get_chord(“Major”) return [0,4,7,12]


