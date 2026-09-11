# Sutra प.7.2.62: उपदेशेऽत्वतः
# (Taddhita (secondary derivations)) — upadeSe'tvataH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.62"
SUTRA_TEXT = "उपदेशेऽत्वतः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — upadeSe'tvataH"


class Sutra7262:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.62: अग्निः'),
		('रामः', '', 'प.7.2.62: रामः'),
		('सीता', '', 'प.7.2.62: सीता'),
	]

