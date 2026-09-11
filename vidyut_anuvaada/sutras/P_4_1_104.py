# Sutra प.4.1.104: अनृष्यानन्तर्ये बिदादिभ्योऽञ्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.104"
SUTRA_TEXT = "अनृष्यानन्तर्ये बिदादिभ्योऽञ्"
SUTRA_DESC = "supaḥ — continued"


class Sutra41104:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

