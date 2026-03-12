def calculate_word_stats():
    text = input("Please enter your sentence or text: ")
    words = text.lower().split()
    total = len(words)
    if total == 0:
        print("You didn't enter any words!")
        return
    counts = {}
    for word in words:
        x = word.strip()
        if word: 
            counts[word] = counts.get(word, 0) + 1
    y = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    top_5 = y[:5]
    top_5_sum = sum(count for word, count in top_5)
    top_5_dict = {word: count for word, count in top_5}
    print("Results:")
    print(f"Top 5: {top_5_dict}")
    print(f"Total number of words: {total}")
    if total > 0:
        proportion = (top_5_sum / total) * 100
        print(f"Proportion of 5 most common words: {top_5_sum} / {total} = {proportion:.2f}%")

calculate_word_stats()
