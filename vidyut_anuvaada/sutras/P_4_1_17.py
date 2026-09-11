# Sutra प.4.1.17: प्राचां ष्फ तद्धितः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.17"
SUTRA_TEXT = "प्राचां ष्फ तद्धितः"
SUTRA_DESC = "supaḥ — continued"


class Sutra4117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

