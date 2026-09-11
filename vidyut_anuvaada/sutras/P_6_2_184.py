# Sutra प.6.2.184: निरुदकादीनि च
# (Sandhi (euphonic combination)) — nirudakAdIni ca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.184"
SUTRA_TEXT = "निरुदकादीनि च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — nirudakAdIni ca"


class Sutra62184:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.184: अग्निः'),
		('रामः', '', 'प.6.2.184: रामः'),
		('सीता', '', 'प.6.2.184: सीता'),
	]

