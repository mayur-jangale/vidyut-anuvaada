# Sutra प.7.2.10: एकाच उपदेशेऽनुदात्तात्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.10"
SUTRA_TEXT = "एकाच उपदेशेऽनुदात्तात्"
SUTRA_DESC = "taddhita — continued"


class Sutra7210:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.10: अग्निः'),
		('रामः', '', 'प.7.2.10: रामः'),
		('सीता', '', 'प.7.2.10: सीता'),
	]

