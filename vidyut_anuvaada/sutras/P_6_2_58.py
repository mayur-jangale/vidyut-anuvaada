# Sutra प.6.2.58: आर्यो ब्राह्मणकुमारयोः
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.58"
SUTRA_TEXT = "आर्यो ब्राह्मणकुमारयोः"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6258:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.58: अग्निः'),
		('रामः', '', 'प.6.2.58: रामः'),
		('सीता', '', 'प.6.2.58: सीता'),
	]

