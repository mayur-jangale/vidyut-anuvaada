# Sutra प.1.2.59: अस्मदो द्वयोश्च
# (Samjna (technical definitions)) — asmado dvayoSca

from P_1_2 import apply_1_2_59

SUTRA_CODE = "प.1.2.59"
SUTRA_TEXT = "अस्मदो द्वयोश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — asmado dvayoSca"


class Sutra1259:
	def apply(self, word, pos):
		return apply_1_2_59(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-asmad:अग्निः'),
		('रामः', '', 'non-asmad:रामः'),
		('सीता', '', 'non-asmad:सीता'),
	]

