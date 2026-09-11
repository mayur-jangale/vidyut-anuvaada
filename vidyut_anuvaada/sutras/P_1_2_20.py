# Sutra प.1.2.20: मृषस्तितिक्षायाम्
# (Samjna (technical definitions)) — mfzastitikzAyAm

from P_1_2 import apply_1_2_20

SUTRA_CODE = "प.1.2.20"
SUTRA_TEXT = "मृषस्तितिक्षायाम्"
SUTRA_DESC = "(Samjna (technical definitions)) — mfzastitikzAyAm"


class Sutra1220:
	def apply(self, word, pos):
		return apply_1_2_20(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-mṛṣ:अग्निः'),
		('रामः', '', 'non-mṛṣ:रामः'),
		('सीता', '', 'non-mṛṣ:सीता'),
	]

