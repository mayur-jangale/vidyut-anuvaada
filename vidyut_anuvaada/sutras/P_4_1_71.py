# Sutra प.4.1.71: कद्रुकमण्डल्वोश्छन्दसि
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.71"
SUTRA_TEXT = "कद्रुकमण्डल्वोश्छन्दसि"
SUTRA_DESC = "supaḥ — continued"


class Sutra4171:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

