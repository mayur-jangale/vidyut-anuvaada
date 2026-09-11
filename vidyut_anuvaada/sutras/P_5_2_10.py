# Sutra प.5.2.10: परोवरपरम्परपुत्रपौत्रमनुभवति
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.10"
SUTRA_TEXT = "परोवरपरम्परपुत्रपौत्रमनुभवति"
SUTRA_DESC = "taddhita — continued"


class Sutra5210:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.10: अग्निः'),
		('रामः', '', 'प.5.2.10: रामः'),
		('सीता', '', 'प.5.2.10: सीता'),
	]

