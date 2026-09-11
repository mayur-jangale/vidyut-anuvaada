# Sutra प.4.1.15: टिड्ढाणञ्द्वयसज्दघ्नञ्मात्रच्तयप्ठक्ठञ्कञ्क्वरपः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.15"
SUTRA_TEXT = "टिड्ढाणञ्द्वयसज्दघ्नञ्मात्रच्तयप्ठक्ठञ्कञ्क्वरपः"
SUTRA_DESC = "supaḥ — continued"


class Sutra4115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

