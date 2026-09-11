# Sutra प.4.1.60: दिक्पूर्वपदान्ङीप्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.60"
SUTRA_TEXT = "दिक्पूर्वपदान्ङीप्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4160:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

