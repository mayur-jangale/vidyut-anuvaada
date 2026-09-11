# Sutra प.1.1.35: स्वमज्ञातिधनाख्यायाम्
# (Samjna (technical definitions)) — svamajYAtiDanAKyAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.35"
SUTRA_TEXT = "स्वमज्ञातिधनाख्यायाम्"
SUTRA_DESC = "(Samjna (technical definitions)) — svamajYAtiDanAKyAyAm"


class Sutra1135:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_35
		return apply_1_1_35(word, pos)

	EXAMPLES = [
		('स्वम्', 'sva', 'sva-sense:स्वम्'),
		('देव', '', 'non-applicable:देव'),
	]

