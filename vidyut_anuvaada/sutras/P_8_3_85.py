# Sutra प.8.3.85: मातुःपितुर्भ्यामन्यतरस्याम्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.85"
SUTRA_TEXT = "मातुःपितुर्भ्यामन्यतरस्याम्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8385:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.85: अग्निः'),
		('रामः', '', 'प.8.3.85: रामः'),
		('सीता', '', 'प.8.3.85: सीता'),
	]

