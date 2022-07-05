import gokudo


ret = 0
gokudo.Write("Hello Comrade!")
dialogueOptions = ["Respond by saying 'Hello'", "Ignore Kiryu", "Slap Kiryu", "Give the Middle Finger"]
ret = gokudo.Dialogue(dialogueOptions, ret)
if ret == 0:
  gokudo.Write("You Seem Like A Nice Person!")
elif ret == 1:
  gokudo.Write("HELLO??")
  ret = gokudo.Dialogue(dialogueOptions, ret)
  if ret == 1 or ret == 2 or ret == 3:
    gokudo.Write("FUCK OFF!")
    quit()
  else:
    gokudo.Write("Great to see you!")
else:
  gokudo.Write("FUCK OFF!")
  quit()