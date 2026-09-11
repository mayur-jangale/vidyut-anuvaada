# Sutra प.4.1.43: शोणात् प्राचाम्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.43"
SUTRA_TEXT = "शोणात् प्राचाम्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4143:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

