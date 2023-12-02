# Импорт библиотеки discord
import discord

# Создание экземпляра клиента Discord
client = discord.Client()

# Определение события on_ready, которое срабатывает при успешном подключении бота к Discord
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

# Определение события on_message, которое срабатывает при получении сообщения
@client.event
async def on_message(message):
    # Проверка, что сообщение не отправлено самим ботом
    if message.author == client.user:
        return

    # Проверка, что сообщение начинается с '!role'
    if message.content.startswith('!role'):
        # Получение имени роли из сообщения
        role_name = message.content.split(' ')[1]
        # Поиск роли по имени
        role = discord.utils.get(message.guild.roles, name=role_name)
        if role:
            # Добавление роли пользователю, отправившему сообщение
            await message.author.add_roles(role)
            # Отправка подтверждения добавления роли
            await message.channel.send(f'Роль {role_name} успешно добавлена.')
        else:
            # Отправка сообщения об ошибке, если роль не найдена
            await message.channel.send(f'Роль {role_name} не найдена.')

# Запуск бота с использованием указанного токена
client.run('токен')
