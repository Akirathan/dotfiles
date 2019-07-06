from i3pystatus import Status

status = Status()

status.register("clock",
    format="%a %-d.%-m. %H:%M",)

status.register("xkblayout",
	interval=0.5
	)

status.register("pulseaudio",
    format="♪{volume}")

status.register("battery",
    format="BAT {status} {percentage:.2f}% {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=35,
    status={
        "DIS": "↓",
        "CHR": "↑",
        "FULL": "=",
    })

status.register("backlight",
	format="BACKLIGHT {brightness}/{max_brightness}",
	interval=1
	)

status.register("temp",
    format="{temp:.0f}°C")

status.register("cpu_usage",
	format="CPU {usage:02}%"
	)

status.register("swap",
	format="SWAP {used:.0f}MB/{total:.0f}MB"
	)

orange_color = "#FF8000"
status.register("mem",
	format="MEM {used_mem:.0f}MB/{total_mem:.0f}MB",
	warn_percentage=80,
	alert_percentage=90,
	alert_color=orange_color,
	divisor=1024**2  #MB
	)


# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
status.register("network",
    interface="eth0",
    format_up="{v4cidr}",)

# Note: requires both netifaces and basiciw (for essid and quality)
status.register("network",
    interface="wlan0",
    format_up="{essid} {quality:03.0f}%",)

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    path="/",
    format="DISK {used}/{total}G [{avail}G]",)


# Shows mpd status
# Format:
# Cloud connected▶Reroute to Remain
status.register("mpd",
    format="{title}{status}{album}",
    status={
        "pause": "▷",
        "play": "▶",
        "stop": "◾",
    },)

status.run()

