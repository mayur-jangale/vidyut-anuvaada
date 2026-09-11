# Sutra प.7.3.110: ऋतो ङिसर्वनामस्थानयोः
# (Taddhita (secondary derivations)) — fto NisarvanAmasTAnayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.110"
SUTRA_TEXT = "ऋतो ङिसर्वनामस्थानयोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — fto NisarvanAmasTAnayoH"


class Sutra73110:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.110: अग्निः'),
		('रामः', '', 'प.7.3.110: रामः'),
		('सीता', '', 'प.7.3.110: सीता'),
	]

