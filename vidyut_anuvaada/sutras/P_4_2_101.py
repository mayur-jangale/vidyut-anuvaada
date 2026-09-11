# Sutra प.4.2.101: द्युप्रागपागुदक्प्रतीचो यत्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — dyuprAgapAgudakpratIco yat

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.101"
SUTRA_TEXT = "द्युप्रागपागुदक्प्रतीचो यत्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — dyuprAgapAgudakpratIco yat"


class Sutra42101:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.101: अग्निः'),
		('रामः', '', 'प.4.2.101: रामः'),
		('सीता', '', 'प.4.2.101: सीता'),
	]

