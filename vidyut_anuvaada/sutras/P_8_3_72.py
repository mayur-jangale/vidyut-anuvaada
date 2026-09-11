# Sutra प.8.3.72: अनुविपर्यभिनिभ्यः स्यन्दतेरप्राणिषु
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.72"
SUTRA_TEXT = "अनुविपर्यभिनिभ्यः स्यन्दतेरप्राणिषु"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8372:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.72: अग्निः'),
		('रामः', '', 'प.8.3.72: रामः'),
		('सीता', '', 'प.8.3.72: सीता'),
	]

