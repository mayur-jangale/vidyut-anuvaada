# Sutra प.7.3.36: अर्तिह्रीव्लीरीक्नूयीक्ष्माय्यातां पुङ्णौ
# (Taddhita (secondary derivations)) — artihrIvlIrIknUyIkzmAyyAtAM puNRO

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.36"
SUTRA_TEXT = "अर्तिह्रीव्लीरीक्नूयीक्ष्माय्यातां पुङ्णौ"
SUTRA_DESC = "(Taddhita (secondary derivations)) — artihrIvlIrIknUyIkzmAyyAtAM puNRO"


class Sutra7336:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.36: अग्निः'),
		('रामः', '', 'प.7.3.36: रामः'),
		('सीता', '', 'प.7.3.36: सीता'),
	]

