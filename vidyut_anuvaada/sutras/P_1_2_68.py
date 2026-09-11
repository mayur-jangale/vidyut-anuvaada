# Sutra प.1.2.68: भ्रातृपुत्रौ स्वसृदुहितृभ्याम्
# (Samjna (technical definitions)) — BrAtfputrO svasfduhitfByAm

from P_1_2 import apply_1_2_68

SUTRA_CODE = "प.1.2.68"
SUTRA_TEXT = "भ्रातृपुत्रौ स्वसृदुहितृभ्याम्"
SUTRA_DESC = "(Samjna (technical definitions)) — BrAtfputrO svasfduhitfByAm"


class Sutra1268:
	def apply(self, word, pos):
		return apply_1_2_68(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-bhrātṛ:अग्निः'),
		('रामः', '', 'non-bhrātṛ:रामः'),
		('सीता', '', 'non-bhrātṛ:सीता'),
	]

