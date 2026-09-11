# Sutra प.2.3.3: तृतीया च होश्छन्दसि
# (Samasa (compound formation)) — tftIyA ca hoSCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.3"
SUTRA_TEXT = "तृतीया च होश्छन्दसि"
SUTRA_DESC = "(Samasa (compound formation)) — tftIyA ca hoSCandasi"


class Sutra233:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

