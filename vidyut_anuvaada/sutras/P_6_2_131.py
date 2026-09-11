# Sutra प.6.2.131: वर्ग्यादयश्च
# (Sandhi (euphonic combination)) — vargyAdayaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.131"
SUTRA_TEXT = "वर्ग्यादयश्च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — vargyAdayaSca"


class Sutra62131:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.131: अग्निः'),
		('रामः', '', 'प.6.2.131: रामः'),
		('सीता', '', 'प.6.2.131: सीता'),
	]

