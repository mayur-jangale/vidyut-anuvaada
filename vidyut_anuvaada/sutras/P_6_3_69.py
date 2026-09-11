# Sutra प.6.3.69: वाचंयमपुरंदरौ च
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.69"
SUTRA_TEXT = "वाचंयमपुरंदरौ च"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6369:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.69: अग्निः'),
		('रामः', '', 'प.6.3.69: रामः'),
		('सीता', '', 'प.6.3.69: सीता'),
	]

