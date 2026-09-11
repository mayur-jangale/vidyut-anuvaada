# Sutra प.4.1.163: जीवति तु वंश्ये युवा
# (Sup-sthāna (nominal endings) and kṛt-affixes) — jIvati tu vaMSye yuvA

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.163"
SUTRA_TEXT = "जीवति तु वंश्ये युवा"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — jIvati tu vaMSye yuvA"


class Sutra41163:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

