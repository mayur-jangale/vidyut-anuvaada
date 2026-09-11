# Sutra प.2.3.40: आयुक्तकुशलाभ्यां चासेवायाम्
# (Samasa (compound formation)) — AyuktakuSalAByAM cAsevAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.40"
SUTRA_TEXT = "आयुक्तकुशलाभ्यां चासेवायाम्"
SUTRA_DESC = "(Samasa (compound formation)) — AyuktakuSalAByAM cAsevAyAm"


class Sutra2340:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

