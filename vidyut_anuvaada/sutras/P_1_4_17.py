# Sutra प.1.4.17: स्वादिष्वसर्वनामस्थाने
# (Samjna (technical definitions)) — svAdizvasarvanAmasTAne

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.17"
SUTRA_TEXT = "स्वादिष्वसर्वनामस्थाने"
SUTRA_DESC = "(Samjna (technical definitions)) — svAdizvasarvanAmasTAne"


class Sutra1417:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_17
		return apply_1_4_17(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-svAdi:अग्निः'),
		('रामः', '', 'not-svAdi:रामः'),
		('सीता', '', 'not-svAdi:सीता'),
	]

