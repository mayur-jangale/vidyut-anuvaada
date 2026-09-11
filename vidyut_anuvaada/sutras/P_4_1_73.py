# Sutra प.4.1.73: शार्ङ्गरवाद्यञो ङीन्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.73"
SUTRA_TEXT = "शार्ङ्गरवाद्यञो ङीन्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4173:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

