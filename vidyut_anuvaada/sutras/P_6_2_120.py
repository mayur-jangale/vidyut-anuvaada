# Sutra प.6.2.120: वीरवीर्यौ च
# (Sandhi (euphonic combination)) — vIravIryO ca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.120"
SUTRA_TEXT = "वीरवीर्यौ च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — vIravIryO ca"


class Sutra62120:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.120: अग्निः'),
		('रामः', '', 'प.6.2.120: रामः'),
		('सीता', '', 'प.6.2.120: सीता'),
	]

