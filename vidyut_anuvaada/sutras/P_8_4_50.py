# Sutra प.8.4.50: त्रिप्रभृतिषु शाकटायनस्य
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.50"
SUTRA_TEXT = "त्रिप्रभृतिषु शाकटायनस्य"
SUTRA_DESC = "final transformations — continued"


class Sutra8450:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.50: अग्निः'),
		('रामः', '', 'प.8.4.50: रामः'),
		('सीता', '', 'प.8.4.50: सीता'),
	]

