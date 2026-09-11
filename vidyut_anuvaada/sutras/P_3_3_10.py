# Sutra प.3.3.10: तुमुन्ण्वुलौ क्रियायां क्रियार्थायाम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — tumunRvulO kriyAyAM kriyArTAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.10"
SUTRA_TEXT = "तुमुन्ण्वुलौ क्रियायां क्रियार्थायाम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — tumunRvulO kriyAyAM kriyArTAyAm"


class Sutra3310:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

