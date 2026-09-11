# Sutra प.4.1.18: सर्वत्र लोहितादिकतन्तेभ्यः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.18"
SUTRA_TEXT = "सर्वत्र लोहितादिकतन्तेभ्यः"
SUTRA_DESC = "supaḥ — continued"


class Sutra4118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

