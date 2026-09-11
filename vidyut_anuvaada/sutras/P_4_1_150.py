# Sutra प.4.1.150: फाण्टाहृतिमिमताभ्यां णफिञौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — PARwAhftimimatAByAM RaPiYO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.150"
SUTRA_TEXT = "फाण्टाहृतिमिमताभ्यां णफिञौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — PARwAhftimimatAByAM RaPiYO"


class Sutra41150:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

