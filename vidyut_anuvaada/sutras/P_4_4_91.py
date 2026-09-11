# Sutra प.4.4.91: नौवयोधर्मविषमूलमूलसीतातुलाभ्यस्तार्यतुल्यप्राप्यवध्यानाम्यसमसमितसम्मितेषु
# (Sup-sthāna (nominal endings) and kṛt-affixes) — nOvayoDarmavizamUlamUlasItAtulAByastAryatulyaprApyavaDyAnAmyasamasamitasammitezu

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.91"
SUTRA_TEXT = "नौवयोधर्मविषमूलमूलसीतातुलाभ्यस्तार्यतुल्यप्राप्यवध्यानाम्यसमसमितसम्मितेषु"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — nOvayoDarmavizamUlamUlasItAtulAByastAryatulyaprApyavaDyAnAmyasamasamitasammitezu"


class Sutra4491:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.91: अग्निः'),
		('रामः', '', 'प.4.4.91: रामः'),
		('सीता', '', 'प.4.4.91: सीता'),
	]

