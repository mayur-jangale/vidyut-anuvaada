# Sutra प.4.1.157: उदीचां वृद्धादगोत्रात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — udIcAM vfdDAdagotrAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.157"
SUTRA_TEXT = "उदीचां वृद्धादगोत्रात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — udIcAM vfdDAdagotrAt"


class Sutra41157:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

