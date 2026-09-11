# Sutra प.6.3.63: ङ्यापोः संज्ञाछन्दसोर्बहुलम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.63"
SUTRA_TEXT = "ङ्यापोः संज्ञाछन्दसोर्बहुलम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6363:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.63: अग्निः'),
		('रामः', '', 'प.6.3.63: रामः'),
		('सीता', '', 'प.6.3.63: सीता'),
	]

