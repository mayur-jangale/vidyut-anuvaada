# Sutra प.8.1.2: तस्य परमाम्रेडितम्
# mo'nusvāraḥ — म् becomes अनुस्वार (ṃ) in certain positions

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.2"
SUTRA_TEXT = "तस्य परमाम्रेडितम्"
SUTRA_DESC = "mo'nusvāraḥ — म् becomes अनुस्वार (ṃ) in certain positions"


class Sutra812:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.2: अग्निः'),
		('रामः', '', 'प.8.1.2: रामः'),
		('सीता', '', 'प.8.1.2: सीता'),
	]

