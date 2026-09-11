# Sutra प.7.3.42: शदेरगतौ तः
# (Taddhita (secondary derivations)) — SaderagatO taH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.42"
SUTRA_TEXT = "शदेरगतौ तः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — SaderagatO taH"


class Sutra7342:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.42: अग्निः'),
		('रामः', '', 'प.7.3.42: रामः'),
		('सीता', '', 'प.7.3.42: सीता'),
	]

