

t = open("notes.txt","r")
r = open("note_edit.txt","w")

j = []

for line in t:
    j.append(line)
    if len(j) == 3:
        note, freq, wave = j
        note = note.split("/")[0].strip()
        freq = freq.split(".")[0].strip()
        j = []
        print(note, freq)
        r.write(note+" "+freq+"\n")
