# Sutra प.4.1.61: वाहः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.61"
SUTRA_TEXT = "वाहः"
SUTRA_DESC = "supaḥ — continued"


class Sutra4161:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

