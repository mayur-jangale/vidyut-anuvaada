# Sutra प.4.1.168: जनपदशब्दात् क्षत्रियादञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — janapadaSabdAt kzatriyAdaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.168"
SUTRA_TEXT = "जनपदशब्दात् क्षत्रियादञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — janapadaSabdAt kzatriyAdaY"


class Sutra41168:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

