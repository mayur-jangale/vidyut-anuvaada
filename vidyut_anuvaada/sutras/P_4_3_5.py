# Sutra प.4.3.5: परावराधमोत्तमपूर्वाच्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — parAvarADamottamapUrvAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.5"
SUTRA_TEXT = "परावराधमोत्तमपूर्वाच्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — parAvarADamottamapUrvAcca"


class Sutra435:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.5: अग्निः'),
		('रामः', '', 'प.4.3.5: रामः'),
		('सीता', '', 'प.4.3.5: सीता'),
	]

