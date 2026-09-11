# Sutra प.4.1.119: ढक् च मण्डूकात्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.119"
SUTRA_TEXT = "ढक् च मण्डूकात्"
SUTRA_DESC = "supaḥ — continued"


class Sutra41119:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

