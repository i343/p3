# from nicegui import ui

# chat_log = ui.column()

# def send_message():
#     msg = input_box.value
#     if msg:
#         chat_log.clear()
#         messages.append(f'Вы: {msg}')
#         messages.append(f'Бот: {msg[::-1]}')
#         for m in messages:
#             chat_log.label(m)
#         input_box.value = ''

# messages = []
# input_box = ui.input(on_change=send_message)
# ui.run()

# from nicegui import ui

# messages = []

# chat_log = ui.column()

# def send_message():
#     msg = input_box.value
#     if msg:
#         messages.append(f'Вы: {msg}')
#         messages.append(f'Бот: {msg[::-1]}')
#         chat_log.clear()
#         for m in messages:
#             chat_log.add(ui.label(m))
#         input_box.value = ''

# input_box = ui.input(on_change=send_message)
# ui.run()


# from nicegui import ui

# messages = []

# chat_log = ui.column()

# def send_message():
#     msg = input_box.value
#     if msg:
#         messages.append(f'Вы: {msg}')
#         messages.append(f'Бот: {msg[::-1]}')
#         chat_log.clear()  # Очистить все дочерние элементы
#         for m in messages:
#             ui.label(m, parent=chat_log)  # Создаем label внутри chat_log
#         input_box.value = ''

# input_box = ui.input(on_change=send_message)

# ui.run()

# from nicegui import ui

# # Create chat log as a column
# chat_log = ui.column().classes('w-full h-64 overflow-y-auto')  # Add styling for scrollable chat

# # Create input field and send button
# input_field = ui.input('Type a message').classes('w-full')
# ui.button('Send', on_click=send_message).classes('w-full')

# async def send_message():
#     if input_field.value.strip():  # Check for non-empty input
#         with chat_log:
#             ui.label(input_field.value).classes('text-blue-600')  # Add message with styling
#         input_field.value = ''  # Clear input
#         await ui.run_javascript('window.scrollTo(0, document.body.scrollHeight)')  # Scroll to bottom

# # Run the app
# ui.run()


# from nicegui import ui

# # Create chat log as a column
# chat_log = ui.column().classes('w-full h-64 overflow-y-auto border rounded p-4 bg-gray-100')

# # Create input field
# input_field = ui.input('Type a message').classes('w-full')

# # Define send_message function
# async def send_message():
#     if input_field.value.strip():  # Check for non-empty input
#         with chat_log:
#             ui.label(f"User: {input_field.value}").classes('text-blue-600 self-end')
#         input_field.value = ''  # Clear input
#         await ui.run_javascript('window.scrollTo(0, document.body.scrollHeight)')  # Scroll to bottom

# # Create send button
# ui.button('Send', on_click=send_message).classes('w-full')

# # Run the app
# ui.run()


from nicegui import ui

# Create chat log
chat_log = ui.column().classes('w-full h-64 overflow-y-auto border rounded p-4 bg-gray-100')

# Create input field
input_field = ui.input('Type a message').classes('w-full')

# Define send_message function
async def send_message():
    if input_field.value.strip():  # Check for non-empty input
        with chat_log:
            ui.label(f"User: {input_field.value}").classes('text-blue-600 self-end')
        input_field.value = ''  # Clear input
        ui.run_javascript('window.scrollTo(0, document.body.scrollHeight)')  # Scroll without await

# Create send button
ui.button('Send', on_click=send_message).classes('w-full')

# Run the app
ui.run(port=8080)