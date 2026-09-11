# Sutra प.4.2.60: क्रतूक्थादिसूत्रान्ताट्ठक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kratUkTAdisUtrAntAwWak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.60"
SUTRA_TEXT = "क्रतूक्थादिसूत्रान्ताट्ठक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kratUkTAdisUtrAntAwWak"


class Sutra4260:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.60: अग्निः'),
		('रामः', '', 'प.4.2.60: रामः'),
		('सीता', '', 'प.4.2.60: सीता'),
	]

