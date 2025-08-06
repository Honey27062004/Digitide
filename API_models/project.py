from transformers import pipeline

def main():
    print("🔹 Hugging Face Text Generator 🔹")
    
    generator = pipeline("text-generation", model="gpt2-medium")

    while True:
        prompt = input("\n📝 Enter your prompt (or type 'exit' to quit): ")
        if prompt.lower() == 'exit':
            print("✅ Exiting the generator. Have a great day!")
            break

        
        output = generator(
            prompt,
            max_length=150,
            num_return_sequences=1,
            repetition_penalty=1.2,   
            temperature=0.9,          
            top_p=0.95,             
            do_sample=True            
        )

        print("\n📄 Generated Output:\n")
        print(output[0]['generated_text'])
        print("\n" + "-"*80)

if __name__ == "__main__":
    main()
