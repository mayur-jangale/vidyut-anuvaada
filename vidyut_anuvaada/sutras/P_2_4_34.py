# Sutra प.2.4.34: द्वितीयाटौस्स्वेनः
# (Samasa (compound formation)) — dvitIyAwOssvenaH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.34"
SUTRA_TEXT = "द्वितीयाटौस्स्वेनः"
SUTRA_DESC = "(Samasa (compound formation)) — dvitIyAwOssvenaH"


class Sutra2434:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

