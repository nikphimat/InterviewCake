'''
Python 3.6
Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.

Python 3.6
Do not assume the meetings are in order. The meeting times are coming from multiple teams.

'''

def merge_ranges(meetings):

    # Merge meeting ranges
    meetings.sort()
    list_length = len(meetings)
    merged_time_block = []
    i=0
    j=0
    merged_time_block.append(meetings[0])

    while(i<list_length-1):
      if merged_time_block[j][1]>= meetings[i+1][1]:
          new_time_block = (merged_time_block[j][0],merged_time_block[j][1])
          merged_time_block[j] = new_time_block
          #print(merged_time_block)
          i+=1
      elif merged_time_block[j][1]>= meetings[i+1][0]:
          new_time_block = (merged_time_block[j][0],meetings[i+1][1])
          merged_time_block[j] = new_time_block
          #print(merged_time_block)
          i+=1
      else:
          merged_time_block.append(meetings[i+1])
          #print(merged_time_block)
          i+=1
          j+=1

    return merged_time_block

