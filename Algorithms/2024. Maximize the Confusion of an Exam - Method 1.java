// A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. 
//   He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

// You are given a string answerKey, where answerKey[i] is the original answer to the ith question. 
// In addition, you are given an integer k, the maximum number of times you may perform the following operation:
//   Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').

// Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.


class Solution {
    public int maxConsecutiveAnswers(String answerKey, int k) {
        int end = 0;
        int num_T = 0;
        int num_F = 0;
        int output = 0;

        for (int front = 0; front < answerKey.length(); front++) {
            if (answerKey.charAt(front) == 'T') {
                num_T++;
            }
            else {
                num_F++;
            }

            while (Math.min(num_F, num_T) > k) {
                output = Math.max(output, front - end);
                if (answerKey.charAt(end) == 'T') {
                    num_T--;
                }
                else {
                    num_F--;
                }
                end++;
            }
        }

        return Math.max(output, answerKey.length() - end);
    }
}
