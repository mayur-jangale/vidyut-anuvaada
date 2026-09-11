# Sutra प.4.3.86: अभिनिष्क्रामति द्वारम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — aBinizkrAmati dvAram

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.86"
SUTRA_TEXT = "अभिनिष्क्रामति द्वारम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — aBinizkrAmati dvAram"


class Sutra4386:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.86: अग्निः'),
		('रामः', '', 'प.4.3.86: रामः'),
		('सीता', '', 'प.4.3.86: सीता'),
	]

