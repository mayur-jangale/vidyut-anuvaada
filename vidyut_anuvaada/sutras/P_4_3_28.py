# Sutra प.4.3.28: पूर्वाह्णापराह्णार्द्रामूलप्रदोषावस्कराद्वुन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — pUrvAhRAparAhRArdrAmUlapradozAvaskarAdvun

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.28"
SUTRA_TEXT = "पूर्वाह्णापराह्णार्द्रामूलप्रदोषावस्कराद्वुन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — pUrvAhRAparAhRArdrAmUlapradozAvaskarAdvun"


class Sutra4328:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.28: अग्निः'),
		('रामः', '', 'प.4.3.28: रामः'),
		('सीता', '', 'प.4.3.28: सीता'),
	]

