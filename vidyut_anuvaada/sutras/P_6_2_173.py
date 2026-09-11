# Sutra प.6.2.173: कपि पूर्वम्
# (Sandhi (euphonic combination)) — kapi pUrvam

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.173"
SUTRA_TEXT = "कपि पूर्वम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — kapi pUrvam"


class Sutra62173:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.173: अग्निः'),
		('रामः', '', 'प.6.2.173: रामः'),
		('सीता', '', 'प.6.2.173: सीता'),
	]

