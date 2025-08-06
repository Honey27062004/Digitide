from transformers import pipeline

def main():
    print("🏥 Hospital Management System - Text Generator")

    generator = pipeline("text-generation", model="gpt2-medium")

    while True:
        prompt = input("\n🩺 Enter your hospital-related prompt (or type 'exit' to quit): ")
        if prompt.lower() == 'exit':
            print("✅ Exiting. Stay healthy!")
            break

        output = generator(
            prompt,
            max_length=200,
            num_return_sequences=1,
            repetition_penalty=1.2,
            temperature=0.8,
            top_p=0.9,
            do_sample=True
        )

        print("\n📄 Generated Response:\n")
        print(output[0]['generated_text'])
        print("\n" + "-"*100)

if __name__ == "__main__":
    main()
