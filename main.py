def count_words(text):
    words = text.split()
    print(f"The total words in the text is: {len(words)}")

def count_characters(text):
    character_dict = {}
    lower_text = text.lower()

    for letter in lower_text:
        if letter.isalpha():
            character_dict[letter] = character_dict.get(letter, 0) + 1
            
    return character_dict

def generate_report(text):
    sorted_characters = sorted(count_characters(text).items(), key=lambda x: x[1], reverse=True)
    
    print("--- Generated report for books/Frankenstein.txt ---")
    count_words(text)
    
    for character, count in sorted_characters:
        print(f"Character {character} found {count} times")
        
    print("--- End of report ---")
    
def main():
    with open("./books/Frankenstein.txt", 'r') as file:
        text = file.read()
        generate_report(text)
        
main()