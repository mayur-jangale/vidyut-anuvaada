# Sutra प.3.4.9: तुमर्थे सेसेनसेऽसेन्क्सेकसेनध्यैअध्यैन्कध्यैकध्यैन्शध्यैशध्यैन्तवैतवेङ्तवेनः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — tumarTe sesenase'senksekasenaDyEaDyEnkaDyEkaDyEnSaDyESaDyEntavEtaveNtavenaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.9"
SUTRA_TEXT = "तुमर्थे सेसेनसेऽसेन्क्सेकसेनध्यैअध्यैन्कध्यैकध्यैन्शध्यैशध्यैन्तवैतवेङ्तवेनः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — tumarTe sesenase'senksekasenaDyEaDyEnkaDyEkaDyEnSaDyESaDyEntavEtaveNtavenaH"


class Sutra349:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

