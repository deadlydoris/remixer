from pydub import *
from math import ceil

#class Masher():
 #   def mash(self):#, file1, file2, splice_length_1, splice_length_2):
track1 = AudioSegment.from_mp3("track1.mp3")
track2 = AudioSegment.from_mp3("track2.mp3")
# track1 = AudioSegment.from_wav("track1.wav")
# track2 = AudioSegment.from_wav("track2.wav")
print(track1.duration_seconds)
print(track2.duration_seconds)
splice_length_1 = 3
splice_length_2 = 4
num_slices_1 = track1.duration_seconds / splice_length_1
num_slices_2 = track2.duration_seconds / splice_length_2

track1_pieces = list()
track2_pieces = list()

splice_start = 0
for i in range(ceil(num_slices_1)):
    splice_end = splice_start + splice_length_1
    track1_pieces.append(track1[splice_start*1000:splice_end*1000])
    splice_start = splice_end

splice_start = 0
for i in range(ceil(num_slices_2)):
    splice_end = splice_start + splice_length_2
    track2_pieces.append(track2[splice_start*1000:splice_end*1000])
    splice_start = splice_end

print(len(track1_pieces))
print(len(track2_pieces))

if len(track1_pieces) >= len(track2_pieces):
    for idx, track1_piece in enumerate(track1_pieces):
        print(idx)
        if idx == 0:
            #First time through the list - declare song variable
            song = track1_piece + track2_pieces[idx]
        else:
            #Second + times through list - add to existing song variable
            if idx < len(track2_pieces):
                song = song + track1_piece + track2_pieces[idx]
            else: 
                song = song + track1_piece + track2_pieces[-1]

    song.export("mashup.mp3", format="mp3")
                    
