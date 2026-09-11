# Sutra प.4.1.47: भुवश्च
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.47"
SUTRA_TEXT = "भुवश्च"
SUTRA_DESC = "supaḥ — continued"


class Sutra4147:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

