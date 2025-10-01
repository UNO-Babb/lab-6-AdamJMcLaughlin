#WordCount.py
#Name: Adam McLaughlin
#Date: Fall25
#Assignment: Lab06

def main():
    
    line_count = 0
    word_count = 0
    char_count = 0

    with open("gettysberg.txt", 'r') as textFile:
        for line in textFile:
            line_count += 1                    
            words_in_line = line.split()       
            word_count += len(words_in_line)   
            char_count += len(line)            

    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters:{char_count}")

if __name__ == '__main__':
    main()
