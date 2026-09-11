# Sutra प.3.4.43: कर्त्रोर्जीवपुरुषयोर्नशिवहोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kartrorjIvapuruzayornaSivahoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.43"
SUTRA_TEXT = "कर्त्रोर्जीवपुरुषयोर्नशिवहोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kartrorjIvapuruzayornaSivahoH"


class Sutra3443:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

