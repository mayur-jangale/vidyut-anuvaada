# Sutra प.6.3.133: ऋचि तुनुघमक्षुतङ्कुत्रोरुष्याणाम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.133"
SUTRA_TEXT = "ऋचि तुनुघमक्षुतङ्कुत्रोरुष्याणाम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63133:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.133: अग्निः'),
		('रामः', '', 'प.6.3.133: रामः'),
		('सीता', '', 'प.6.3.133: सीता'),
	]

