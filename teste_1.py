def retry(operation, attempts):
   for n in range(attempts):
    print(operation)
    if attempts < 4:
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")

retry("abc", 3)
retry("abcd", 5)

