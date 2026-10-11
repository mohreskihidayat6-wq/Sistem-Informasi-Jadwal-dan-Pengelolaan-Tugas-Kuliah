
import customtkinter as ctk
from views.pengeluaran_view import PengeluaranView


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = PengeluaranView()
    app.mainloop()
