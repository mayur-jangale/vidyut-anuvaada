# Sutra प.2.4.17: स नपुंसकम्
# (Samasa (compound formation)) — sa napuMsakam

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.17"
SUTRA_TEXT = "स नपुंसकम्"
SUTRA_DESC = "(Samasa (compound formation)) — sa napuMsakam"


class Sutra2417:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

