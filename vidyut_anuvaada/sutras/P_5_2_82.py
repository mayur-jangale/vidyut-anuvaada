# Sutra प.5.2.82: तदस्मिन्नन्नं प्राये संज्ञायाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadasminnannaM prAye saMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.82"
SUTRA_TEXT = "तदस्मिन्नन्नं प्राये संज्ञायाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadasminnannaM prAye saMjYAyAm"


class Sutra5282:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.82: अग्निः'),
		('रामः', '', 'प.5.2.82: रामः'),
		('सीता', '', 'प.5.2.82: सीता'),
	]

