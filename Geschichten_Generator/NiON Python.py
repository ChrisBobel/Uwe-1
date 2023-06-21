from flask import Flask, request, render_template
import openai

# OpenAI API Key
openai.api_key = "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"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate-story', methods=['POST'])
def generate_story():
    main_character = request.form.get('main_character')
    theme = request.form.get('theme')
    setting = request.form.get('setting')
    additional_wishes = request.form.get('additional_wishes')

    prompt = f"Du bist ein talentierter Geschichtenerzähler und deine Aufgabe ist es, eine Gute-Nacht-Geschichte zu kreieren. Die Geschichte sollte sich um die Themen Mut, Freundschaft, Opferbereitschaft, Respekt vor der Natur, Hoffnung und Ausdauer drehen. Die Geschichte sollte der Struktur der Heldenreise folgen, mit {main_character} als Hauptfigur, der sich aus seiner gewöhnlichen Welt heraus begibt, Herausforderungen und Prüfungen durchläuft, und schließlich mit neuer Weisheit oder einem Geschenk zurückkehrt. Das Thema der Geschichte ist {theme} und sie findet in {setting} statt. Zusätzliche Wünsche: {additional_wishes}.\n"
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.8,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    story = response.choices[0].text.strip()

    return render_template('generated_story.html', story=story)

if __name__ == '__main__':
    app.run(debug=True)
