# Sutra प.4.1.19: कौरव्यमाण्डूकाभ्यां च
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.19"
SUTRA_TEXT = "कौरव्यमाण्डूकाभ्यां च"
SUTRA_DESC = "supaḥ — continued"


class Sutra4119:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

