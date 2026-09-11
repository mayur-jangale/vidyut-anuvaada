# Sutra प.4.2.128: नगरात् कुत्सनप्रावीण्ययोः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — nagarAt kutsanaprAvIRyayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.128"
SUTRA_TEXT = "नगरात् कुत्सनप्रावीण्ययोः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — nagarAt kutsanaprAvIRyayoH"


class Sutra42128:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.128: अग्निः'),
		('रामः', '', 'प.4.2.128: रामः'),
		('सीता', '', 'प.4.2.128: सीता'),
	]

