# Sutra प.2.2.2: अर्धं नपुंसकम्
# (Samasa (compound formation)) — arDaM napuMsakam

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.2"
SUTRA_TEXT = "अर्धं नपुंसकम्"
SUTRA_DESC = "(Samasa (compound formation)) — arDaM napuMsakam"


class Sutra222:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

