

# Challange 12

'''

⚔️ Challenge 12: The Mountain Peak Finder
🧠 Problem:
    1. Given a list of integers representing altitudes (like a mountain range), find the peak elements — numbers that are greater than both of their neighbors.
        Then determine:
            - How many peaks exist.
            - The highest peak value.
            - The index of that highest peak.
'''

def find_peaks(altitudes: list[int]) -> dict:
    peaks = []
    found_peaks = {}
    count = 0
    for i in range(len(altitudes)):
        if not i-1 < 0 and not i+1 >= len(altitudes):
            if altitudes[i] > altitudes[i-1] and altitudes[i] > altitudes[i+1]:
                peaks.append(altitudes[i])
                count += 1

    highest_peak = max(peaks)
    found_peaks["peaks"] = peaks
    found_peaks["count"] = count
    found_peaks["highest_peak"] = highest_peak
    found_peaks["highest_index"] = altitudes.index(highest_peak)

    return found_peaks

print(find_peaks([2, 5, 3, 6, 8, 6, 4, 10, 7, 5, 11, 3]))