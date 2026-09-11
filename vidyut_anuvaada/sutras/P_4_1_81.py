# Sutra प.4.1.81: दैवयज्ञिशौचिवृक्षिसात्यमुग्रिकाण्ठेविद्धिभ्योऽन्यतरस्याम्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.81"
SUTRA_TEXT = "दैवयज्ञिशौचिवृक्षिसात्यमुग्रिकाण्ठेविद्धिभ्योऽन्यतरस्याम्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4181:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

