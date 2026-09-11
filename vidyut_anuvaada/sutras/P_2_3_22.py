# Sutra प.2.3.22: संज्ञोऽन्यतरस्यां कर्मणि
# (Samasa (compound formation)) — saMjYo'nyatarasyAM karmaRi

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.22"
SUTRA_TEXT = "संज्ञोऽन्यतरस्यां कर्मणि"
SUTRA_DESC = "(Samasa (compound formation)) — saMjYo'nyatarasyAM karmaRi"


class Sutra2322:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

