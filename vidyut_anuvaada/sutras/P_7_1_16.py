# Sutra प.7.1.16: पूर्वादिभ्यो नवभ्यो वा
# (Taddhita (secondary derivations)) — pUrvAdiByo navaByo vA

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.16"
SUTRA_TEXT = "पूर्वादिभ्यो नवभ्यो वा"
SUTRA_DESC = "(Taddhita (secondary derivations)) — pUrvAdiByo navaByo vA"


class Sutra7116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.16: अग्निः'),
		('रामः', '', 'प.7.1.16: रामः'),
		('सीता', '', 'प.7.1.16: सीता'),
	]

