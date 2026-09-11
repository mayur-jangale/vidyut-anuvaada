# Sutra प.6.2.182: परेरभितोभाविमण्डलम्
# (Sandhi (euphonic combination)) — pareraBitoBAvimaRqalam

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.182"
SUTRA_TEXT = "परेरभितोभाविमण्डलम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — pareraBitoBAvimaRqalam"


class Sutra62182:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.182: अग्निः'),
		('रामः', '', 'प.6.2.182: रामः'),
		('सीता', '', 'प.6.2.182: सीता'),
	]

