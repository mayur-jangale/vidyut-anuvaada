# Sutra प.5.3.47: याप्ये पाशप्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — yApye pASap

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.47"
SUTRA_TEXT = "याप्ये पाशप्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — yApye pASap"


class Sutra5347:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.47: अग्निः'),
		('रामः', '', 'प.5.3.47: रामः'),
		('सीता', '', 'प.5.3.47: सीता'),
	]

