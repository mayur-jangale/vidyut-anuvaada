# Sutra प.6.3.119: मतौ बह्वचोऽनजिरादीनाम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.119"
SUTRA_TEXT = "मतौ बह्वचोऽनजिरादीनाम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63119:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.119: अग्निः'),
		('रामः', '', 'प.6.3.119: रामः'),
		('सीता', '', 'प.6.3.119: सीता'),
	]

