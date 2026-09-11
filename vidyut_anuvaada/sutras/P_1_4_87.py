# Sutra प.1.4.87: उपोऽधिके च
# (Samjna (technical definitions)) — upo'Dike ca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.87"
SUTRA_TEXT = "उपोऽधिके च"
SUTRA_DESC = "(Samjna (technical definitions)) — upo'Dike ca"


class Sutra1487:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_87
		return apply_1_4_87(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-upa-adhika:अग्निः'),
		('रामः', '', 'not-upa-adhika:रामः'),
		('सीता', '', 'not-upa-adhika:सीता'),
	]

