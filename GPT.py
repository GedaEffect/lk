from groq import Groq
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, jsonify

class GPT():
	def __init__(self):
		self.client = Groq(api_key="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")

	def gpt_message(self):
	    # Получаем сообщение от клиента
	    user_message = request.json.get('message')
	    
	    if not user_message:
	        return jsonify({'error': 'No message provided'}), 400
	    
	    # Запрос к GPT
	    try:
	        completion = self.client.chat.completions.create(
	            model="llama-3.1-70b-versatile",
	            messages=[
	                {
	                    "role": "system",
	                    "content": "ты бот помощьник для работников компании ООО Гедаэффект. Тебя Зовут GedaGPT. Гедаэффект - это инжинеринговая компани ,которая занимается автоматизацией производства."
	                },
	                {
	                    "role": "user",
	                    "content": user_message
	                }
	            ],
	            temperature=1,
	            max_tokens=1024,
	            top_p=1,
	            stream=False,
	            stop=None,
	        )
	        
	        gpt_response = completion.choices[0].message.content
	        return jsonify({'response': gpt_response.replace('\\n', '<br>')})
	    
	    except Exception as e:
	        print(e)
	        return jsonify({'error': str(e)}), 500