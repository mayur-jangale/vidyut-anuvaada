# Sutra प.6.2.135: षट् च काण्डादीनि
# (Sandhi (euphonic combination)) — zaw ca kARqAdIni

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.135"
SUTRA_TEXT = "षट् च काण्डादीनि"
SUTRA_DESC = "(Sandhi (euphonic combination)) — zaw ca kARqAdIni"


class Sutra62135:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.135: अग्निः'),
		('रामः', '', 'प.6.2.135: रामः'),
		('सीता', '', 'प.6.2.135: सीता'),
	]

