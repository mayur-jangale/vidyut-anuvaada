# Sutra प.2.4.57: वा यौ
# (Samasa (compound formation)) — vA yO

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.57"
SUTRA_TEXT = "वा यौ"
SUTRA_DESC = "(Samasa (compound formation)) — vA yO"


class Sutra2457:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

