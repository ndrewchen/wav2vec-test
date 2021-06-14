# wav2vec-test
Followed this [wav2vec2 tutorial](https://www.kdnuggets.com/2021/03/speech-text-wav2vec.html) and added my own [3 wav file tests](https://github.com/achen4290/ForcedAligner/tree/master/tests) from my flask implementation of Forced Alignment. Actual transcript and wave2vec2 output shown below:

**taken_clip.wav:**  
Transcript: I will look for you, I will find you and I will kill you  
wav2vec2: I WILL LOOK FOR YOU I WILL FIND YOU  AND I WILL KILL YOU

**test1.wav**  
Transcript: Hello, my name is Andrew. Nice to meet you.  
wav2vec2: HULLO MY NAME IS ANDREW NICE TO MEET YOU

**test2.wav**
Transcript: Expanding on a 1908 paper by Smoluchowski, he derived a formula for the intensity of scattered light in media fluctuating densities that reduces to Rayleigh's law for ideal gases in The Theory of the Opalescence of Homogenous Fluids and Liquid Mixtures near the Critical State. That research supported his theories of matter first developed when he calculated the diffusion constant in terms of fundamental parameters of the particles of a gas undergoing Brownian Motion. In that same year, 1905, he also published On a Heuristic Point of View Concerning the Production and Transformation of Light. That explication of the photoelectric effect won him 1921 Nobel in Physics. For ten points, name this German physicist best known for his theory of Relativity.  
wav2vec2: EXPANDING ON A NINETEEN O EIGHT PAPER BY SMOLUCHOWSKY HE DERIVED OF FORMULA FOR THE INTENSITY OF SCATTERED LIGHT AND MEDIOFLUCTUATING DENSITIES THAT REDUCES TO REALIZE LAW FOR IDEAL GASES IN THE THEORY OF THE OPOLESCENCE OF HOMOGENEOUS FLUIDS AN LIQUID MIXTURES NEAR THE CRITICAL STATE THAT RESEARCH SUPPORTED HIS THEORIES OF MATTER FIRST DEVELOPED WHEN HE CALCULATED THE DIFFUSION CONSTANT IN TERMS OF FUNDAMENTAL PERAMETERS OF THE PARTICLES OF A GAS UNDERGOING BROWNIAN MOTION IN THAT SAME YEAR NINETEEN O FIVE HE ALSO PUBLISHED ON A HEURISTIC POINT OF VIEW CONCERNING THE PRODUCTION AND TRANSFORMATION OF LIGHT THAT EXPLICATION OF THE PHOTOELECTRIC EFFECT WON HYM NINETEEN TWENTY ONE NOBELL AND PHYSICS FOR TEN POINTS NAMED THIS GERMAN PHYSICIST BEST KNOWN FOR HIS THEORY OF RELATIVITY  

**test3.wav**  
Transcript: How is the weather today? It is sunny with a chance of meatballs.  
wav2vec2: HOW IS THE WEATHER TO DAY IT IS SUNNY WITH A CHANCE OF MEAT BALLS
