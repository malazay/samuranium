class Logger:
  def __init__(self, log_level='debug'):
    self.log_level = log_level
    pass

  def log(self, msg):
    print(msg)

  def debug(self, msg):
    print(msg)

  def error(self, msg, error=None):
    print("----------------------------------------------------")
    print("An error has occurred: {}".format(msg))
    print("----------------------------------------------------")
    if error:
      print("Error output: {}".format(error))
      print("----------------------------------------------------")