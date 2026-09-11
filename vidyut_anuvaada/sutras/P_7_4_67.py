# Sutra प.7.4.67: द्युतिस्वाप्योः सम्प्रसारणम्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.67"
SUTRA_TEXT = "द्युतिस्वाप्योः सम्प्रसारणम्"
SUTRA_DESC = "taddhita — continued"


class Sutra7467:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.67: अग्निः'),
		('रामः', '', 'प.7.4.67: रामः'),
		('सीता', '', 'प.7.4.67: सीता'),
	]

