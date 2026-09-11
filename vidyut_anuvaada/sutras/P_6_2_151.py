# Sutra प.6.2.151: मन्क्तिन्व्याख्यानशयनासनस्थानयाजकादिक्रीताः
# (Sandhi (euphonic combination)) — manktinvyAKyAnaSayanAsanasTAnayAjakAdikrItAH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.151"
SUTRA_TEXT = "मन्क्तिन्व्याख्यानशयनासनस्थानयाजकादिक्रीताः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — manktinvyAKyAnaSayanAsanasTAnayAjakAdikrItAH"


class Sutra62151:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.151: अग्निः'),
		('रामः', '', 'प.6.2.151: रामः'),
		('सीता', '', 'प.6.2.151: सीता'),
	]

