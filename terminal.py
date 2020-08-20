from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.completion import WordCompleter, NestedCompleter


class BaseTerminal:

    command_list = [
        
    ]

    def __init__(self):

        completer_dict = {}

        #for commands in self.command_list:
        #    if not isinstance(commands, BaseCommand):
        #        print("ERROR")
        #    else:
        #        completer_dict.update(commands.command_choices())


    def parse_input(self,string):
        """
        parses the input string into required dictionary for further processing

        Args:
            string (String): the string containing the command

        Raises:
            Exception: Raised when empty string is provided

        Returns:
            dict: dictionary containing parsed string with corresponding keys 
        """

        import shlex

        if len(string) == 0:
            raise Exception("No string provided")

        split_str = shlex.split(string)

        string_dict = {
            'command': split_str.pop(0),
            'flags':[],
            'options': {},
            'arg':[]
        }
        
        index = 1
        while len(split_str):
            

            if split_str[0].startswith('-'):
                keyword = split_str.pop(0)

                if len(split_str):

                    if split_str[0].startswith('-'):
                    # next keyword is also option or flag
                    # thn the last was a flag
                        string_dict['flags'].append(keyword)

                    else:
                        string_dict['options'][keyword] = split_str.pop(0)
            else:
                string_dict['arg'] = split_str
                break
            index+=1

        return string_dict


    def loop(self):
        mycompleter = WordCompleter(["Hello",  "exit"], ignore_case=True)

        while True:
            data = prompt(">", completer=mycompleter)

            if data == "exit":
                break

            print(self.parse_input(data))


class BaseCommand:


    name = ""


    """
    options = {

        # The option name
        '-option_name':{

            #whether the option is compulsory 
            'required':True/False,

            #can the value of the option be just from the list
            'strict':True/False

            #default value for the option if no value is assigned to the option 
            'default':'value1',

            #list of the suggested or persmissible values
            'values':['value1', 'value2']
        }
    }
    """
    options = {}

    def __init__(self, command, options, arg):
        """Creates and holds a basic command

        Args:
            command (String): name of the command
            options_list (dict): dictionary of the options
            arguements (list): list of the arguements for the command
        """

        self.command = command
        self.options_list = options

        if self.name == '':
            self.name = self.__name__
            

        for key in options:
            if options[key] != None:
                setattr(self, key, options[key])
            else:
                self.flags.append(options[key])
             

        self.arguements = arg

    #TODO make such method later on
    @classmethod
    def command_from_string(string):
        pass

    def validity(self):
        """
        Checks the validity of the command arguements we give to the class Instance

        """

        if self.name == "":
            # TODO raise some appropriate error
            raise ValueError("No name given to the command class")

        for opt_keys in self.options:

            required = self.options[opt_keys][required]
            default = self.options[opt_keys][required]
            required = self.options[opt_keys][required]
            

            # check whether a option is compulsory or not 
            if required == True:

                if not opt_keys in self.options_list:
                    #no such option was provided
                    raise Exception("{} this option was not provided".format)
                
                else:
                    #option was provided
                


    def command(self):
        """
        Execute the command in this function
        
        """
        
        pass

    def execute(self, *args, **kwargs):
        """
        Function called when the command is called for  its function

        """
        pass

