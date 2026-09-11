# Sutra प.4.3.61: ग्रामात् पर्यनुपूर्वात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — grAmAt paryanupUrvAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.61"
SUTRA_TEXT = "ग्रामात् पर्यनुपूर्वात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — grAmAt paryanupUrvAt"


class Sutra4361:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.61: अग्निः'),
		('रामः', '', 'प.4.3.61: रामः'),
		('सीता', '', 'प.4.3.61: सीता'),
	]

