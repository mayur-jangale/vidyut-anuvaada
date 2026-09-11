# Sutra प.4.3.123: पत्राध्वर्युपरिषदश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — patrADvaryuparizadaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.123"
SUTRA_TEXT = "पत्राध्वर्युपरिषदश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — patrADvaryuparizadaSca"


class Sutra43123:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.123: अग्निः'),
		('रामः', '', 'प.4.3.123: रामः'),
		('सीता', '', 'प.4.3.123: सीता'),
	]

