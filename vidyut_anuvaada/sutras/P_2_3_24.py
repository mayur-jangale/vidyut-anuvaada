# Sutra प.2.3.24: अकर्तर्यृणे पञ्चमी
# (Samasa (compound formation)) — akartaryfRe paYcamI

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.24"
SUTRA_TEXT = "अकर्तर्यृणे पञ्चमी"
SUTRA_DESC = "(Samasa (compound formation)) — akartaryfRe paYcamI"


class Sutra2324:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

