import os
import dotenv

if __name__ == '__main__':
    dotenv.load_dotenv()
    print("Hello langchain!")
    print(os.environ["OPENAI_API_KEY"])
