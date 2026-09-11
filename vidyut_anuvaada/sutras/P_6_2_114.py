# Sutra प.6.2.114: कण्ठपृष्ठग्रीवाजंघं च
# (Sandhi (euphonic combination)) — kaRWapfzWagrIvAjaMGaM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.114"
SUTRA_TEXT = "कण्ठपृष्ठग्रीवाजंघं च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — kaRWapfzWagrIvAjaMGaM ca"


class Sutra62114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.114: अग्निः'),
		('रामः', '', 'प.6.2.114: रामः'),
		('सीता', '', 'प.6.2.114: सीता'),
	]

