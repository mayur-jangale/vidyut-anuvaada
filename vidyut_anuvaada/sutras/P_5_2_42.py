# Sutra प.5.2.42: संख्याया अवयवे तयप्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyAyA avayave tayap

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.42"
SUTRA_TEXT = "संख्याया अवयवे तयप्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyAyA avayave tayap"


class Sutra5242:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.42: अग्निः'),
		('रामः', '', 'प.5.2.42: रामः'),
		('सीता', '', 'प.5.2.42: सीता'),
	]

