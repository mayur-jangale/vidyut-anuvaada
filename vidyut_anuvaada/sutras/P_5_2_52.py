# Sutra प.5.2.52: बहुपूगगणसंघस्य तिथुक्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — bahupUgagaRasaMGasya tiTuk

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.52"
SUTRA_TEXT = "बहुपूगगणसंघस्य तिथुक्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — bahupUgagaRasaMGasya tiTuk"


class Sutra5252:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.52: अग्निः'),
		('रामः', '', 'प.5.2.52: रामः'),
		('सीता', '', 'प.5.2.52: सीता'),
	]

