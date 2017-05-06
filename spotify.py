#!/bin/env python

import dbus

try:
    session_bus = dbus.SessionBus()
    spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
    spotify_properties = dbus.Interface(spotify_bus, "org.freedesktop.DBus.Properties")
    metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")

    track = metadata['xesam:title']
    artist = metadata['xesam:artist'][0]

    if artist == "":
   
        print("Advertisement")
   
    else:

        print(artist + " - " + track)

except:

    print("No Track")

