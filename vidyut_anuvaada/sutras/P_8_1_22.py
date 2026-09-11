# Sutra प.8.1.22: तेमयावेकवचनस्य
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.22"
SUTRA_TEXT = "तेमयावेकवचनस्य"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8122:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.22: अग्निः'),
		('रामः', '', 'प.8.1.22: रामः'),
		('सीता', '', 'प.8.1.22: सीता'),
	]

