
class ENGLSIH:
    keys = ["G", "G#", "A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#", "G2", "G#2", "A2", "Bb2", "B2",
            "C2", "C#2", "D2", "Eb2", "E2", "F2", "F#2", "G3"]

    label_main_note = "Main note:"
    label_sec_note = "Secondary note:"
    label_lenght_note = "Lenght:"

    pause_but_note = "note"
    pause_but_pause = "pause"

    no_sec_but = "none"
    add_but = "-> ADD"

    text_at = "at"
    text_with = "with"
    text_of_lenght = "of lenght"


class GERMAN:
    keys = ["G", "G#", "A", "Hb", "H", "C", "C#", "D", "Eb", "E", "F", "F#", "G2", "G#2", "A2", "Hb2", "H2",
            "C2", "C#2", "D2", "Eb2", "E2", "F2", "F#2", "G3"]

    label_main_note = "Hauptnote:"
    label_sec_note = "Beinote:"
    label_lenght_note = "Länge:"

    pause_but_note = "Note"
    pause_but_pause = "Pause"

    no_sec_but = "Nichts"
    add_but = "-> Hinzufügen"

    text_at = "auf"
    text_with = "mit"
    text_of_lenght = "der Länge"



def load_language(language):
    languages = {
        "english" : ENGLSIH,
        "german" : GERMAN
    }

    return languages[language]()