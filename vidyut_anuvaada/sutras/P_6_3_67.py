# Sutra प.6.3.67: अरुर्द्विषदजन्तस्य मुम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.67"
SUTRA_TEXT = "अरुर्द्विषदजन्तस्य मुम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6367:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.67: अग्निः'),
		('रामः', '', 'प.6.3.67: रामः'),
		('सीता', '', 'प.6.3.67: सीता'),
	]

