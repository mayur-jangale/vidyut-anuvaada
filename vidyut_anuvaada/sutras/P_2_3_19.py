# Sutra प.2.3.19: सहयुक्तेऽप्रधाने
# (Samasa (compound formation)) — sahayukte'praDAne

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.19"
SUTRA_TEXT = "सहयुक्तेऽप्रधाने"
SUTRA_DESC = "(Samasa (compound formation)) — sahayukte'praDAne"


class Sutra2319:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

