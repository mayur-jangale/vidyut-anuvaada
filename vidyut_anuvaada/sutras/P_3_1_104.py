# Sutra प.3.1.104: उपसर्या काल्या प्रजने
# vali lopaḥ — repeated pattern

from P_3_1 import apply_3_1_104

SUTRA_CODE = "प.3.1.104"
SUTRA_TEXT = "उपसर्या काल्या प्रजने"
SUTRA_DESC = "vali lopaḥ — repeated pattern"


class Sutra31104:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_104(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.104:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.104:root=रामः;pos='),
		('सीता', '', 'प.3.1.104:root=सीता;pos='),
	]

