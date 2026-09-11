# Sutra प.6.2.198: सक्थं चाक्रान्तात्
# (Sandhi (euphonic combination)) — sakTaM cAkrAntAt

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.198"
SUTRA_TEXT = "सक्थं चाक्रान्तात्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — sakTaM cAkrAntAt"


class Sutra62198:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.198: अग्निः'),
		('रामः', '', 'प.6.2.198: रामः'),
		('सीता', '', 'प.6.2.198: सीता'),
	]

