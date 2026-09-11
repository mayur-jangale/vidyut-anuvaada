# Sutra प.6.2.192: नेरनिधाने
# (Sandhi (euphonic combination)) — neraniDAne

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.192"
SUTRA_TEXT = "नेरनिधाने"
SUTRA_DESC = "(Sandhi (euphonic combination)) — neraniDAne"


class Sutra62192:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.192: अग्निः'),
		('रामः', '', 'प.6.2.192: रामः'),
		('सीता', '', 'प.6.2.192: सीता'),
	]

