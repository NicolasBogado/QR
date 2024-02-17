"""VERSION para generar codigo qr de paginas web"""

import tkinter as tk
from tkinter import messagebox
import qrcode

def generate_qr():
    # Obtener la URL ingresada por el usuario
    url = url_entry.get().strip()
    if url:
        # Generar el código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Crear una imagen del código QR
        img = qr.make_image(fill_color="black", back_color="white")

        # Guardar la imagen
        img.save("qr_code.png")

        # Mostrar mensaje de éxito
        result = messagebox.askquestion("Código QR generado", f"Se ha generado el código QR para la URL: {url}. ¿Desea generar otro código QR?")
        
        # Verificar la respuesta del usuario
        if result == 'yes':
            # Limpiar la entrada para un nuevo QR
            url_entry.delete(0, 'end')
        else:
            # Salir de la aplicación
            root.destroy()
    else:
        messagebox.showerror("Error", "Por favor, introduce una URL")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Generador de Código QR")

# Configuración del contenedor principal
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack()

# Etiqueta y entrada para la URL
url_label = tk.Label(main_frame, text="URL:")
url_label.grid(row=0, column=0, sticky="w")
url_entry = tk.Entry(main_frame, width=30)
url_entry.grid(row=0, column=1, padx=10, pady=5)

# Botón para generar el código QR
generate_button = tk.Button(main_frame, text="Generar Código QR", command=generate_qr)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
root.mainloop()
