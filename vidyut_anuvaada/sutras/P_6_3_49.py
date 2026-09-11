# Sutra प.6.3.49: विभाषा चत्वारिंशत्प्रभृतौ सर्वेषाम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.49"
SUTRA_TEXT = "विभाषा चत्वारिंशत्प्रभृतौ सर्वेषाम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6349:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.49: अग्निः'),
		('रामः', '', 'प.6.3.49: रामः'),
		('सीता', '', 'प.6.3.49: सीता'),
	]

