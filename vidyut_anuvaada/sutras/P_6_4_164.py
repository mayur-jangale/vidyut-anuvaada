# Sutra प.6.4.164: इनण्यनपत्ये
# (Sandhi (euphonic combination)) — inaRyanapatye

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.164"
SUTRA_TEXT = "इनण्यनपत्ये"
SUTRA_DESC = "(Sandhi (euphonic combination)) — inaRyanapatye"


class Sutra64164:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.164: अग्निः'),
		('रामः', '', 'प.6.4.164: रामः'),
		('सीता', '', 'प.6.4.164: सीता'),
	]

