# Sutra प.1.2.46: कृत्तद्धितसमासाश्च
# (Samjna (technical definitions)) — kfttadDitasamAsASca

from P_1_2 import apply_1_2_46

SUTRA_CODE = "प.1.2.46"
SUTRA_TEXT = "कृत्तद्धितसमासाश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — kfttadDitasamAsASca"


class Sutra1246:
	def apply(self, word, pos):
		return apply_1_2_46(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-prātipadika:अग्निः'),
		('रामः', '', 'non-prātipadika:रामः'),
		('सीता', '', 'non-prātipadika:सीता'),
	]

