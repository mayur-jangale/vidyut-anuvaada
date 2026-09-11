# Sutra प.7.1.67: उपसर्गात् खल्घञोः
# (Taddhita (secondary derivations)) — upasargAt KalGaYoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.67"
SUTRA_TEXT = "उपसर्गात् खल्घञोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — upasargAt KalGaYoH"


class Sutra7167:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.67: अग्निः'),
		('रामः', '', 'प.7.1.67: रामः'),
		('सीता', '', 'प.7.1.67: सीता'),
	]

