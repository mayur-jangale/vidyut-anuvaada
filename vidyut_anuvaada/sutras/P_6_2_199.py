# Sutra प.6.2.199: परादिश्छन्दसि बहुलम्
# (Sandhi (euphonic combination)) — parAdiSCandasi bahulam

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.199"
SUTRA_TEXT = "परादिश्छन्दसि बहुलम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — parAdiSCandasi bahulam"


class Sutra62199:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.199: अग्निः'),
		('रामः', '', 'प.6.2.199: रामः'),
		('सीता', '', 'प.6.2.199: सीता'),
	]

