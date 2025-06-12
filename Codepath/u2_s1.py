
# PROBLEM 1: Festival Lineup

# Given two lists of strings artists and set_times of length n, write a function lineup() that maps each artist to their set time.
# An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).

from itertools import count
from math import floor
from typing import Counter


def lineup(artists, set_times):
    return {artist: time for artist, time in zip(artists, set_times)}

def lineup(artists, set_times):
    shows = {}

    for i in range(len(artists)):
        shows[artists[i]] = set_times[i]
    
    return shows

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print("\t Problem 1")
print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))
print("\n")


# PROBLEM 2: Planning App

# You are designing an app for your festival to help attendees have the best experience possible! As part of the application, users will be able to easily search their favorite artist and find out the day, time, and stage the artist is playing at. Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping artist's names to dictionaries containing the day, time, and stage they are playing on. Return the dictionary containing the information about the given artist.

# If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.

def get_artist_info(artist, festival_schedule):
    return festival_schedule.get(artist, "Artist not found")

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print("\t Problem 2")
print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  
print("\n")

# PROBLEM 3: Ticket Sales
# A dictionary ticket_sales is used to map ticket type to number of tickets sold. Return the total number of tickets of all types sold.

def total_sales(ticket_sales):
    return sum(ticket_sales.values())

def total_sales(ticket_sales):
    total = 0

    for ticket in ticket_sales:
        total += ticket_sales[ticket]
    
    return total

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print("\t Problem 3")
print(total_sales(ticket_sales))
print("\n")


# PROBLEM 4: Scheduling Conflict

# Demand for your festival has exceeded expectations, so you're expanding the festival to span two different venues. Some artists will perform both venues, while others will perform at just one. To ensure that there are no scheduling conflicts, implement a function identify_conflicts() that accepts two dictionaries venue1_schedule and venue2_schedule each mapping the artists playing at the venue to their set times. Return a dictionary containing the key-value pairs that are the same in each schedule.

def identify_conflicts(venue1_schedule, venue2_schedule):
    # keys() returns a set-like view of the keys. & on two sets means intersection and gives you all elements that are in both sets. So only iterating over keys in both sets
    # and is a boolean. v1.keys() and v2.keys() would evaluate to v2.keys() if v1.keys() is “truthy” (non-empty object). Just checks if both contain something
    # if artist in v1 and there's something in v2 then its true
    return {artist: venue1_schedule[artist] for artist in venue1_schedule.keys() & venue2_schedule.keys() if venue1_schedule[artist] == venue2_schedule[artist]}

def identify_conflicts(venue1_schedule, venue2_schedule):
    conflicts = {}

    for artist in venue1_schedule:
        if venue1_schedule.get(artist) == venue2_schedule.get(artist):
            conflicts[artist] = venue1_schedule.get(artist)

    return conflicts

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print("\t Problem 4")
print(identify_conflicts(venue1_schedule, venue2_schedule))
print("\n")

# PROBLEM 5: Best Set

# As part of the festival, attendees cast votes for their favorite set. Given a dictionary votes that maps attendees id numbers to the artist they voted for, return the artist that had the most number of votes. If there is a tie, return any artist with the top number of votes.

def best_set(votes):
    # counts the votes each artist got: Counter({'SZA': 3, 'Ethel Cain': 2, 'Yo-Yo Ma': 1}))
    counter = Counter(votes.values())
    # most_common() returns n most common in a list [(artist, vote_count)]
    return counter.most_common(1)[0][0]

def best_set(votes):
    freq = {}
    best = ""
    biggest = 0

    for artist in votes.values():
        freq[artist] = 1 + freq.get(artist, 0)
        # best = this artist if artist's vote count is equal to the highest vote count else its just what best was previously
        best = artist if freq[artist] == max(freq.values()) else best
    
        # if freq[artist] > biggest:
        #     best = artist

    return best


votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print("\t Problem 5")
print(best_set(votes1))
print(best_set(votes2))
print("\n")

# PROBLEM 6: Performances with Maximum Audience

# You are given an array audiences consisting of positive integers representing the audience size for different performances at a music festival.
# Return the combined audience size of all performances in audiences with the maximum audience size.
# The audience size of a performance is the number of people who attended that performance.

def max_audience_performances(audiences):
    biggest = max(audiences)
    return sum(size for size in audiences if size == biggest)


audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print("\t Problem 6")
print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
print("\n")

# PROBLEM 7: Performances with Maximum Audience II

# If you used a dictionary as part of your solution to max_audience_performances() in the previous problem, try reimplementing the function without using a dictionary. If you implemented max_audience_performances() without using a dictionary, try solving the problem with a dictionary.

# Once you've come up with your second solution, compare the two. Is one solution better than the other? Why or why not?

# First solution is better in terms of time and space, theres only two passes for the max and sum functions so 2 x O(n) and less extra space without the dictionary
# Second solution requires three runs to get the frequency, and for the max functions 3 x O(n). And used more space for the dictionary

def max_audience_performances(audiences):
    freq = {}

    for size in audiences:
        freq[size] = freq.get(size, 0) + 1
    
    return max(audiences) * freq[max(audiences)]
    
audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print("\t Problem 7")
print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
print("\n")

# PROBLEM 8: Popular Song Pairs
# Given an array of integers popularity_scores representing the popularity scores of songs in a music festival playlist, return the number of popular song pairs.

# A pair (i, j) is called popular if the songs have the same popularity score and i < j.

# Hint: number of pairs = (n x n-1)/2

