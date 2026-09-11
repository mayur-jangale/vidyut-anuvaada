# Sutra प.4.2.124: जनपदतदवध्योश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — janapadatadavaDyoSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.124"
SUTRA_TEXT = "जनपदतदवध्योश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — janapadatadavaDyoSca"


class Sutra42124:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.124: अग्निः'),
		('रामः', '', 'प.4.2.124: रामः'),
		('सीता', '', 'प.4.2.124: सीता'),
	]

