#Question2-
#Problem Name - The Captain's Room
#HackerRank Link - https://www.hackerrank.com/challenges/py-the-captains-room/problem

#Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
#One fine day, a finite number of tourists come to stay at the hotel.
#The tourists consist of:
#→ A Captain.
#→ An unknown group of families consisting of K members per group where K ≠ 1.
#The Captain was given a separate room, and the rest were given one room per group.
#Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear K times per group except for the Captain's room.
#Mr. Anant needs you to help him find the Captain's room number.
#The total number of tourists or the total number of groups of families is not known to you.
#You only know the value of K and the room number list.


k = int(input())
rooms = list(map(int, input().split()))

room_set = set(rooms)
sum_set = sum(room_set)
sum_rooms = sum(rooms)

# Mathematical formula to find the captain's room
captains_room = (sum_set * k - sum_rooms) // (k - 1)

print(captains_room)
