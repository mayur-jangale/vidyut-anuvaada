# Sutra प.3.4.10: प्रयै रोहिष्यै अव्यथिष्यै
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — prayE rohizyE avyaTizyE

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.10"
SUTRA_TEXT = "प्रयै रोहिष्यै अव्यथिष्यै"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — prayE rohizyE avyaTizyE"


class Sutra3410:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

