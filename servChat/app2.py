# import gradio as gr

# def chat_func(message, history):
#     response = f"Эхо: {message}"
#     history.append((message, response))
#     return "", history

# gr.ChatInterface(fn=chat_func).launch()

# import gradio as gr

# def chat_func(message, history):
#     response = f"Бот: {message[::-1]}"  # Простой ответ, переворачивает текст
#     history.append((message, response))  # Это ок
#     return "", history  # Первый элемент — новое пустое поле ввода, второй — обновлённая история

# chat = gr.ChatInterface(fn=chat_func)
# chat.launch()


# import gradio as gr

# def chat_func(messages):
#     last_user_message = messages[-1]["content"]
#     reply = f"Ответ: {last_user_message[::-1]}"
#     messages.append({"role": "assistant", "content": reply})
#     return messages

# gr.ChatInterface(fn=chat_func, type="messages").launch()

# import gradio as gr

# def chat_fn(messages):
#     last = messages[-1]['content']
#     response = last[::-1]  # Пример — бот просто переворачивает сообщение
#     messages.append({"role": "assistant", "content": response})
#     return messages

# gr.ChatInterface(fn=chat_fn, type="messages").launch()

import gradio as gr

async def chat_fn(message: str, history: list) -> str:
    return f"Echo: {message}"

demo = gr.ChatInterface(fn=chat_fn)
demo.launch()