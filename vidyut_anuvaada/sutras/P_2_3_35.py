# Sutra प.2.3.35: दूरान्तिकार्थेभ्यो द्वितीया च
# (Samasa (compound formation)) — dUrAntikArTeByo dvitIyA ca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.35"
SUTRA_TEXT = "दूरान्तिकार्थेभ्यो द्वितीया च"
SUTRA_DESC = "(Samasa (compound formation)) — dUrAntikArTeByo dvitIyA ca"


class Sutra2335:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

