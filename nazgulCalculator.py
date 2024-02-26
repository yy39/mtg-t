import pyautogui

test = pyautogui.prompt(text='Number of nonToken Nazgul', title='Test' , default='')
numOf = {
  'nonToken': 0,
  'Token': 0,
  'tokenDoubler': 0,
  'counterDoubler': 0
}

def validateInput(input):
    try:
        print(input)
    except:
        print(input)

print(test)