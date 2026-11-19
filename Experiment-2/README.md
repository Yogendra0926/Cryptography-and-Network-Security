# Experiment 2: Frequency Analysis of Classical Cipher Texts

## Aim

To perform frequency analysis on classical cipher texts using CrypTool and study their vulnerability to cryptanalysis attacks.

## Tool Required

- CrypTool 2

## Theory

Frequency analysis is a technique used to study how often each letter appears in a text. In English, letters such as E, T, A and O occur more frequently than others. Attackers can use these patterns to identify possible letters in an encrypted message.

Classical ciphers such as the Caesar cipher change letters according to a fixed rule but preserve their frequency patterns. This makes them vulnerable to frequency analysis, especially when the ciphertext is long.

## Procedure

1. Open CrypTool 2 and create a new project.
2. Add a Text Input component and enter the text `THE CAT IS ON THE MAT`.
3. Connect the input to the Frequency Test component and observe the letter-frequency graph.
4. Add a Caesar cipher component and set the action to Encrypt with key `3`.
5. Connect the Caesar output to the Frequency Test component.
6. Execute the workflow and observe the frequency distribution of the encrypted text.
7. Compare the frequency patterns of the original and encrypted texts.

## Input

Plaintext: `THE CAT IS ON THE MAT`

Encryption algorithm: Caesar Cipher

Key: `3`

## Output and Observation

The Frequency Test component displays the percentage frequency of letters in the input text. After Caesar encryption, the letters change, but their frequency pattern is shifted rather than removed.

The graph shows which letters occur more frequently in the ciphertext. However, the sample text is short, so it is not sufficient for reliably identifying the original message through frequency analysis alone.

## Vulnerability Analysis

Caesar cipher is vulnerable to frequency analysis because each plaintext letter is consistently replaced by another letter. An attacker can study the frequency distribution and compare it with common English letter patterns. The attacker can also try the limited possible Caesar shifts to recover the original text.

## Result

Frequency analysis was performed successfully using CrypTool 2. The experiment demonstrated that classical substitution ciphers such as Caesar are vulnerable to cryptanalysis because they preserve letter-frequency patterns.

## Screenshots

- `screenshots/frequenc`y_test.png
- `screenshots/frequen`cy_test_caesar.png
