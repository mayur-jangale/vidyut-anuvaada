# Sutra प.3.3.116: कर्मणि च येन संस्पर्शात् कर्तुः शरीरसुखम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmaRi ca yena saMsparSAt kartuH SarIrasuKam

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.116"
SUTRA_TEXT = "कर्मणि च येन संस्पर्शात् कर्तुः शरीरसुखम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmaRi ca yena saMsparSAt kartuH SarIrasuKam"


class Sutra33116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

