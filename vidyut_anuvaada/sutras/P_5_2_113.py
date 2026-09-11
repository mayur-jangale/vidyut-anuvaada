# Sutra प.5.2.113: दन्तशिखात् संज्ञायाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dantaSiKAt saMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.113"
SUTRA_TEXT = "दन्तशिखात् संज्ञायाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dantaSiKAt saMjYAyAm"


class Sutra52113:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.113: अग्निः'),
		('रामः', '', 'प.5.2.113: रामः'),
		('सीता', '', 'प.5.2.113: सीता'),
	]

