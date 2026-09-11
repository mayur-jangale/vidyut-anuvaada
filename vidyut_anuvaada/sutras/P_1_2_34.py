# Sutra प.1.2.34: यज्ञकर्मण्यजपन्यूङ्खसामसु
# (Samjna (technical definitions)) — yajYakarmaRyajapanyUNKasAmasu

from P_1_2 import apply_1_2_34

SUTRA_CODE = "प.1.2.34"
SUTRA_TEXT = "यज्ञकर्मण्यजपन्यूङ्खसामसु"
SUTRA_DESC = "(Samjna (technical definitions)) — yajYakarmaRyajapanyUNKasAmasu"


class Sutra1234:
	def apply(self, word, pos):
		return apply_1_2_34(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-yajñādi:अग्निः'),
		('रामः', '', 'non-yajñādi:रामः'),
		('सीता', '', 'non-yajñādi:सीता'),
	]

