# Sutra प.4.1.139: कुलात् खः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.139"
SUTRA_TEXT = "कुलात् खः"
SUTRA_DESC = "supaḥ — continued"


class Sutra41139:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

