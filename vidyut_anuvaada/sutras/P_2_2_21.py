# Sutra प.2.2.21: तृतीयाप्रभृतीन्यन्यतरस्याम्
# (Samasa (compound formation)) — tftIyApraBftInyanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.21"
SUTRA_TEXT = "तृतीयाप्रभृतीन्यन्यतरस्याम्"
SUTRA_DESC = "(Samasa (compound formation)) — tftIyApraBftInyanyatarasyAm"


class Sutra2221:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

