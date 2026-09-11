# Sutra प.6.2.32: सप्तमी सिद्धशुष्कपक्वबन्धेष्वकालात्
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.32"
SUTRA_TEXT = "सप्तमी सिद्धशुष्कपक्वबन्धेष्वकालात्"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6232:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.32: अग्निः'),
		('रामः', '', 'प.6.2.32: रामः'),
		('सीता', '', 'प.6.2.32: सीता'),
	]

