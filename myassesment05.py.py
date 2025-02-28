# Function to count word occurrences in a file
def count_word_occurrences(file_name):
    word_count = {}
    
    # Open the file in read mode
    try:
        with open(file_name, 'r') as file:
            # Read the content of the file
            content = file.read()
            
            # Split the content into words
            words = content.split()
            
            # Count occurrences of each word
            for word in words:
                word = word.lower()  # Convert to lowercase to make it case-insensitive
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        
        # Print the word count
        for word, count in word_count.items():
            print(f"'{word}': {count}")
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")

# Input file name
file_name = input("Enter the file name: ")

# Call the function to count word occurrences
count_word_occurrences(file_name)
