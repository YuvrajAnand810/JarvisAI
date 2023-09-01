import os
import openai
from config import apikey

openai.api_key = apikey
  # os.getenv("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"))


response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "Write an email to my boss for my resignation."
    },
    {
      "role": "user",
      "content": ""
    },
    {
      "role": "assistant",
      "content": "Dear [Boss's Name],\n\nI hope this email finds you well. I wanted to reach out to you to formally submit my resignation from my position at [Company Name]. It is with a heavy heart that I have made this decision, as I have thoroughly enjoyed my time here and have learned so much under your leadership.\n\nOver the past [duration of employment], I have had the privilege of working with a dedicated and talented team. I am grateful for the opportunities I have been given, the support I have received, and the knowledge I have gained during my time at [Company Name]. The challenges and experiences I have faced have contributed immensely to my professional growth and development.\n\nHowever, after careful consideration and evaluation of my career goals and personal aspirations, I have decided to explore a new opportunity that aligns more closely with my long-term objectives. This decision was not an easy one, as I value the relationships I have built within the organization and the trust you have placed in me.\n\nI would like to express my gratitude to you, [Boss's Name], for your guidance, mentorship, and support throughout my tenure at [Company Name]. Your leadership style has been an inspiration to me, and I have learned valuable lessons from you that I will carry with me throughout my career.\n\n"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

'''
{
  "id": "chatcmpl-7twwxnV4Z4FtcCytdXerfRVg03PNv",
  "object": "chat.completion",
  "created": 1693568999,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "I understand that this resignation may result in changes and adjustments within the team, and I assure you that I am committed to ensuring a smooth transition of my responsibilities. I am happy to assist in training my replacement and provide any necessary handover documentation to make the transition as seamless as possible.\n\nPlease let me know how you would like to proceed in terms of an official resignation letter and the timeline for my departure. I am more than willing to discuss this further in person or over a call, if that would be preferable for you.\n\nOnce again, I want to express my gratitude for the opportunities and experiences I have had at [Company Name]. It has been an honor to be a part of such a dynamic and supportive organization. I will always look back on my time here with fond memories and appreciation.\n\nThank you for your understanding and support during this time of transition. I hope to maintain the strong relationships I have built here and wish everyone at [Company Name] continued success.\n\nKind regards,\n\n[Your Name]"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 281,
    "completion_tokens": 201,
    "total_tokens": 482
  }
}
'''