from abc import ABC


# class ConsoleOutputAbstract(ABC):
#     def output(self, text: str, *args) -> str:
#         ...

class ConsoleAbstract(ABC):
    def output(self, text: str, *args) -> str:
        ...

class TerminalOutput(ConsoleAbstract):
    def output(self, *args) -> None:
        return args[0]
			
class Commands_Handler:
    def __init__(self, command_output: ConsoleAbstract):
        self.__output_processor = command_output
        
    def print_result(self, *args) -> None:
        return self.__output_processor.output(*args)

if __name__ == "__main__":
    def print_text(text):
        print (text)

    # terminal_out = TerminalOutput()

    # terminal_handler = Commands_Handler(terminal_out)
      
    # terminal_handler.print_result(print_text("hello"), "New created terminal!")
  