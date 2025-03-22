import openai
openai.api_key = "Your_API_key"
def generate_poem(theme):
    prompt = f"Write a poem about {theme}."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0.7,
    )
    poem = response['choices'][0]['message']['content'].strip()
    return poem
def main():
    print("Welcome to the AI Poem Generator!")
    theme = input("Please enter a theme for your poem: ")
    poem = generate_poem(theme)
    print("\nHere is your poem:\n")
    print(poem)

if __name__ == "__main__":
    main()