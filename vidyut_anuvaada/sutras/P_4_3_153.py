# Sutra प.4.3.153: जातरूपेभ्यः परिमाणे
# (Sup-sthāna (nominal endings) and kṛt-affixes) — jAtarUpeByaH parimARe

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.153"
SUTRA_TEXT = "जातरूपेभ्यः परिमाणे"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — jAtarUpeByaH parimARe"


class Sutra43153:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.153: अग्निः'),
		('रामः', '', 'प.4.3.153: रामः'),
		('सीता', '', 'प.4.3.153: सीता'),
	]

