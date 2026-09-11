# Sutra प.4.3.103: काश्यपकौशिकाभ्यामृषिभ्यां णिनिः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kASyapakOSikAByAmfziByAM RiniH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.103"
SUTRA_TEXT = "काश्यपकौशिकाभ्यामृषिभ्यां णिनिः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kASyapakOSikAByAmfziByAM RiniH"


class Sutra43103:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.103: अग्निः'),
		('रामः', '', 'प.4.3.103: रामः'),
		('सीता', '', 'प.4.3.103: सीता'),
	]

