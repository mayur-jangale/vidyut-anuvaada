# Sutra प.3.2.57: कर्तरि भुवः खिष्णुच्खुकञौ
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kartari BuvaH KizRucKukaYO

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.57"
SUTRA_TEXT = "कर्तरि भुवः खिष्णुच्खुकञौ"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kartari BuvaH KizRucKukaYO"


class Sutra3257:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

