# Sutra प.8.3.110: न रपरसृपिसृजिस्पृशिस्पृहिसवनादीनाम्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.110"
SUTRA_TEXT = "न रपरसृपिसृजिस्पृशिस्पृहिसवनादीनाम्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra83110:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.110: अग्निः'),
		('रामः', '', 'प.8.3.110: रामः'),
		('सीता', '', 'प.8.3.110: सीता'),
	]

