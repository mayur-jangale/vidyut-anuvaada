# Sutra प.1.1.27: सर्वादीनि सर्वनामानि
# (Samjna (technical definitions)) — sarvAdIni sarvanAmAni

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.27"
SUTRA_TEXT = "सर्वादीनि सर्वनामानि"
SUTRA_DESC = "(Samjna (technical definitions)) — sarvAdIni sarvanAmAni"


class Sutra1127:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_27
		return apply_1_1_27(word, pos)

	EXAMPLES = [
		('सर्व', '', 'sarvanāma:सर्व'),
		('उभय', '', 'sarvanāma:उभय'),
		('देवः', '', 'non-sarvanāma:देवः'),
	]

