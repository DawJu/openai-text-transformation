from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
from file_reader import file_reader


load_dotenv()

def generate_html_from_article(file_path):
    article_content = file_reader(file_path)
    if article_content == '' or article_content is None:
        return
    client = OpenAI()

    tranformation_prompt = (
        'Transform the following article into structured HTML suitable for a webpage. Use appropriate HTML tags, '
        'insert <img> tags for relevant image placeholders with src="image_placeholder.jpg" attribute and the alt attribute containing a detailed prompt that could be used for generating that image, '
        'and add captions using appropriate tags. Ensure the output includes only the content between <body> and </body>. Do not use the <body> and </body> tags or "```html ```", and keep everything in the article\'s original language.\n\n'
        f'Article:\n{article_content}'
    )

    try:
        completion = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {'role': 'system', 'content': 'You are an assistant skilled in HTML formatting.'},
                {'role': 'user', 'content': tranformation_prompt}
            ]
        )
    except OpenAIError as e:
            print(f'An error occurred with the OpenAI API: {e}')
            return

    generated_html = completion.choices[0].message.content

    output_file = 'artykul.html'
    with open(output_file, 'w', encoding='UTF-8') as f:
        f.write(generated_html)
    
    print(f'Generated HTML saved to {output_file}')

if __name__ == '__main__':
    file_path = 'text_file.txt'
    generate_html_from_article(file_path)
