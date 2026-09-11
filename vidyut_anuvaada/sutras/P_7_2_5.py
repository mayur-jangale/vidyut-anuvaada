# Sutra प.7.2.5: ह्म्यन्तक्षणश्वसजागृणिश्व्येदिताम्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.5"
SUTRA_TEXT = "ह्म्यन्तक्षणश्वसजागृणिश्व्येदिताम्"
SUTRA_DESC = "taddhita — continued"


class Sutra725:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.5: अग्निः'),
		('रामः', '', 'प.7.2.5: रामः'),
		('सीता', '', 'प.7.2.5: सीता'),
	]

