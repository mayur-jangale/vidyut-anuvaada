# Sutra प.4.3.168: कंसीयपरशव्ययोर्यञञौ लुक् च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kaMsIyaparaSavyayoryaYaYO luk ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.168"
SUTRA_TEXT = "कंसीयपरशव्ययोर्यञञौ लुक् च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kaMsIyaparaSavyayoryaYaYO luk ca"


class Sutra43168:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.168: अग्निः'),
		('रामः', '', 'प.4.3.168: रामः'),
		('सीता', '', 'प.4.3.168: सीता'),
	]

