# Sutra प.4.2.107: दिक्पूर्वपदादसंज्ञायां ञः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — dikpUrvapadAdasaMjYAyAM YaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.107"
SUTRA_TEXT = "दिक्पूर्वपदादसंज्ञायां ञः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — dikpUrvapadAdasaMjYAyAM YaH"


class Sutra42107:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.107: अग्निः'),
		('रामः', '', 'प.4.2.107: रामः'),
		('सीता', '', 'प.4.2.107: सीता'),
	]

