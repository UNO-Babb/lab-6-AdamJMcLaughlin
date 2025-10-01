#WordIndex.py
#Name: Adam McLaughlin
#Date: Fall25
#Assignment: Lab06

def main():
    filename = "fish.txt"  
    file = open(filename, "r")

    word_index = {}  
    line_number = 1  
    for line in file:
        line = line.lower().strip()  
        words = line.split()  

        for word in words:
            word = word.strip(",.!?;:")

            if word in word_index:
                if line_number not in word_index[word]:
                    word_index[word].append(line_number)  
            else:
                word_index[word] = [line_number]  

        line_number += 1 

    file.close()  

    for word in sorted(word_index.keys()):
        print(word, ":", word_index[word])

if __name__ == "__main__":
    main()
