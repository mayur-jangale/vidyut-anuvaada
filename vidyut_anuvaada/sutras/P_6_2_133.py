# Sutra प.6.2.133: नाचार्यराजर्त्विक्संयुक्तज्ञात्याख्येभ्यः
# (Sandhi (euphonic combination)) — nAcAryarAjartviksaMyuktajYAtyAKyeByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.133"
SUTRA_TEXT = "नाचार्यराजर्त्विक्संयुक्तज्ञात्याख्येभ्यः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — nAcAryarAjartviksaMyuktajYAtyAKyeByaH"


class Sutra62133:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.133: अग्निः'),
		('रामः', '', 'प.6.2.133: रामः'),
		('सीता', '', 'प.6.2.133: सीता'),
	]

