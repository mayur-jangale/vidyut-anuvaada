# Sutra प.4.1.100: हरितादिभ्योऽञः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.100"
SUTRA_TEXT = "हरितादिभ्योऽञः"
SUTRA_DESC = "supaḥ — continued"


class Sutra41100:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

