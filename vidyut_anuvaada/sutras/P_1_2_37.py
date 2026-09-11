# Sutra प.1.2.37: न सुब्रह्मण्यायां स्वरितस्य तूदात्तः
# (Samjna (technical definitions)) — na subrahmaRyAyAM svaritasya tUdAttaH

from P_1_2 import apply_1_2_37

SUTRA_CODE = "प.1.2.37"
SUTRA_TEXT = "न सुब्रह्मण्यायां स्वरितस्य तूदात्तः"
SUTRA_DESC = "(Samjna (technical definitions)) — na subrahmaRyAyAM svaritasya tUdAttaH"


class Sutra1237:
	def apply(self, word, pos):
		return apply_1_2_37(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-subrahmaṇyā:अग्निः'),
		('रामः', '', 'non-subrahmaṇyā:रामः'),
		('सीता', '', 'non-subrahmaṇyā:सीता'),
	]

