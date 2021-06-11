# Recurring-Character

>11 June 2021 02:53 PM 

aespa 💆‍♀️❤️

Question v simple

***Question: Given a lowercase alphabet string s, return the index of the first recurring character in it. If there are no recurring characters, return -1.***

So I made a new list and basically add every letter from the string to it unless it's not there in the list. If it is we return the loop number i.e the i value. Some v big brain person did it by creating a set. Then they traverse through the string till a min of 27 characters have been covered. If the character is already in the set it's position is returned or else the character is added to the set. It's a way of implementing the pigeonhole principle.

``Pigeonhole Principle: The pigeonhole principle states that if n pigeons (or any other items) are placed into m holes and n>m, then at least one hole must contain more than one pigeon.``
