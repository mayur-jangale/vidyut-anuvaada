# Sutra प.4.2.76: स्त्रीषु सौवीरसाल्वप्राक्षु
# (Sup-sthāna (nominal endings) and kṛt-affixes) — strIzu sOvIrasAlvaprAkzu

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.76"
SUTRA_TEXT = "स्त्रीषु सौवीरसाल्वप्राक्षु"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — strIzu sOvIrasAlvaprAkzu"


class Sutra4276:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.76: अग्निः'),
		('रामः', '', 'प.4.2.76: रामः'),
		('सीता', '', 'प.4.2.76: सीता'),
	]

