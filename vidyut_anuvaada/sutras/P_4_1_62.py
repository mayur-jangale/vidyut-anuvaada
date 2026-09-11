# Sutra प.4.1.62: सख्यशिश्वीति भाषायाम्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.62"
SUTRA_TEXT = "सख्यशिश्वीति भाषायाम्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4162:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

