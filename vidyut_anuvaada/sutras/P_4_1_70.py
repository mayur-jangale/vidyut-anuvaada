# Sutra प.4.1.70: संहितशफलक्षणवामादेश्च
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.70"
SUTRA_TEXT = "संहितशफलक्षणवामादेश्च"
SUTRA_DESC = "supaḥ — continued"


class Sutra4170:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

