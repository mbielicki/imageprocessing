class ApplicationError(Exception): pass

class ArgumentError(ApplicationError): pass

class UnknownArgumentError(ArgumentError): pass
class ArgumentValueError(ArgumentError): pass
class MissingArgumentError(ArgumentError): pass
class InputFileError(ArgumentError): pass

class ComparisonError(ApplicationError): pass