### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        #import hashlib
        #email = "hp1079@nyu.edu"
        #hash_value = hashlib.sha256(email.encode()).hexdigest()
        #print(hash_value)
        answer = "ef84c831db878f6d8a2409117ef1d16ee1a1bc056052c8d026f6d850d52a210f" #hp1079@nyu.edu SHA256 hash
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = 4
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = 2
    else:
        answer = "Error: Question Not Recognised"
        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue and catch errors
    #return(f"{question} \n{answer}") my code, question + answer looks cleaner.
    return answer

# Complete all the questions.
if __name__ == "__main__":
    #use this space to debug and verify that the program works
    questions = [
        "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?",
        "Are encoding and encryption the same? - Yes/No",
        "Is it possible to decrypt a message without a key? - Yes/No",
        "Is it possible to decode a message without a key? - Yes/No",
        "Is a hashed message supposed to be un-hashed? - Yes/No",
        "Is MD5 a secured hashing algorithm? - Yes/No",
        "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number",
        "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"
        #"Error Test Question"
    ]

    for q in questions:
        print(q)
        print("Answer:", welcome_assignment_answers(q))
        print("-" * 125)

#Questions:
#Q1: "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
#Q1A: Secret Passphrase: pcap
#Q2: "Are encoding and encryption the same? - Yes/No":
#Q2A: No. Encoding algorithms seldom use a key, encryption algos almost always do.
#Q3: "Is it possible to decrypt a message without a key? - Yes/No":
#Q3A: No. Encryption and decryption are both done via key (symmetric or asymmetric) pairs. Without the key/keys, it's virtually impossible to decrypt.
#Q4: "Is it possible to decode a message without a key? - Yes/No":
#Q4A: Yes. Encoding means that the algorithm being used is public knowledge, so it can be brute forced/rainbow tabled if some sort of plaintext is known/deciphered.
#Q5: "Is a hashed message supposed to be un-hashed? - Yes/No":
#Q5A: No. Hashing is a 1 way function that can't be reversed, it is complemented via salting or peppering to secure passwords/sensitive information even more.
#Q6: "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
#Q6A: "ef84c831db878f6d8a2409117ef1d16ee1a1bc056052c8d026f6d850d52a210f", double-checked with a mini script and a SHA 256 generator on Google.
#Q7: "Is MD5 a secured hashing algorithm? - Yes/No":
#Q7A: No. MD5 is prone to collisions- which makes it unsecure.
#Q8: "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
#Q8A: 4, really trying to understand the TCP/IP model since I understand the OSI model more.
#Q9: "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
#Q9A: 2, really trying to understand the TCP/IP model since I understand the OSI model more.