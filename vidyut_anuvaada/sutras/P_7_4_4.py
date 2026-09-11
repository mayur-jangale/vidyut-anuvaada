# Sutra प.7.4.4: लोपः पिबतेरीच्चाभ्यासस्य
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.4"
SUTRA_TEXT = "लोपः पिबतेरीच्चाभ्यासस्य"
SUTRA_DESC = "taddhita — continued"


class Sutra744:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.4: अग्निः'),
		('रामः', '', 'प.7.4.4: रामः'),
		('सीता', '', 'प.7.4.4: सीता'),
	]

