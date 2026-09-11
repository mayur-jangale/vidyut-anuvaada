# Sutra प.4.2.136: गोयवाग्वोश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — goyavAgvoSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.136"
SUTRA_TEXT = "गोयवाग्वोश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — goyavAgvoSca"


class Sutra42136:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.136: अग्निः'),
		('रामः', '', 'प.4.2.136: रामः'),
		('सीता', '', 'प.4.2.136: सीता'),
	]

