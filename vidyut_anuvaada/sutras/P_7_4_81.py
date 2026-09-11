# Sutra प.7.4.81: स्रवतिशृणोतिद्रवतिप्रवतिप्लवतिच्यवतीनां वा
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.81"
SUTRA_TEXT = "स्रवतिशृणोतिद्रवतिप्रवतिप्लवतिच्यवतीनां वा"
SUTRA_DESC = "taddhita — continued"


class Sutra7481:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.81: अग्निः'),
		('रामः', '', 'प.7.4.81: रामः'),
		('सीता', '', 'प.7.4.81: सीता'),
	]

