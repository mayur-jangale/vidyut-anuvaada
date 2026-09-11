# Sutra प.4.1.140: अपूर्वपदादन्यतरस्यां यड्ढकञौ
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.140"
SUTRA_TEXT = "अपूर्वपदादन्यतरस्यां यड्ढकञौ"
SUTRA_DESC = "supaḥ — continued"


class Sutra41140:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

