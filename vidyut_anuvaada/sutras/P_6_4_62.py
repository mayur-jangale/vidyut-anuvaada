# Sutra प.6.4.62: स्यसिच्सीयुट्तासिषु भावकर्मणोरुपदेशेऽज्झनग्रहदृशां वा चिण्वदिट् च
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.62"
SUTRA_TEXT = "स्यसिच्सीयुट्तासिषु भावकर्मणोरुपदेशेऽज्झनग्रहदृशां वा चिण्वदिट् च"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6462:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.62: अग्निः'),
		('रामः', '', 'प.6.4.62: रामः'),
		('सीता', '', 'प.6.4.62: सीता'),
	]

