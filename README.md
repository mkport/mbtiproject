# mbtiproject
## Introduction, Use Terms
This is a personal project analyzing the personality types of the top 250 Anime & Manga characters on [Personality Database](https://www.personality-database.com/). <br />
On this website, users can vote for a character's personality type. It includes many different tests such as MBTI, Enneagram, etc. <br />
The data was collected myself via manual input from July 2023. <br />
The data is collected from votes, so some of the data may have changed from when I have collected it. <br />
If you use the data, please keep the above in mind and take care in cleaning the data for proper analysis. <br />
Please use these project files for learning purposes only. Please do not claim the files as your own. <br />
Please do not use the information in the following Summary section as a source for official work, as I am not an expert in personality tests. Please use trusted resources instead. <br />
## Summary of Personality Type Tests
I did research on the personality tests for this project using Google. Please keep in mind that I am not an expert in them, but I hope this summary is helpful for understanding the project. <br /> 
+ MBTI: There are 16 MBTI types based on 8 cognitive functions (Ni, Ne, Si, Se, Fi, Fe, Ti, Te). These 8 functions stand for  i**N**tuition, **S**ensing, **F**eeling, **T**hinking, and are **I**ntroverted or **E**xtraverted. Each of the 16 types has 4 functions attributed to them. The first function is the dominant one, the next is auxiliary, then tertiary, and last inferior. Let me provide an example:
   + ENFJ: Dominant Extroverted Feeling (Fe), Auxiliary Introverted Intuition (Ni), Teritary Extroverted Sensing (Se), Inferior Introverted Thinking (Ti)
   + ENFJ stands for Extraverted Intuition Feeling Judging, and its opposite type ISTP is Introverted Sensing Thinking Perceiving.
      + Basing MBTI types off of cognitive functions is preferred rather than using this method; I included both in this project as users on the website vote in different ways.
+ Enneagram: There are 9 enneagram types, numbered 1-9. The nine types are differentiated according to their fears. Along with an enneagram type, characters have a wing attached to it, which specifies their enneagram type further. A character can only have a preceding or succeeding number as their wing. Let me provide an example:
   + If someone is Enneagram type 2, they have a fear of being unlovable. They can have Enneagram type 1 (fear of being incorrect) or type 3 (fear of failure) as their wing, but they cannot have the other enneagram types as their wing.
+ Instinctual Variant: This test specifies what centers a person, and has primary and secondary components. There are three types: so is social, sx is sexual (one on one), and sp is self-preserving. Let me provide an example:
   + A character has so/sx as their instinctual variant. They are primarily socially focused, and secondarily focused on one on one relationships. They do not have sp in their instinctual variant, so they do not center around self-preservation.
   + This test also can be interpreted together with the Enneagram test; two people may have the same instinctual variant, but due to different enneagram types, they may seem to be different from each other.
+ Tritype: This test goes hand in hand with the Enneagram test. A tritype has three Enneagram numbers, and each one corresponds to a Gut, Head, and Heart type. Enneagrams 2, 3, and 4 correspond to the Heart. Enneagrams 5, 6, and 7 correspond to the Head. 8, 9, and 1 correspond to the Gut. It is customary to put the person's Enneagram number first. Let me provide an example:
   + A character has 215 as their tritype. Their main Enneagram is 2, and that is their Heart type. 1 is their Gut type, and 5 (fear of being overwhelmed by need) is their Head type.
+ Socionics: Like the MBTI test, this test is based around functions, but they are defined differently than for MBTI. The functions have 8 possible places instead of 4, as in the MBTI test. The three letters in someone's socionics type have different meanings. This test is more specific and difficult to understand than the others, so I will only include what is important to know for this project. Let me provide an example:
   + A character has EIE as their socionics type. Their leading function is Fe, which focuses on others' emotions. This is suggested due to the first letter of their type being E (for emotion), the second I (intuition) and the last letter being E (extraverted).
+ Big 5: This test gives someone a 5 Letter result, corresponding to the categories of Extraversion, Emotional Stability, Orderliness, Accommodation, and Intellect. Let me provide examples:
   + SCOEI: Extraversion: Social, Emotional Stability: Calm, Orderliness: Organized, Accommodation: Egocentric, Intellect: Inquisitive
   + RLUAN: Extraversion: Reserved, Emotional Stability: Limbic, Orderliness: Unorganized, Accommodation: Agreeable, Intellect: Non-inquisitive
+ Attitudinal Psyche: This personality test is composed of four letters and their positions give insight onto a person's attitude. The four letters are Emotion (E), Physics (F), Logic (L), and Volition (V). The first position is confident, second is flexible, third is insecure, and fourth is unbothered. Let me provide an example:
   + VELF: Confident Volition suggests this person is goal-oriented, Flexible Emotions suggests this person is comfortable talking about emotion with others, Insecure Logic suggests they overanalyze and are sensitive to criticism, and Unbothered Physics suggests they are unattached to the physical world.
+ Temperament: This personality test is also composed of four letters: Phlegmatic (P), Melancholic (M), Sanguine (S), and Choleric (C). The letters correspond to personality traits. Some characters only have one letter as that temperament is dominant for them, while others have two since they have a mix of those in their character. The first letter is more dominant than the second. Let me provide examples:
   + PC: Phlegmatic-Choleric, mainly relaxed and seeks cooperation, with some irritability and stubbornness. 

## Files in Project
+ [top.csv](docs/top.csv): data file of the top 250 characters <br />
+ [top250.py](docs/top250.py): python file analyzing the characters' personality types visually
+ [mcode.py](docs/mcode.py): python file with code that takes personality types as an input and outputs the characters that match most with the inputs (think of it as a fun quiz :) ) <br />
+ [MBTIDashboard.pdf](docs/MBTIDashboard.pdf): a dashboard created from the data in Google Sheets using pivot tables and charts <br />
