# Sutra प.4.2.126: कच्छाग्निवक्त्रवर्त्तोत्तरपदात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kacCAgnivaktravarttottarapadAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.126"
SUTRA_TEXT = "कच्छाग्निवक्त्रवर्त्तोत्तरपदात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kacCAgnivaktravarttottarapadAt"


class Sutra42126:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.126: अग्निः'),
		('रामः', '', 'प.4.2.126: रामः'),
		('सीता', '', 'प.4.2.126: सीता'),
	]

