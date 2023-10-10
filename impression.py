import win32print
import win32ui
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfFileReader

def imprimer_pdf():
    # Sélectionner l'imprimante par défaut
    printer_name = win32print.GetDefaultPrinter()

    # Ouvrir l'imprimante
    printer_handle = win32print.OpenPrinter(printer_name)
    printer_info = win32print.GetPrinter(printer_handle, 2)

    # Configurer l'impression
    printer_info['pDatatype'] = 'RAW'

    # Commencer l'impression
    win32print.StartDocPrinter(printer_handle, 1, ("Document PDF", None, "RAW"))
    win32print.StartPagePrinter(printer_handle)

    # Ouvrir le fichier PDF sélectionné
    selected_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_file = open(selected_file, "rb")
    pdf_data = pdf_file.read()

    # Imprimer le contenu du PDF
    win32print.WritePrinter(printer_handle, pdf_data)

    # Terminer l'impression
    win32print.EndPagePrinter(printer_handle)
    win32print.EndDocPrinter(printer_handle)
    win32print.ClosePrinter(printer_handle)

    # Fermer le fichier PDF
    pdf_file.close()

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Imprimer un fichier PDF")

# Créer un bouton pour sélectionner le fichier PDF
select_button = tk.Button(root, text="Sélectionner un fichier PDF", command=imprimer_pdf)
select_button.pack(padx=20, pady=20)

# Lancer la boucle principale de l'interface graphique
root.mainloop()
