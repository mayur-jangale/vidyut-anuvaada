# Sutra प.4.3.24: विभाषा पूर्वाह्णापराह्णाभ्याम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — viBAzA pUrvAhRAparAhRAByAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.24"
SUTRA_TEXT = "विभाषा पूर्वाह्णापराह्णाभ्याम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — viBAzA pUrvAhRAparAhRAByAm"


class Sutra4324:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.24: अग्निः'),
		('रामः', '', 'प.4.3.24: रामः'),
		('सीता', '', 'प.4.3.24: सीता'),
	]

