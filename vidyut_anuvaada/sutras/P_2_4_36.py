# Sutra प.2.4.36: अदो जग्धिर्ल्यप्ति किति
# (Samasa (compound formation)) — ado jagDirlyapti kiti

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.36"
SUTRA_TEXT = "अदो जग्धिर्ल्यप्ति किति"
SUTRA_DESC = "(Samasa (compound formation)) — ado jagDirlyapti kiti"


class Sutra2436:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

