# Sutra प.4.1.165: वान्यस्मिन् सपिण्डे स्थविरतरे जीवति
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vAnyasmin sapiRqe sTaviratare jIvati

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.165"
SUTRA_TEXT = "वान्यस्मिन् सपिण्डे स्थविरतरे जीवति"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vAnyasmin sapiRqe sTaviratare jIvati"


class Sutra41165:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

