# Sutra प.5.4.153: नद्यृतश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — nadyftaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.153"
SUTRA_TEXT = "नद्यृतश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — nadyftaSca"


class Sutra54153:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.153: अग्निः'),
		('रामः', '', 'प.5.4.153: रामः'),
		('सीता', '', 'प.5.4.153: सीता'),
	]

