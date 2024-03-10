import pyautogui

numOf = {
  'nonToken': 0,
  'token': 0,
  'tokenDoubler': 0,
  'counterDoubler': 0
}

def validateInput(string: input):
    try:
        print(input)
    except:
        print(input)

def calculate(nums: dict):
    for x in nums:
        print(nums[x])

# numOf['nonToken'] = pyautogui.prompt(text='Enter number of non-token Nazguls entering', title='Enter numbers 1/4', default='')
# numOf['token'] = pyautogui.prompt(text='Enter number of token Nazguls entering', title='Enter numbers 2/4', default='')
# numOf['tokenDoubler'] = pyautogui.prompt(text='Enter number of token doublers', title='Enter numbers 3/4', default='')
# numOf['counterDoubler'] = pyautogui.prompt(text='Enter number of counter doublers', title='Enter numbers 4/4', default='')

# print(numOf)
calculate(numOf)