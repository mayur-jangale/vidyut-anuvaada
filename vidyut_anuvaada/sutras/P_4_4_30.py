# Sutra प.4.4.30: प्रयच्छति गर्ह्यम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — prayacCati garhyam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.30"
SUTRA_TEXT = "प्रयच्छति गर्ह्यम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — prayacCati garhyam"


class Sutra4430:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.30: अग्निः'),
		('रामः', '', 'प.4.4.30: रामः'),
		('सीता', '', 'प.4.4.30: सीता'),
	]

