# mangopdf_solved and use for CIA KRYPTOS

The python code to solve mango pdf challenge with added upper case conversion is shown as example.

I want to take this same method and try to solve the remaining Kryptos CIA challenge by using the first letter of every word in the oxford english dictionary, the range of the words would be from 5 characters and up, this would save the computation of millions of iterations and instead bring the number of culculation of words to use to less than 200,000 (estimate).  
For example, a word like "pneumoencephalography" has 21 characters, but there are not 5.1813187e+29 (<<--extremely big number) words in the dictionary, because running a word generator we would have to calculate the permutations of every letter in the alphabet, to the power of the number of characters, in this case "21", but since the words used in the encryption of kryptos are in the english language, we can safely assume that we only need to cross-reference less than 200,000 set of words against the key.  

notes:  

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

