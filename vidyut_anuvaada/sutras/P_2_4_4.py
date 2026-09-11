# Sutra प.2.4.4: अध्वर्युक्रतुरनपुंसकम्
# (Samasa (compound formation)) — aDvaryukraturanapuMsakam

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.4"
SUTRA_TEXT = "अध्वर्युक्रतुरनपुंसकम्"
SUTRA_DESC = "(Samasa (compound formation)) — aDvaryukraturanapuMsakam"


class Sutra244:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

