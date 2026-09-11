# Sutra प.4.4.114: सगर्भसयूथसनुताद्यन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — sagarBasayUTasanutAdyan

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.114"
SUTRA_TEXT = "सगर्भसयूथसनुताद्यन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — sagarBasayUTasanutAdyan"


class Sutra44114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.114: अग्निः'),
		('रामः', '', 'प.4.4.114: रामः'),
		('सीता', '', 'प.4.4.114: सीता'),
	]

