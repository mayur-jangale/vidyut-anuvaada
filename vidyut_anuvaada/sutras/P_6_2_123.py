# Sutra प.6.2.123: तत्पुरुषे शालायां नपुंसके
# (Sandhi (euphonic combination)) — tatpuruze SAlAyAM napuMsake

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.123"
SUTRA_TEXT = "तत्पुरुषे शालायां नपुंसके"
SUTRA_DESC = "(Sandhi (euphonic combination)) — tatpuruze SAlAyAM napuMsake"


class Sutra62123:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.123: अग्निः'),
		('रामः', '', 'प.6.2.123: रामः'),
		('सीता', '', 'प.6.2.123: सीता'),
	]

