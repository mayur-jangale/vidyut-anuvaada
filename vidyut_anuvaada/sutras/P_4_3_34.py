# Sutra प.4.3.34: श्रविष्ठाफल्गुन्यनुराधास्वातितिष्यपुनर्वसुहस्तविशाखाषाढाबहुलाल्लुक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SravizWAPalgunyanurADAsvAtitizyapunarvasuhastaviSAKAzAQAbahulAlluk

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.34"
SUTRA_TEXT = "श्रविष्ठाफल्गुन्यनुराधास्वातितिष्यपुनर्वसुहस्तविशाखाषाढाबहुलाल्लुक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SravizWAPalgunyanurADAsvAtitizyapunarvasuhastaviSAKAzAQAbahulAlluk"


class Sutra4334:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.34: अग्निः'),
		('रामः', '', 'प.4.3.34: रामः'),
		('सीता', '', 'प.4.3.34: सीता'),
	]