def num_popular_pairs(popularity_scores):
    counter = Counter(popularity_scores)
    pairs = 0

    for score in counter.values():
        pairs += (score * (score - 1)) // 2 

    return pairs

def num_popular_pairs(popularity_scores):
    counter = Counter(popularity_scores)
    return sum((count * (count - 1) // 2) for count in counter.values()) 

def num_popular_pairs(popularity_scores):
    freq = {}
    pairs = 0

    for score in popularity_scores:
        freq[score] = freq.get(score, 0) + 1

    for count in freq.values():
        pairs += count * (count - 1) // 2

    return pairs


popularity_scores1 = [1, 2, 3, 1, 1, 3] # Counter({1: 3, 3: 2, 2: 1})
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print("\t Problem 8")
print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3)) 
print("\n")

# PROBLEM 9: Stage Arrangement Difference Between Two Performances

# You are given two strings s and t representing the stage arrangements of performers in two different performances at a music festival, such that every performer occurs at most once in s and t, and t is a permutation of s.

# The stage arrangement difference between s and t is defined as the sum of the absolute difference between the index of the occurrence of each performer in s and the index of the occurrence of the same performer in t.

# Return the stage arrangement difference between s and t.

# A permutation is a rearrangement of a sequence. For example, [3, 1, 2] and [2, 1 , 3] are both permutations of the list [1, 2, 3].

# Hint: Absolute value function

def find_stage_arrangement_difference(s, t):
    """
    :type s: List[str]
    :type t: List[str]
    :rtype: int
    """
    total_difference = 0

    # map each performer in s to their index
    index_in_s = {performer: i for i, performer in enumerate(s)}
    
    # sum up absolute differences between s-index and t-index
    for i, performer in enumerate(t):
        j = index_in_s[performer]
        total_difference += abs(i - j)
    
    return total_difference

s1 = ["Alice", "Bob", "Charlie"]  # {Alice: 0, Bob: 1, Charlie: 2}
t1 = ["Bob", "Alice", "Charlie"]  # {Bob: 0, Alice: 1, Charlie: 2}
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

print("\t Problem 9")
print(find_stage_arrangement_difference(s1, t1))
print(find_stage_arrangement_difference(s2, t2))
print("\n")

# PROBLEM 10: VIP Passes and Guests

# You're given strings vip_passes representing the types of guests that have VIP passes, and guests representing the guests you have at the music festival. Each character in guests is a type of guest you have. You want to know how many of the guests you have are also VIP pass holders.

# Letters are case sensitive, so "a" is considered a different type of guest from "A".

# Here is the pseudocode for the problem. Implement this in Python and explain your implementation step-by-step.

# 1. Create an empty set called vip_set.
# 2. For each character in vip_passes, add it to vip_set.
# 3. Initialize a counter variable to 0.
# 4. For each character in guests:
#    * If the character is in vip_set, increment the count by 1.
# 5. Return the count.

def num_VIP_guests(vip_passes, guests):
    vip_set = set(vip_passes) 
    count = 0

    for guest in guests:
        if guest in vip_set:
            count += 1

    return count

vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print("\t Problem 10")
print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))
print("\n")


# PROBLEM 11: Performer Schedule Pattern

# Given a string pattern and a string schedule, return True if schedule follows the same pattern. Return False otherwise.

# Here, "follow" means a full match, such that there is a one-to-one correspondence between a letter in pattern and a non-empty word in schedule.

# You are provided with a partially implemented and buggy version of the solution. Identify and fix the bugs in the code. Then, perform a thorough code review and suggest improvements.

def schedule_pattern(pattern, schedule):
    genres = schedule.split()

    if len(genres) != len(pattern):
        return False

    char_to_genre = {}
    genre_to_char = {}

    for char, genre in zip(pattern, genres):
        if char in char_to_genre:
            if char_to_genre[char] != genre:
                return False
        else:
            char_to_genre[char] = genre

        if genre in genre_to_char:
            if genre_to_char[genre] != char:
                return False
        else:
            genre_to_char[genre] = char

    return True


pattern1 = "abba"
schedule1 = "rock jazz jazz rock"

pattern2 = "abba"
schedule2 = "rock jazz jazz blues"

pattern3 = "aaaa"
schedule3 = "rock jazz jazz rock"

print("\t Problem 11")
print(schedule_pattern(pattern1, schedule1))
print(schedule_pattern(pattern2, schedule2))
print(schedule_pattern(pattern3, schedule3))
print("\n")


# PROBLEM 12: Sort the Performers

# You are given an array of strings performer_names, and an array performance_times that consists of distinct positive integers representing the performance durations in minutes. Both arrays are of length n.

# For each index i, performer_names[i] and performance_times[i] denote the name and performance duration of the ith performer.

# Return performer_names sorted in descending order by the performance durations.

def sort_performers(performer_names, performance_times):
    """
    :type performer_names: List[str]
    :type performance_times: List[int]
    :rtype: List[str]
    """

    # pair each name with its time
    paired = list(zip(performance_times, performer_names))

    # sort by time descending
    paired.sort(reverse=True)

    # extract the names in sorted order, _, name means don't return the other value in the pairing
    return [name for _, name in paired]


performer_names1 = ["Mary", "John", "Emma"] # [(Mary, 180), (Emma, 170), (John, 165)]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

print("\t Problem 12")
print(sort_performers(performer_names1, performance_times1)) 
print(sort_performers(performer_names2, performance_times2))
print("\n")


