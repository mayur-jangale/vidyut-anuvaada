# Sutra प.2.3.10: पञ्चम्यपाङ्परिभिः
# (Samasa (compound formation)) — paYcamyapANpariBiH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.10"
SUTRA_TEXT = "पञ्चम्यपाङ्परिभिः"
SUTRA_DESC = "(Samasa (compound formation)) — paYcamyapANpariBiH"


class Sutra2310:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

