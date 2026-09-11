# Sutra प.4.4.16: भस्त्रादिभ्यः ष्ठन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — BastrAdiByaH zWan

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.16"
SUTRA_TEXT = "भस्त्रादिभ्यः ष्ठन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — BastrAdiByaH zWan"


class Sutra4416:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.16: अग्निः'),
		('रामः', '', 'प.4.4.16: रामः'),
		('सीता', '', 'प.4.4.16: सीता'),
	]

