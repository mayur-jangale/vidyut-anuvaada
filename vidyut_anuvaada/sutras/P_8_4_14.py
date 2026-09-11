# Sutra प.8.4.14: उपसर्गादसमासेऽपि णोपदेशस्य
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.14"
SUTRA_TEXT = "उपसर्गादसमासेऽपि णोपदेशस्य"
SUTRA_DESC = "final transformations — continued"


class Sutra8414:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.14: अग्निः'),
		('रामः', '', 'प.8.4.14: रामः'),
		('सीता', '', 'प.8.4.14: सीता'),
	]

