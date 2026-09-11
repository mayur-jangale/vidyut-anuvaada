# Sutra प.6.4.55: अयामन्ताल्वाय्येत्न्विष्णुषु
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.55"
SUTRA_TEXT = "अयामन्ताल्वाय्येत्न्विष्णुषु"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6455:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.55: अग्निः'),
		('रामः', '', 'प.6.4.55: रामः'),
		('सीता', '', 'प.6.4.55: सीता'),
	]

