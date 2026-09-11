# Sutra प.6.2.129: कूलसूदस्थलकर्षाः संज्ञायाम्
# (Sandhi (euphonic combination)) — kUlasUdasTalakarzAH saMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.129"
SUTRA_TEXT = "कूलसूदस्थलकर्षाः संज्ञायाम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — kUlasUdasTalakarzAH saMjYAyAm"


class Sutra62129:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.129: अग्निः'),
		('रामः', '', 'प.6.2.129: रामः'),
		('सीता', '', 'प.6.2.129: सीता'),
	]

