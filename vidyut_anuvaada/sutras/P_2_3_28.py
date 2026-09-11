# Sutra प.2.3.28: अपादाने पञ्चमी
# (Samasa (compound formation)) — apAdAne paYcamI

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.28"
SUTRA_TEXT = "अपादाने पञ्चमी"
SUTRA_DESC = "(Samasa (compound formation)) — apAdAne paYcamI"


class Sutra2328:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

