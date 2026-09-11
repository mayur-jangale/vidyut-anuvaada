# Sutra प.8.3.87: उपसर्गप्रादुर्भ्यामस्तिर्यच्परः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.87"
SUTRA_TEXT = "उपसर्गप्रादुर्भ्यामस्तिर्यच्परः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8387:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.87: अग्निः'),
		('रामः', '', 'प.8.3.87: रामः'),
		('सीता', '', 'प.8.3.87: सीता'),
	]

