# Sutra प.6.2.144: थाथघञ्क्ताजबित्रकाणाम्
# (Sandhi (euphonic combination)) — TATaGaYktAjabitrakARAm

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.144"
SUTRA_TEXT = "थाथघञ्क्ताजबित्रकाणाम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — TATaGaYktAjabitrakARAm"


class Sutra62144:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.144: अग्निः'),
		('रामः', '', 'प.6.2.144: रामः'),
		('सीता', '', 'प.6.2.144: सीता'),
	]

