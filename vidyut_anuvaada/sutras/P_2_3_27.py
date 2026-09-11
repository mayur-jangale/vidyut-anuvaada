# Sutra प.2.3.27: सर्वनाम्नस्तृतीया च
# (Samasa (compound formation)) — sarvanAmnastftIyA ca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.27"
SUTRA_TEXT = "सर्वनाम्नस्तृतीया च"
SUTRA_DESC = "(Samasa (compound formation)) — sarvanAmnastftIyA ca"


class Sutra2327:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

