# Sutra प.7.4.40: द्यतिस्यतिमास्थामित्ति किति
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.40"
SUTRA_TEXT = "द्यतिस्यतिमास्थामित्ति किति"
SUTRA_DESC = "taddhita — continued"


class Sutra7440:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.40: अग्निः'),
		('रामः', '', 'प.7.4.40: रामः'),
		('सीता', '', 'प.7.4.40: सीता'),
	]

