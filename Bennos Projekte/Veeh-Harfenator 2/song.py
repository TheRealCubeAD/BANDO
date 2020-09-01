
class SONG:

    def __init__(self):
        self.notes = []

    def add_note(self, note, pos=-1):
        if pos == -1:
            self.notes.append(note)
        else:
            self.notes.insert(pos, note)
        self.update_index()

    def get_note(self, index):
        if index < len(self.notes):
            return self.notes[index]
        else:
            return None

    def get_notes(self):
        return self.notes

    def update_index(self):
        for i in range(len(self.notes)):
            self.notes[i].set_index(i + 1)

    def del_note(self, index):
        if index < len(self.notes):
            del(self.notes[index])
        self.update_index()

    def link_ammount(self, id):
        ammount = 0
        for note in self.notes:
            if id in note.links:
                ammount += 1
        return ammount