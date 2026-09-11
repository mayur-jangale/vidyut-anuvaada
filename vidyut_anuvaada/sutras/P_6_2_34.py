# Sutra प.6.2.34: राजन्यबहुवचनद्वन्द्वेऽन्धकवृष्णिषु
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.34"
SUTRA_TEXT = "राजन्यबहुवचनद्वन्द्वेऽन्धकवृष्णिषु"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6234:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.34: अग्निः'),
		('रामः', '', 'प.6.2.34: रामः'),
		('सीता', '', 'प.6.2.34: सीता'),
	]

