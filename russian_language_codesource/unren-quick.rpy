init 999 python:
  try:
    config.underlay[0].keymap['quickSave'] = QuickSave()
    config.keymap['quickSave'] = 'K_F5'
    config.underlay[0].keymap['quickLoad'] = QuickLoad()
    config.keymap['quickLoad'] = 'K_F9'
  except:
    pass
