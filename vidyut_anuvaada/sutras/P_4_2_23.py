# Sutra प.4.2.23: विभाषा फाल्गुनीश्रवणाकार्त्तिकीचैत्रीभ्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — viBAzA PAlgunISravaRAkArttikIcEtrIByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.23"
SUTRA_TEXT = "विभाषा फाल्गुनीश्रवणाकार्त्तिकीचैत्रीभ्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — viBAzA PAlgunISravaRAkArttikIcEtrIByaH"


class Sutra4223:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.23: अग्निः'),
		('रामः', '', 'प.4.2.23: रामः'),
		('सीता', '', 'प.4.2.23: सीता'),
	]

