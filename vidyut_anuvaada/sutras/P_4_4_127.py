# Sutra प.4.4.127: वयस्यासु मूर्ध्नो मतुप्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vayasyAsu mUrDno matup

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.127"
SUTRA_TEXT = "वयस्यासु मूर्ध्नो मतुप्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vayasyAsu mUrDno matup"


class Sutra44127:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.127: अग्निः'),
		('रामः', '', 'प.4.4.127: रामः'),
		('सीता', '', 'प.4.4.127: सीता'),
	]

