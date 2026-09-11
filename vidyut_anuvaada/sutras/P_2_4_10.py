# Sutra प.2.4.10: शूद्राणामनिरवसितानाम्
# (Samasa (compound formation)) — SUdrARAmaniravasitAnAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.10"
SUTRA_TEXT = "शूद्राणामनिरवसितानाम्"
SUTRA_DESC = "(Samasa (compound formation)) — SUdrARAmaniravasitAnAm"


class Sutra2410:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

