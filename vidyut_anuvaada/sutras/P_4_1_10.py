# Sutra प.4.1.10: न षट्स्वस्रादिभ्यः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.10"
SUTRA_TEXT = "न षट्स्वस्रादिभ्यः"
SUTRA_DESC = "supaḥ — continued"


class Sutra4110:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

