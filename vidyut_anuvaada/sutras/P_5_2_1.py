# Sutra प.5.2.1: धान्यानां भवने क्षेत्रे खञ्
# taddhita — secondary derivation rules begin

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.1"
SUTRA_TEXT = "धान्यानां भवने क्षेत्रे खञ्"
SUTRA_DESC = "taddhita — secondary derivation rules begin"


class Sutra521:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.1: अग्निः'),
		('रामः', '', 'प.5.2.1: रामः'),
		('सीता', '', 'प.5.2.1: सीता'),
	]

