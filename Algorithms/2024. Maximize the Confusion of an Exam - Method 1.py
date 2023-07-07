# A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. 
# He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

# You are given a string answerKey, where answerKey[i] is the original answer to the ith question. 
# In addition, you are given an integer k, the maximum number of times you may perform the following operation:
#   Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').

# Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        front = 0
        end = 0
        num_T = 0
        num_F = 0
        output = 0

        while front < len(answerKey):
            if answerKey[front] == "T":
                num_T += 1
            else:
                num_F += 1
            
            while min(num_F, num_T) > k:
                output = max(output, front - end)
                if answerKey[end] == "T":
                    num_T -= 1
                else:
                    num_F -= 1
                end += 1
            
            front += 1
        
        return max(output, front - end)
