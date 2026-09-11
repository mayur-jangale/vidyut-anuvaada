# Sutra प.6.2.136: कुण्डं वनम्
# (Sandhi (euphonic combination)) — kuRqaM vanam

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.136"
SUTRA_TEXT = "कुण्डं वनम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — kuRqaM vanam"


class Sutra62136:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.136: अग्निः'),
		('रामः', '', 'प.6.2.136: रामः'),
		('सीता', '', 'प.6.2.136: सीता'),
	]

