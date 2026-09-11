# Sutra प.2.3.2: कर्मणि द्वितीया
# (Samasa (compound formation)) — karmaRi dvitIyA

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.2"
SUTRA_TEXT = "कर्मणि द्वितीया"
SUTRA_DESC = "(Samasa (compound formation)) — karmaRi dvitIyA"


class Sutra232:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

