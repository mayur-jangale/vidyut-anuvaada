# Sutra प.2.4.7: विशिष्टलिङ्गो नदी देशोऽग्रामाः
# (Samasa (compound formation)) — viSizwaliNgo nadI deSo'grAmAH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.7"
SUTRA_TEXT = "विशिष्टलिङ्गो नदी देशोऽग्रामाः"
SUTRA_DESC = "(Samasa (compound formation)) — viSizwaliNgo nadI deSo'grAmAH"


class Sutra247:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

