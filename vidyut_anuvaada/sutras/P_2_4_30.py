# Sutra प.2.4.30: अपथं नपुंसकम्
# (Samasa (compound formation)) — apaTaM napuMsakam

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.30"
SUTRA_TEXT = "अपथं नपुंसकम्"
SUTRA_DESC = "(Samasa (compound formation)) — apaTaM napuMsakam"


class Sutra2430:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

