# Sutra प.4.3.98: वासुदेवार्जुनाभ्यां वुन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vAsudevArjunAByAM vun

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.98"
SUTRA_TEXT = "वासुदेवार्जुनाभ्यां वुन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vAsudevArjunAByAM vun"


class Sutra4398:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.98: अग्निः'),
		('रामः', '', 'प.4.3.98: रामः'),
		('सीता', '', 'प.4.3.98: सीता'),
	]

