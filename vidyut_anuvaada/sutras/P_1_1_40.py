# Sutra प.1.1.40: क्त्वातोसुन्कसुनः
# (Samjna (technical definitions)) — ktvAtosunkasunaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.40"
SUTRA_TEXT = "क्त्वातोसुन्कसुनः"
SUTRA_DESC = "(Samjna (technical definitions)) — ktvAtosunkasunaH"


class Sutra1140:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_40
		return apply_1_1_40(word, pos)

	EXAMPLES = [
		('क्त्वा', '', 'kṛd-affix:क्त्वा'),
		('तोसुन्', '', 'kṛd-affix:तोसुन्'),
		('दश', '', 'non-kṛd:दश'),
	]

