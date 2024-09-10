from abc import ABC, abstractmethod

# Interface Abstrak untuk Printer
class Printer(ABC):
    @abstractmethod
    def print(self, message):
        pass

# Implementasi Konkret untuk Pencetakan ke Konsol
class ConsolePrinter(Printer):
    def print(self, message):
        print(f"Console: {message}")

# Implementasi Konkret untuk Pencetakan ke File
class FilePrinter(Printer):
    def print(self, message):
        with open('output.txt', 'a') as file:
            file.write(f"File: {message}\n")

# High-Level Class yang Bergantung pada Abstraksi
class MessagePrinter:
    def __init__(self, printer: Printer):
        self.printer = printer  # Ketergantungan pada abstraksi
    
    def print_message(self, message):
        self.printer.print(message)

# Penggunaan
console_printer = ConsolePrinter()
message_printer = MessagePrinter(console_printer)
message_printer.print_message("Hello, World!")

file_printer = FilePrinter()
message_printer = MessagePrinter(file_printer)
message_printer.print_message("Hello, World!")
