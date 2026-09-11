# Sutra प.2.2.37: वाहिताग्न्यादिषु
# (Samasa (compound formation)) — vAhitAgnyAdizu

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.37"
SUTRA_TEXT = "वाहिताग्न्यादिषु"
SUTRA_DESC = "(Samasa (compound formation)) — vAhitAgnyAdizu"


class Sutra2237:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

