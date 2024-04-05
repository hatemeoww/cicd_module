import os

def count(file_path: str) -> tuple[int, int]:
    """
    This function reads the content stored in .txt file and returnes the number of words and sentences in file

    Args: file_path: Path to the .txt file

    Returns: Tuple: number of words (int) and number of sentences (int)
    """
    try:
        with open(file_path, "r") as file:
            text = file.read()
            words = 0
            sentences = 0

            for word in text.split():
                if word:
                    words += 1

            for punct in [".","!","?", "..."]:
                sentences += text.count(punct)

            return words,  sentences
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error: ", e)

def main():
    file_path = os.path.join("text.txt") #get file path

    word_count, sentence_count = count(file_path) #count words and sentences
    
    if word_count is not None and sentence_count is not None: 
        file = open('result.txt', 'w')
        file.write(f"Number of words: {word_count}\nNumber of sentences: {sentence_count}")
        file.close()
    else:
        print("File is empty!")
        
if __name__ == "__main__":
    main()