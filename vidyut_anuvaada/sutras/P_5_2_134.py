# Sutra प.5.2.134: वर्णाद्ब्रह्मचारिणि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — varRAdbrahmacAriRi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.134"
SUTRA_TEXT = "वर्णाद्ब्रह्मचारिणि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — varRAdbrahmacAriRi"


class Sutra52134:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.134: अग्निः'),
		('रामः', '', 'प.5.2.134: रामः'),
		('सीता', '', 'प.5.2.134: सीता'),
	]

