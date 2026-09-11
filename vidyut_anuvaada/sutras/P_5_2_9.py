# Sutra प.5.2.9: अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.9"
SUTRA_TEXT = "अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु"
SUTRA_DESC = "taddhita — continued"


class Sutra529:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.9: अग्निः'),
		('रामः', '', 'प.5.2.9: रामः'),
		('सीता', '', 'प.5.2.9: सीता'),
	]

