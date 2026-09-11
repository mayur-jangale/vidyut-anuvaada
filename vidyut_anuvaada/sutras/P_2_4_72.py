# Sutra प.2.4.72: अदिप्रभृतिभ्यः शपः
# (Samasa (compound formation)) — adipraBftiByaH SapaH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.72"
SUTRA_TEXT = "अदिप्रभृतिभ्यः शपः"
SUTRA_DESC = "(Samasa (compound formation)) — adipraBftiByaH SapaH"


class Sutra2472:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

