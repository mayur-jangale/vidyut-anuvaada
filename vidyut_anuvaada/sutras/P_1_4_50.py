# Sutra प.1.4.50: तथायुक्तं चानीप्सितम्
# (Samjna (technical definitions)) — taTAyuktaM cAnIpsitam

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.50"
SUTRA_TEXT = "तथायुक्तं चानीप्सितम्"
SUTRA_DESC = "(Samjna (technical definitions)) — taTAyuktaM cAnIpsitam"


class Sutra1450:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_50
		return apply_1_4_50(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'maybe-karman:अग्निः'),
		('रामः', '', 'maybe-karman:रामः'),
		('सीता', '', 'maybe-karman:सीता'),
	]

