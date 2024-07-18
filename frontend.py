from nicegui import ui
import httpx

class LoginUI:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.error_message = ''

    async def login(self):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    'http://localhost:8000/api/token',
                    data={'username': self.username, 'password': self.password}
                )
                if response.status_code == 200:
                    token = response.json()['access_token']
                    ui.notify('Login successful!', type='positive')
                    # Here you can store the token and redirect to a new page
                else:
                    self.error_message = 'Invalid username or password'
            except httpx.RequestError:
                self.error_message = 'Unable to connect to the server'

    def build(self):
        with ui.card().classes('w-96'):
            ui.label('Login').classes('text-2xl mb-4')
            ui.input(label='Username', on_change=lambda e: setattr(self, 'username', e.value))
            ui.input(label='Password', password=True, on_change=lambda e: setattr(self, 'password', e.value))
            ui.button('Login', on_click=self.login)
            ui.label().bind_text_from(self, 'error_message')

login_ui = LoginUI()

def create_ui(_=None):
    login_ui.build()

if __name__ == '__main__':
    ui.run(on_load=create_ui, port=8080)