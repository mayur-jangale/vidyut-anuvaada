# Sutra प.6.3.83: प्रकृत्याऽऽशिष्यगोवत्सहलेषु
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.83"
SUTRA_TEXT = "प्रकृत्याऽऽशिष्यगोवत्सहलेषु"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6383:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.83: अग्निः'),
		('रामः', '', 'प.6.3.83: रामः'),
		('सीता', '', 'प.6.3.83: सीता'),
	]

