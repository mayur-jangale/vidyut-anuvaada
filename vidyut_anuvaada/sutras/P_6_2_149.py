# Sutra प.6.2.149: इत्थम्भूतेन कृतमिति च
# (Sandhi (euphonic combination)) — itTamBUtena kftamiti ca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.149"
SUTRA_TEXT = "इत्थम्भूतेन कृतमिति च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — itTamBUtena kftamiti ca"


class Sutra62149:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.149: अग्निः'),
		('रामः', '', 'प.6.2.149: रामः'),
		('सीता', '', 'प.6.2.149: सीता'),
	]

