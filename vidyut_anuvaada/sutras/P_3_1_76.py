# Sutra प.3.1.76: तनूकरणे तक्षः
# vā śnābhyāṃ — optional śna forms

from P_3_1 import apply_3_1_76

SUTRA_CODE = "प.3.1.76"
SUTRA_TEXT = "तनूकरणे तक्षः"
SUTRA_DESC = "vā śnābhyāṃ — optional śna forms"


class Sutra3176:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_76(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.76:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.76:root=रामः;pos='),
		('सीता', '', 'प.3.1.76:root=सीता;pos='),
	]

