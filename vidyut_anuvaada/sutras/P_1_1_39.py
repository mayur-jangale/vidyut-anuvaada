# Sutra प.1.1.39: कृन्मेजन्तः
# tiṅ — the 18 verbal endings (तिप्, तस्, झि, etc.)

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.39"
SUTRA_TEXT = "कृन्मेजन्तः"
SUTRA_DESC = "tiṅ — the 18 verbal endings (तिप्, तस्, झि, etc.)"


class Sutra1139:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_39
		return apply_1_1_39(word, pos)

	EXAMPLES = [
		('तिप्', '', 'tiṅ:तिप्;verb-pratyaya'),
		('तस्', '', 'tiṅ:तस्;verb-pratyaya'),
		('मिप्', '', 'tiṅ:मिप्;verb-pratyaya'),
		('सु', '', 'non-tiṅ:सु'),
	]

