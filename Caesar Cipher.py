import wx


def encrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


class CaesarCipherFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Caesar Cipher", size=(420, 320))

        panel = wx.Panel(self)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(panel, label="Caesar Cipher")
        title.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT,
                              wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        main_sizer.Add(title, 0, wx.ALIGN_CENTER | wx.TOP, 15)

        main_sizer.Add(wx.StaticText(panel, label="Enter Message:"), 0, wx.LEFT | wx.TOP, 15)
        self.message_ctrl = wx.TextCtrl(panel)
        main_sizer.Add(self.message_ctrl, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        main_sizer.Add(wx.StaticText(panel, label="Shift Value:"), 0, wx.LEFT | wx.TOP, 10)
        self.shift_ctrl = wx.TextCtrl(panel)
        main_sizer.Add(self.shift_ctrl, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        encrypt_btn = wx.Button(panel, label="Encrypt")
        decrypt_btn = wx.Button(panel, label="Decrypt")

        encrypt_btn.Bind(wx.EVT_BUTTON, self.on_encrypt)
        decrypt_btn.Bind(wx.EVT_BUTTON, self.on_decrypt)

        button_sizer.Add(encrypt_btn, 0, wx.RIGHT, 10)
        button_sizer.Add(decrypt_btn, 0)

        main_sizer.Add(button_sizer, 0, wx.ALIGN_CENTER | wx.TOP, 15)

        main_sizer.Add(wx.StaticText(panel, label="Result:"), 0, wx.LEFT | wx.TOP, 15)
        self.output_ctrl = wx.TextCtrl(panel, style=wx.TE_READONLY)
        main_sizer.Add(self.output_ctrl, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        panel.SetSizer(main_sizer)
        self.Centre()
        self.Show()

    def on_encrypt(self, event):
        try:
            message = self.message_ctrl.GetValue()
            shift = int(self.shift_ctrl.GetValue())
            self.output_ctrl.SetValue(encrypt(message, shift))
        except ValueError:
            wx.MessageBox("Shift value must be an integer",
                          "Error", wx.OK | wx.ICON_ERROR)

    def on_decrypt(self, event):
        try:
            message = self.message_ctrl.GetValue()
            shift = int(self.shift_ctrl.GetValue())
            self.output_ctrl.SetValue(decrypt(message, shift))
        except ValueError:
            wx.MessageBox("Shift value must be an integer",
                          "Error", wx.OK | wx.ICON_ERROR)


if __name__ == "__main__":
    app = wx.App(False)
    frame = CaesarCipherFrame()
    app.MainLoop()
