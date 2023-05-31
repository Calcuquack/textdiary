# textdiary
A Python script which retrieves entries from a simply-formatted text file diary.
## Requirements
You must have Python 3 installed for this to work.
## Usage
To begin, drag the ```textdiary.py``` script into the same folder as your text files. Then, navigate to the folder using Terminal and run the script with ```python textdiary.py``` or ```python3 textdiary.py```. 
## Diary Format
This entry retriever only works with a specific yet simple format. Text files are divided into directories similar to file systems. Here is a sample document in the correct format for retrieval:
```
[part1]
(entry1)
Test!
[[subentry1]]
This text is within subentry1, which is in turn located within entry1.
[[subentry2]]
This is another sentence enclosed within entry1, but is also inside subentry2.
(entry2)
This is entry 2!
[part2]
(entry1)
Another test!
```
To access the entirety of ```part1```, simply type in ```part1``` when prompted for the nesting of the entry. If, however, you want to access only a subdivison of ```entry1``` titled ```subentry1```, you must type in ```part1/subentry1``` when prompted. As you can see, subdivisons are preceeded by a separate line consisting solely of a title surrounded by parentheses, the shape and number of which determine the nesting level. Below is a chart relating the nesting level with the parentheses used:
```
1 - []
2 - ()
3 - [[]]
4 - (())
```
For deeper nesting, simply continue the pattern, adding 1 layer of parentheses for every 2 layers deep of nesting.
