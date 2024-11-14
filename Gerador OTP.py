import tkinter as tk
import random

# Função para gerar o OTP
def generate_otp():
    otp = random.randint(100000, 999999)  # Gera um OTP numérico de 6 dígitos
    otp_display.config(text=str(otp))  # Exibe o OTP gerado

# Configurações principais da janela
root = tk.Tk()
root.title("Gerador OTP")
root.geometry("400x300")
root.configure(bg="#1b76f2")

# Container principal
container = tk.Frame(root, bg="#1a1820", bd=2, relief="solid")
container.place(relx=0.5, rely=0.5, anchor="center", width=300, height=200)

# Título
title = tk.Label(
    container,
    text="Gerador OTP",
    font=("Poppins", 16, "bold"),
    fg="#ffffff",
    bg="#1a1820",
)
title.pack(pady=(20, 10))

# Display do OTP
otp_display = tk.Label(
    container,
    text="------",
    font=("Poppins", 18, "bold"),
    fg="#ffffff",
    bg="#2a292e",
    width=10,
    height=2,
)
otp_display.pack(pady=10)

# Botão de gerar OTP
generate_button = tk.Button(
    container,
    text="Gerar OTP",
    font=("Poppins", 14, "bold"),
    fg="#ffffff",
    bg="#1b76f2",
    bd=0,
    relief="flat",
    command=generate_otp,
    cursor="hand2",
)
generate_button.pack(pady=10)

# Executa o OTP ao iniciar a aplicação
generate_otp()

# Inicia a aplicação
root.mainloop()
