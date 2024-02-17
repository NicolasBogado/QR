import tkinter as tk
from tkinter import messagebox
import qrcode

def generate_qr():
    username = username_entry.get().strip()
    if username:
        # URL base de Instagram
        base_url = 'https://www.instagram.com/'
        # URL completa
        instagram_url = f"{base_url}{username}"
        
        # Generar el código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(instagram_url)
        qr.make(fit=True)

        # Crear una imagen del código QR
        img = qr.make_image(fill_color="black", back_color="white")

        # Guardar la imagen
        img.save(f"{username}_instagram_qr.png")

        # Mostrar mensaje de éxito
        result = messagebox.askquestion("Código QR generado", f"Se ha generado el código QR para la cuenta de Instagram: @{username}. ¿Desea generar otro código QR?")
        
        # Verificar la respuesta del usuario
        if result == 'yes':
            # Limpiar la entrada para un nuevo usuario
            username_entry.delete(0, 'end')
        else:
            # Salir de la aplicación
            root.destroy()
    else:
        messagebox.showerror("Error", "Por favor, introduce un nombre de usuario de Instagram")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Generador de Código QR para Instagram")

# Configuración del contenedor principal
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack()

# Etiqueta y entrada para el nombre de usuario de Instagram
username_label = tk.Label(main_frame, text="Nombre de usuario de Instagram:")
username_label.grid(row=0, column=0, sticky="w")
username_entry = tk.Entry(main_frame, width=30)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Botón para generar el código QR
generate_button = tk.Button(main_frame, text="Generar Código QR", command=generate_qr)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
root.mainloop()
