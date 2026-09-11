# Sutra प.6.3.68: इच एकाचोऽम्प्रत्ययवच्च
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.68"
SUTRA_TEXT = "इच एकाचोऽम्प्रत्ययवच्च"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6368:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.68: अग्निः'),
		('रामः', '', 'प.6.3.68: रामः'),
		('सीता', '', 'प.6.3.68: सीता'),
	]

