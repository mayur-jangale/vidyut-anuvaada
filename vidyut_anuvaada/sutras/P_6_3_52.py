# Sutra प.6.3.52: पादस्य पदाज्यातिगोपहतेषु
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.52"
SUTRA_TEXT = "पादस्य पदाज्यातिगोपहतेषु"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6352:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.52: अग्निः'),
		('रामः', '', 'प.6.3.52: रामः'),
		('सीता', '', 'प.6.3.52: सीता'),
	]

