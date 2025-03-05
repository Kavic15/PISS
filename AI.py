import ollama

def ask_ai(type, topic, post_text, PosNeg, length, author_description):
    if type=="post":
        question = f"Write one social media post about {topic} with the length in range of {length} ± 20 characters. Author is by nature {author_description}"
    if type=="comment":
        question = f"Write one {PosNeg} social media comment to this post: {post_text}."
    response = ollama.chat(model="wizard-vicuna", messages=[{"role": "user", "content": question}])
    return response['message']['content']




def generate_pool(output_file, count, topic):
    for x in range(count):
        question = f"Write one social media post about {topic}."
        response = ollama.chat(model="wizard-vicuna", messages=[{"role": "user", "content": question}])
        answer = response['message']['content']
        print("AI generate ("+ topic +"):")
        print(answer)
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(f"{answer}")
            file.write(f"\n")
    return print("Generated "+ count + " posts about " + topic + " into: " + output_file + "")

if __name__ == "__main__":
    author_description = "average user, not too smart with slightly offensive opinions"
    topic = "NATO"  # You can modify this as needed
    length = 200  # Length of post ±20
    count = 3  # Number of posts created
    output_file = "generated_posts.txt"  # File to save the posts

    # Loop through the specified number of posts to generate
    for i in range(count):
        question = f"Write one social media post about {topic} with the length in range of {length} ± 20 characters. Author is by nature {author_description}"
        answer = ask_ai(question)
        
        # Print the AI's response to the console
        print(f"\nPost {i + 1}:\nAI says: {answer}\n")
        
        # Save the response to the file with a numbered format
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(f"{answer}")
            file.write(f"\n")

    print(f"\nAll posts have been saved to {output_file}.")