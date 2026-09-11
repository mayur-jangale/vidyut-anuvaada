# Sutra प.6.2.6: प्रतिबन्धि चिरकृच्छ्रयोः
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.6"
SUTRA_TEXT = "प्रतिबन्धि चिरकृच्छ्रयोः"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra626:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.6: अग्निः'),
		('रामः', '', 'प.6.2.6: रामः'),
		('सीता', '', 'प.6.2.6: सीता'),
	]

