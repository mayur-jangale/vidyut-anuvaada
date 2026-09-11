# Sutra प.3.1.21: मुण्डमिश्रश्लक्ष्णलवणव्रतवस्त्रहलकलकृततूस्तेभ्यो णिच्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — muRqamiSraSlakzRalavaRavratavastrahalakalakftatUsteByo Ric

from P_3_1 import apply_3_1_21

SUTRA_CODE = "प.3.1.21"
SUTRA_TEXT = "मुण्डमिश्रश्लक्ष्णलवणव्रतवस्त्रहलकलकृततूस्तेभ्यो णिच्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — muRqamiSraSlakzRalavaRavratavastrahalakalakftatUsteByo Ric"


class Sutra3121:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_21(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.21:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.21:root=रामः;pos='),
		('सीता', '', 'प.3.1.21:root=सीता;pos='),
	]

