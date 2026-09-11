# Sutra प.1.2.66: स्त्री पुंवच्च
# (Samjna (technical definitions)) — strI puMvacca

from P_1_2 import apply_1_2_66

SUTRA_CODE = "प.1.2.66"
SUTRA_TEXT = "स्त्री पुंवच्च"
SUTRA_DESC = "(Samjna (technical definitions)) — strI puMvacca"


class Sutra1266:
	def apply(self, word, pos):
		return apply_1_2_66(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-strī:अग्निः'),
		('रामः', '', 'non-strī:रामः'),
		('सीता', '', 'non-strī:सीता'),
	]

