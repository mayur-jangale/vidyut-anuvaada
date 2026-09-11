# Sutra प.4.1.22: अपरिमाणबिस्ताचितकम्बल्येभ्यो न तद्धितलुकि
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.22"
SUTRA_TEXT = "अपरिमाणबिस्ताचितकम्बल्येभ्यो न तद्धितलुकि"
SUTRA_DESC = "supaḥ — continued"


class Sutra4122:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

