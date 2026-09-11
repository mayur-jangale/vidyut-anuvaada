# Sutra प.2.4.23: सभा राजामनुष्यपूर्वा
# (Samasa (compound formation)) — saBA rAjAmanuzyapUrvA

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.23"
SUTRA_TEXT = "सभा राजामनुष्यपूर्वा"
SUTRA_DESC = "(Samasa (compound formation)) — saBA rAjAmanuzyapUrvA"


class Sutra2423:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

