# Sutra प.1.2.5: असंयोगाल्लिट् कित्
# (Samjna (technical definitions)) — asaMyogAlliw kit

from P_1_2 import apply_1_2_5

SUTRA_CODE = "प.1.2.5"
SUTRA_TEXT = "असंयोगाल्लिट् कित्"
SUTRA_DESC = "(Samjna (technical definitions)) — asaMyogAlliw kit"


class Sutra125:
	def apply(self, word, pos):
		return apply_1_2_5(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-liṭ:अग्निः'),
		('रामः', '', 'non-liṭ:रामः'),
		('सीता', '', 'non-liṭ:सीता'),
	]

