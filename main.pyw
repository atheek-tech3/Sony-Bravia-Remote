import http.client
import json
import tkinter as tk

with open("./config.json") as config_json:
    config = json.load(config_json)

tv_ip = config["tv_ip"]
psk = config["psk"]
timeout = 60
base_url = "/sony/"
height = 790
width = 330


def rest(service_url, request):
    conn = http.client.HTTPConnection(tv_ip, timeout=timeout)
    headers = {'Content-type': 'application/json',
               'X-Auth-PSK': psk
               }
    json_data = json.dumps(request)
    conn.request('POST', base_url + service_url, json_data, headers)
    response = conn.getresponse()
    print(response.status)
    print(response.read().decode())


def ircc(code):
    service_url = "ircc"
    soapaction = "\"urn:schemas-sony-com:service:IRCC:1#X_SendIRCC\""
    conn = http.client.HTTPConnection(tv_ip, timeout=timeout)
    headers = {'Content-type': 'text/xml; charset=UTF-8',
               'X-Auth-PSK': psk,
               'SOAPACTION': soapaction
               }
    soap_data = f'''
    <s:Envelope
    xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
    s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <s:Body>
        <u:X_SendIRCC xmlns:u="urn:schemas-sony-com:service:IRCC:1">
            <IRCCCode>{code}</IRCCCode>
        </u:X_SendIRCC>
    </s:Body>
</s:Envelope>'''

    conn.request('POST', base_url + service_url, soap_data, headers)
    response = conn.getresponse()
    print(response.status)
    print(response.read().decode())




def volume_up():
    ircc(code="AAAAAQAAAAEAAAASAw==")


def volume_down():
    ircc(code="AAAAAQAAAAEAAAATAw==")


def mute():
    ircc(code="AAAAAQAAAAEAAAAUAw==")


def input():
    ircc(code="AAAAAQAAAAEAAAAlAw==")


def setApp(uri):
    service_url = "appControl"
    req = {
        "method": "setActiveApp",
        "params": [{
            "uri": uri
        }],
        "id": 602,
        "version": "1.0"
    }
    rest(service_url=service_url, request=req)


def playTV():
    setApp(uri="com.sony.dtv.com.sony.dtv.tvx.com.sony.dtv.tvx.MainActivity")


def channel_up():
    ircc(code="AAAAAQAAAAEAAAAQAw==")


def channel_down():
    ircc(code="AAAAAQAAAAEAAAARAw==")


def power():
    ircc(code="AAAAAQAAAAEAAAAVAw==")


def zero():
    ircc(code="AAAAAQAAAAEAAAAJAw==")


def one():
    ircc(code="AAAAAQAAAAEAAAAAAw==")


def two():
    ircc(code="AAAAAQAAAAEAAAABAw==")


def three():
    ircc(code="AAAAAQAAAAEAAAACAw==")


def four():
    ircc(code="AAAAAQAAAAEAAAADAw==")


def five():
    ircc(code="AAAAAQAAAAEAAAAEAw==")


def six():
    ircc(code="AAAAAQAAAAEAAAAFAw==")


def seven():
    ircc(code="AAAAAQAAAAEAAAAGAw==")


def eight():
    ircc(code="AAAAAQAAAAEAAAAHAw==")


def nine():
    ircc(code="AAAAAQAAAAEAAAAIAw==")


def play():
    ircc(code="AAAAAgAAAJcAAAAaAw==")


def confirm():
    ircc(code="AAAAAQAAAAEAAABlAw==")


def up():
    ircc(code="AAAAAQAAAAEAAAB0Aw==")


def down():
    ircc(code="AAAAAQAAAAEAAAB1Aw==")


def left():
    ircc(code="AAAAAQAAAAEAAAA0Aw==")


def right():
    ircc(code="AAAAAQAAAAEAAAAzAw==")


def options():
    ircc(code="AAAAAgAAAJcAAAA2Aw==")


def back1():
    ircc(code="AAAAAgAAAJcAAAAjAw==")


