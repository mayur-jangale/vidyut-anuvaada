# Sutra प.2.3.41: यतश्च निर्धारणम्
# (Samasa (compound formation)) — yataSca nirDAraRam

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.41"
SUTRA_TEXT = "यतश्च निर्धारणम्"
SUTRA_DESC = "(Samasa (compound formation)) — yataSca nirDAraRam"


class Sutra2341:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

