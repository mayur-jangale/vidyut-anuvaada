# Sutra प.3.2.71: मन्त्रे श्वेतवहोक्थशस्पुरोडाशो ण्विन्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — mantre SvetavahokTaSaspuroqASo Rvin

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.71"
SUTRA_TEXT = "मन्त्रे श्वेतवहोक्थशस्पुरोडाशो ण्विन्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — mantre SvetavahokTaSaspuroqASo Rvin"


class Sutra3271:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

