# Solve last section of CIA KRYPTOS

The python code that was used to solve mango.pdf challenge with added upper case conversion is shown as an example of the type of code I would like to use for solving this, including arrays and key values to form the vigenere table.

I want to take this same method and try to solve the remaining [Kryptos](https://en.wikipedia.org/wiki/Kryptos) CIA challenge by using the first letter of every word in the oxford english dictionary, the range of the words would be from 5 characters and up, this would save the computation of millions of iterations and instead bring the number of culculation of words to use to less than 200,000 (estimate).  
For example, a word like "pneumoencephalography" has 21 characters, but there are not 5.1813187e+29 (<<--extremely big number) words in the dictionary, because running a word generator we would have to calculate the permutations of every letter in the alphabet, to the power of the number of characters, in this case "21", but since the words used in the encryption of kryptos are in the english language, we can safely assume that we only need to cross-reference less than 200,000 set of words against the key.

Explanation of how words are used to decipher the text: https://web.archive.org/web/20071116100808/http://filebox.vt.edu/users/batman/kryptos.html

Notes:  

kryptos has the encrypted/coded text as "EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJ"  
the key is "KRYPTOSABCDEFGHIJLMNQUVWXZKRYP"  
every letter on the key will be the corresponding decoded key when the corresponding row is used and pinned against the coded text  

every row has a corresponding set of letters, for example P "row" has the following letters: TOSABCDEFGHIJLMNQUVWXZKRYPTOS
using the example word deciphered PALIMPSEST, this would be a 10 letter word in the dictionary, and it would have gone against the key by taking the E from the coded text and in the "P" row of letters finding the corresponding "E" from coded text and then going up to the column of the corresponding letter which would be "B"..  
to try and explain a bit more, the "P" row has the letter "E" we want to decipher in the 9th position, you then find the 9th position letter in the "key" which is shown above, you can see that the corresponding "deciphered" letter is "B".  


if we take a 5 character word from the dictionary to use it against it, example "HELLO", that means that we take the "H" row and find the "E" on it, and however many positions it is from the beginning of the H row, we find that it is 24 positions until the "E" is found, and then the sample corresponding deciphered letter would have been "W".. this would go on for "E" and the E row with the next coded letter which is "M".. and we would do the same, and so on..  

The python code I want to do would use array and index to simply take the letter that corresponds to that index key on that row, and pull the corresponding "deciphered" letter, forming thousands of gibberish but with some of the array of words use we would eventually find a sentence that makes sense from the ciphered / coded text.. because for example as you see the word PALIMPSEST is in the dictionary and even though it would have taken a lot of iterations, at some point it would have hit on the correct word/array to be cross-referenced with the key.



CIPHER:
KRYPTOSABCDEFGHIJLMNQUVWXZKRYP


RYPTOSABCDEFGHIJLMNQUVWXZKRYPT = this would be the "R" row  
YPTOSABCDEFGHIJLMNQUVWXZKRYPTO = this would be the "Y" row  
PTOSABCDEFGHIJLMNQUVWXZKRYPTOS = this would be the "P" row... and so on..  
TOSABCDEFGHIJLMNQUVWXZKRYPTOSA  
OSABCDEFGHIJLMNQUVWXZKRYPTOSAB  
SABCDEFGHIJLMNQUVWXZKRYPTOSABC  
ABCDEFGHIJLMNQUVWXZKRYPTOSABCD  
BCDEFGHIJLMNQUVWXZKRYPTOSABCDE  
CDEFGHIJLMNQUVWXZKRYPTOSABCDEF  
DEFGHIJLMNQUVWXZKRYPTOSABCDEFG  
EFGHIJLMNQUVWXZKRYPTOSABCDEFGH  
FGHIJLMNQUVWXZKRYPTOSABCDEFGHI  
GHIJLMNQUVWXZKRYPTOSABCDEFGHIJL  
HIJLMNQUVWXZKRYPTOSABCDEFGHIJL  
IJLMNQUVWXZKRYPTOSABCDEFGHIJLM  
JLMNQUVWXZKRYPTOSABCDEFGHIJLMN  
LMNQUVWXZKRYPTOSABCDEFGHIJLMNQ  
MNQUVWXZKRYPTOSABCDEFGHIJLMNQU  
NQUVWXZKRYPTOSABCDEFGHIJLMNQUV  
QUVWXZKRYPTOSABCDEFGHIJLMNQUVW  
UVWXZKRYPTOSABCDEFGHIJLMNQUVWX  
VWXZKRYPTOSABCDEFGHIJLMNQUVWXZ  
WXZKRYPTOSABCDEFGHIJLMNQUVWXZK  
XZKRYPTOSABCDEFGHIJLMNQUVWXZKR  
ZKRYPTOSABCDEFGHIJLMNQUVWXZKRY  

<br>

Based on the following clues given by Sanborn, we can incorporate an if condition into the Python code that if one of the words found after using the vigenere method is equal to BERLIN or CLOCK, in their specific positions, we know that we have probably found the word used to decipher the text.

```
Clues given for passage 4

The Mengenlehreuhr may be the “Berlin Clock” the encrypted message references.
When commenting in 2006 about his error in passage 2, Sanborn said that the answers to the first three passages contain clues to the fourth passage.
In November 2010, Sanborn released a clue, publicly stating that "NYPVTT", the 64th–69th letters in passage four, become "BERLIN" after decryption.

Sanborn gave The New York Times another clue in November 2014: the letters "MZFPK", the 70th–74th letters in passage four, become "CLOCK" after decryption.
The 74th letter is K in both the plaintext and ciphertext, meaning that it is possible for a character to encrypt to itself.
This means it does not have the weakness, where a character could never be encrypted as itself, that was known to be inherent in the German Enigma machine.

Sanborn further stated that in order to solve passage 4, "You'd better delve into that particular clock," but added, "There are several really interesting clocks in Berlin."
The particular clock in question is presumably the Berlin Clock, although the Alexanderplatz World Clock and Clock of Flowing Time are other candidates.

In an article published on January 29, 2020, by the New York Times, Sanborn gave another clue: at positions 26–34, ciphertext "QQPRNGKSS" is the word "NORTHEAST".

In August 2020, Sanborn revealed that the four letters in positions 22–25, ciphertext "FLRV", in the plaintext are "EAST".
Sanborn commented that he "released this layout to several people as early as April". The first person known to have shared this hint more widely was Sukhwant Singh.
```

<br>

The last section (part 4) to be solved, with the included words that were given as clues to show where they currently go:<br>
![image](https://github.com/ealmonte32/mangopdf_cia_kryptos/assets/24350198/75602ce0-c246-4244-a0c5-09c9583b8406)

Complete ciphered text from part 4: <br>
![image](https://github.com/ealmonte32/mangopdf_cia_kryptos/assets/24350198/f3567a41-18f5-4a71-9dae-d93cb2fd8d0c)

