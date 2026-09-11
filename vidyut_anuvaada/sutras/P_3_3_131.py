# Sutra प.3.3.131: वर्तमानसामीप्ये वर्तमानवद्वा
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — vartamAnasAmIpye vartamAnavadvA

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.131"
SUTRA_TEXT = "वर्तमानसामीप्ये वर्तमानवद्वा"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — vartamAnasAmIpye vartamAnavadvA"


class Sutra33131:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

