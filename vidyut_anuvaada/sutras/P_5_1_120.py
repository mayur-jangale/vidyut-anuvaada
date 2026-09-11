# Sutra प.5.1.120: आ च त्वात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — A ca tvAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.120"
SUTRA_TEXT = "आ च त्वात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — A ca tvAt"


class Sutra51120:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.120: अग्निः'),
		('रामः', '', 'प.5.1.120: रामः'),
		('सीता', '', 'प.5.1.120: सीता'),
	]

