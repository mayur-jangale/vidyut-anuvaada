# Sutra प.6.2.42: कुरुगार्हपतरिक्तगुर्वसूतजरत्यश्लीलदृढरूपापारेवडवातैतिलकद्रूःपण्यकम्बलो दासीभाराणां च
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.42"
SUTRA_TEXT = "कुरुगार्हपतरिक्तगुर्वसूतजरत्यश्लीलदृढरूपापारेवडवातैतिलकद्रूःपण्यकम्बलो दासीभाराणां च"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6242:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.42: अग्निः'),
		('रामः', '', 'प.6.2.42: रामः'),
		('सीता', '', 'प.6.2.42: सीता'),
	]

