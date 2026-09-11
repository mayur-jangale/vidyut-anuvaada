# Sutra प.4.3.62: जिह्वामूलाङ्गुलेश्छः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — jihvAmUlANguleSCaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.62"
SUTRA_TEXT = "जिह्वामूलाङ्गुलेश्छः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — jihvAmUlANguleSCaH"


class Sutra4362:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.62: अग्निः'),
		('रामः', '', 'प.4.3.62: रामः'),
		('सीता', '', 'प.4.3.62: सीता'),
	]

