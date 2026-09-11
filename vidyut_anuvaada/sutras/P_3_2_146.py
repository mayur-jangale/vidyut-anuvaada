# Sutra प.3.2.146: निन्दहिंसक्लिशखादविनाशपरिक्षिपपरिरटपरिवादिव्याभाषासूञो वुञ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — nindahiMsakliSaKAdavinASaparikzipaparirawaparivAdivyABAzAsUYo vuY

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.146"
SUTRA_TEXT = "निन्दहिंसक्लिशखादविनाशपरिक्षिपपरिरटपरिवादिव्याभाषासूञो वुञ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — nindahiMsakliSaKAdavinASaparikzipaparirawaparivAdivyABAzAsUYo vuY"


class Sutra32146:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

