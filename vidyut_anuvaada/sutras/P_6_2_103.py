# Sutra प.6.2.103: दिक्शब्दा ग्रामजनपदाख्यानचानराटेषु
# (Sandhi (euphonic combination)) — dikSabdA grAmajanapadAKyAnacAnarAwezu

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.103"
SUTRA_TEXT = "दिक्शब्दा ग्रामजनपदाख्यानचानराटेषु"
SUTRA_DESC = "(Sandhi (euphonic combination)) — dikSabdA grAmajanapadAKyAnacAnarAwezu"


class Sutra62103:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.103: अग्निः'),
		('रामः', '', 'प.6.2.103: रामः'),
		('सीता', '', 'प.6.2.103: सीता'),
	]

