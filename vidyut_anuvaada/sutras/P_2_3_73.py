# Sutra प.2.3.73: चतुर्थी चाशिष्यायुष्यमद्रभद्रकुशलसुखार्थहितैः
# (Samasa (compound formation)) — caturTI cASizyAyuzyamadraBadrakuSalasuKArTahitEH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.73"
SUTRA_TEXT = "चतुर्थी चाशिष्यायुष्यमद्रभद्रकुशलसुखार्थहितैः"
SUTRA_DESC = "(Samasa (compound formation)) — caturTI cASizyAyuzyamadraBadrakuSalasuKArTahitEH"


class Sutra2373:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

