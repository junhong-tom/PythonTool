from subprocess import check_output as Command

CommandString = r'pip freeze > requirements.txt'
Result = Command(CommandString)
print(Result.encode('cp950'))
