# Sutra प.4.2.9: वामदेवाड्ड्यड्ड्यौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vAmadevAqqyaqqyO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.9"
SUTRA_TEXT = "वामदेवाड्ड्यड्ड्यौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vAmadevAqqyaqqyO"


class Sutra429:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.9: अग्निः'),
		('रामः', '', 'प.4.2.9: रामः'),
		('सीता', '', 'प.4.2.9: सीता'),
	]

