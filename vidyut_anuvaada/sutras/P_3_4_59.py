# Sutra प.3.4.59: अव्ययेऽयथाभिप्रेताख्याने कृञः क्त्वाणमुलौ
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — avyaye'yaTABipretAKyAne kfYaH ktvARamulO

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.59"
SUTRA_TEXT = "अव्ययेऽयथाभिप्रेताख्याने कृञः क्त्वाणमुलौ"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — avyaye'yaTABipretAKyAne kfYaH ktvARamulO"


class Sutra3459:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