def home():
    borderwidth=5
    back = tk.Frame(master=root, width=width, height=height, bg='black')
    back.grid_propagate(0)
    back.grid(row=0, column=0)
    font = ("aerial", 13, "bold")
    font1 = ("aerial", 8, "bold")

    row = 1

    power_btn = tk.Button(master=back, text="POWER", font=font, foreground="red", borderwidth=borderwidth, command=power)
    power_btn.grid(row=row, column=1, padx=2, pady=20, ipadx=2, ipady=2)

    input_btn = tk.Button(master=back, text="INPUT", font=font1, foreground='black', borderwidth=borderwidth,  command=input)
    input_btn.grid(row=row, column=2, padx=2, pady=20, ipadx=8, ipady=2)

    play_tv_btn = tk.Button(master=back, text="TV", font=font1, foreground='black', borderwidth=borderwidth,  command=playTV)
    play_tv_btn.grid(row=row, column=3, padx=2, pady=10, ipadx=20, ipady=2)

    row = row + 1

    # spacer = tk.Label(master=back, text="", background="black")
    # spacer.grid(row=row, column=2, padx=50, pady=1)

    row = row + 1

    vol_up_btn = tk.Button(master=back, text="+", font=font, foreground="green", borderwidth=borderwidth, command=volume_up)
    vol_up_btn.grid(row=row, column=1, padx=10, pady=2, ipadx=10, ipady=6)

    mute_btn = tk.Button(master=back, text="MUTE", font=font1, foreground="black", borderwidth=borderwidth, command=mute)
    mute_btn.grid(row=row, column=2, padx=2, pady=5, ipadx=10, ipady=2)

    channel_up_btn = tk.Button(master=back, text="+", font=font, foreground="black", borderwidth=borderwidth, command=channel_up)
    channel_up_btn.grid(row=row, column=3, padx=10, pady=2, ipadx=10, ipady=6)

    row = row + 1

    vol_label = tk.Label(master=back, text="VOL", foreground='white', background="black", borderwidth=10, font=font)
    vol_label.grid(row=row, column=1, padx=2, pady=2, ipadx=6, ipady=2)


    play_btn = tk.Button(master=back, text="PAUSE", font=font1, foreground="black", borderwidth=borderwidth, command=play)
    play_btn.grid(row=row, column=2, padx=10, pady=15, ipadx=10, ipady=2)

    ch_label = tk.Label(master=back, text="CH", foreground='white', background="black", borderwidth=10, font=font)
    ch_label.grid(row=row, column=3, padx=2, pady=2, ipadx=10, ipady=2)

    row = row + 1

    vol_down_btn = tk.Button(master=back, text="-", font=font, foreground="red", borderwidth=borderwidth, command=volume_down)
    vol_down_btn.grid(row=row, column=1, padx=10, pady=2, ipadx=10, ipady=6)

    options_btn = tk.Button(master=back, text="MENU", font=font1, foreground="black", borderwidth=borderwidth, command=options)
    options_btn.grid(row=row, column=2, padx=10, pady=15, ipadx=10, ipady=2)

    channel_down_btn = tk.Button(master=back, text="-", font=font, foreground="black", borderwidth=borderwidth, command=channel_down)
    channel_down_btn.grid(row=row, column=3, padx=10, pady=2, ipadx=10, ipady=6)

    row = row + 1


    back_btn = tk.Button(master=back, text="BACK", font=font, foreground="black", borderwidth=borderwidth, command=back1)
    back_btn.grid(row=row, column=1, padx=2, pady=15, ipadx=5, ipady=2)

    row = row + 1

    up_btn = tk.Button(master=back, text="UP", font=font, foreground="blue", borderwidth=borderwidth, command=up)
    up_btn.grid(row=row, column=2, padx=10, pady=8, ipadx=13, ipady=2)

    row = row + 1

    left_btn = tk.Button(master=back, text="LEFT", font=font, foreground="red", borderwidth=borderwidth, command=left)
    left_btn.grid(row=row, column=1, padx=10, pady=2, ipadx=10, ipady=2)

    confirm_btn = tk.Button(master=back, text="OK", font=font, foreground="black", borderwidth=borderwidth, command=confirm)
    confirm_btn.grid(row=row, column=2, padx=10, pady=2, ipadx=12, ipady=2)

    right_btn = tk.Button(master=back, text="RIGHT", font=font, foreground="green", borderwidth=borderwidth, command=right)
    right_btn.grid(row=row, column=3, padx=10, pady=2, ipadx=10, ipady=2)

    row = row + 1

    down_btn = tk.Button(master=back, text="DOWN", font=font, foreground="brown", borderwidth=borderwidth, command=down)
    down_btn.grid(row=row, column=2, padx=10, pady=8, ipadx=0, ipady=2)

    row = row + 1

    spacer = tk.Label(master=back, text="", background="black")
    spacer.grid(row=row, column=2, padx=50, pady=1)
    row = row + 1

    one_btn = tk.Button(master=back, text="1", font=font, foreground="red",borderwidth=borderwidth, command=one)
    one_btn.grid(row=row, column=1, padx=10, pady=2, ipadx=30, ipady=10)

    two_btn = tk.Button(master=back, text="2", font=font, foreground="green",borderwidth=borderwidth, command=two)
    two_btn.grid(row=row, column=2, padx=10, pady=2, ipadx=30, ipady=10)

    three_btn = tk.Button(master=back, text="3", font=font, foreground="orange",borderwidth=borderwidth, command=three)
    three_btn.grid(row=row, column=3, padx=10, pady=2, ipadx=30, ipady=10)
    row = row + 1

    four_btn = tk.Button(master=back, text="4", font=font, foreground="blue",borderwidth=borderwidth, command=four)
    four_btn.grid(row=row, column=1, padx=10, pady=2, ipadx=30, ipady=10)

    five_btn = tk.Button(master=back, text="5", font=font, foreground="purple",borderwidth=borderwidth, command=five)
    five_btn.grid(row=row, column=2, padx=10, pady=2, ipadx=30, ipady=10)

    six_btn = tk.Button(master=back, text="6", font=font, foreground="magenta", borderwidth=borderwidth, command=six)
    six_btn.grid(row=row, column=3, padx=10, pady=2, ipadx=30, ipady=10)
    row = row + 1

    seven_btn = tk.Button(master=back, text="7", font=font, foreground="dark green", borderwidth=borderwidth, command=seven)
    seven_btn.grid(row=row, column=1, padx=10, pady=2, ipadx=30, ipady=10)

    eight_btn = tk.Button(master=back, text="8", font=font, foreground="dark blue", borderwidth=borderwidth, command=eight)
    eight_btn.grid(row=row, column=2, padx=10, pady=2, ipadx=30, ipady=10)

    nine_btn = tk.Button(master=back, text="9", font=font, foreground="brown", borderwidth=borderwidth, command=nine)
    nine_btn.grid(row=row, column=3, padx=10, pady=2, ipadx=30, ipady=10)
    row = row + 1

    zero_btn = tk.Button(master=back, text="0", font=font, foreground="black", borderwidth=borderwidth, command=zero)
    zero_btn.grid(row=row, column=2, padx=10, pady=2, ipadx=30, ipady=10)


root = tk.Tk()
root.title("Sony Bravia Remote")
root.iconbitmap("sony-logo.ico")
root.geometry(str(width) + "x" + str(height))
root.resizable(0, 0)
home()
tk.mainloop()
