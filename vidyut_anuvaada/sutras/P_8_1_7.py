# Sutra प.8.1.7: उपर्यध्यधसः सामीप्ये
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.7"
SUTRA_TEXT = "उपर्यध्यधसः सामीप्ये"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra817:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.7: अग्निः'),
		('रामः', '', 'प.8.1.7: रामः'),
		('सीता', '', 'प.8.1.7: सीता'),
	]

