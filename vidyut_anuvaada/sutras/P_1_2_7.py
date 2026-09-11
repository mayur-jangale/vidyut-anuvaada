# Sutra प.1.2.7: मृडमृदगुधकुषक्लिशवदवसः क्त्वा
# (Samjna (technical definitions)) — mfqamfdaguDakuzakliSavadavasaH ktvA

from P_1_2 import apply_1_2_7

SUTRA_CODE = "प.1.2.7"
SUTRA_TEXT = "मृडमृदगुधकुषक्लिशवदवसः क्त्वा"
SUTRA_DESC = "(Samjna (technical definitions)) — mfqamfdaguDakuzakliSavadavasaH ktvA"


class Sutra127:
	def apply(self, word, pos):
		return apply_1_2_7(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-mṛḍādi:अग्निः'),
		('रामः', '', 'non-mṛḍādi:रामः'),
		('सीता', '', 'non-mṛḍādi:सीता'),
	]

