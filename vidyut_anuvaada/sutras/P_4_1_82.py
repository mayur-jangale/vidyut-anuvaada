# Sutra प.4.1.82: समर्थानां प्रथमाद्वा
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.82"
SUTRA_TEXT = "समर्थानां प्रथमाद्वा"
SUTRA_DESC = "supaḥ — continued"


class Sutra4182:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

