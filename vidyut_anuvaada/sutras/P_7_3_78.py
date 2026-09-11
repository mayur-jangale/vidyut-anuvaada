# Sutra प.7.3.78: पाघ्राध्मास्थाम्नादाण्दृश्यर्त्तिसर्त्तिशदसदां पिबजिघ्रधमतिष्ठमनयच्छपश्यर्च्छधौशीयसीदाः
# (Taddhita (secondary derivations)) — pAGrADmAsTAmnAdARdfSyarttisarttiSadasadAM pibajiGraDamatizWamanayacCapaSyarcCaDOSIyasIdAH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.78"
SUTRA_TEXT = "पाघ्राध्मास्थाम्नादाण्दृश्यर्त्तिसर्त्तिशदसदां पिबजिघ्रधमतिष्ठमनयच्छपश्यर्च्छधौशीयसीदाः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — pAGrADmAsTAmnAdARdfSyarttisarttiSadasadAM pibajiGraDamatizWamanayacCapaSyarcCaDOSIyasIdAH"


class Sutra7378:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.78: अग्निः'),
		('रामः', '', 'प.7.3.78: रामः'),
		('सीता', '', 'प.7.3.78: सीता'),
	]

