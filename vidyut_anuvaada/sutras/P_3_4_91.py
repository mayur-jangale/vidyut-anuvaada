# Sutra प.3.4.91: सवाभ्यां वामौ
# ardhādhātuka — these endings are ardhādhātuka

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.91"
SUTRA_TEXT = "सवाभ्यां वामौ"
SUTRA_DESC = "ardhādhātuka — these endings are ardhādhātuka"


class Sutra3491:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

