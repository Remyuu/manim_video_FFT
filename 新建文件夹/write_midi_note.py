from mido import Message, MidiFile, MidiTrack
import random
import Notes_Toolbox
#为什么会报错？？

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=0, time=0))


# # # def play_note(note, length, track, base_num=0, delay=0, velocity=1.0, channel=0):
# # #     bpm = 125
# # #     meta_time = 60 / bpm * 1000 # 一拍多少毫秒，一拍等于一个四分音符
# # #     major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
# # #     base_note = 60 # C4
# # #     track.append(Message('note_on', note=base_note + base_num*12 + sum(major_notes[0:note]), velocity=round(64*velocity), time=round(delay*meta_time), channel=channel))
# # #     track.append(Message('note_off', note=base_note + base_num*12 + sum(major_notes[0:note]), velocity=round(64*velocity), time=round(meta_time*length), channel=channel))
# # #     # 1 就是 四分音符
# # # my_list = [0.5, 1, 1.5] # 分别代表八分音符，四分音符以及带附点的四分音符
# # # for v in range(1,100):
# # #     play_note(random.randint(1,7), random.choice(my_list), track) #仅仅在小字一组生成旋律
# # # mid.save('MyFirstDamnSong.mid')


#输出分解和弦到midi文件
    # 使用此方法时，需要传入
        #track mido库的输出音频接口 : MidiTrack()
        #root : 'C','D','E','F','G','A','B'
        #name 和弦的名称，在Notes_Toolbox中定义了 : 'Major3'...
        #format 分解和弦的方式 : [0,1,2] [1,3,2,3]...
        #length 音符持续的时长 : 
def add_broken_chord(root, name, format, length, track, tone_name='Cmajor', root_base=0, channel=0):
    #默认是c大调
    root_num = Notes_Toolbox.Cmajor
    if tone_name == 'Eflat':
        root_num = {'C': 63, 'D': 65, 'E': 67, 'F': 68, 'G': 70, 'A': 72, 'B': 74}
    root_note = root_num[root] + root_base*12  # 分解和弦的根音
    
    time = (length * 480) / len(format)  # 此处为官方文档写法，我也不懂，time指的是音符持续时长
    for broken_chord in format:  # 通过for循环，逐个输出和弦的音符
        note = root_note + Notes_Toolbox.get_chord(name)[broken_chord]
        track.append(Message('note_on', note=note,
                     velocity=60, time=0, channel=channel))
        track.append(Message('note_on', note=note, velocity=60,
                     time=round(time), channel=channel))


format = [0, 1, 2, 3]
add_broken_chord('C', 'Major3', format, 4, track)
add_broken_chord('C', 'Minor3', format, 4, track)
add_broken_chord('C', 'Augmented3', format, 4, track)
add_broken_chord('C', 'Diminished3', format, 4, track)
add_broken_chord('C', 'Diminished3', format, 4, track)
mid.save('MySecondDamnSong.mid')

