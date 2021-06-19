def return_settings():
    dgroups_key_binder = None
    dgroups_app_rules = []
    main = None
    follow_mouse_focus = True
    bring_front_click = True
    cursor_warp = False
    auto_fullscreen = True
    focus_on_window_activation = "smart"
    wmname = "LG3D"
    return dgroups_key_binder, dgroups_app_rules, main, follow_mouse_focus, bring_front_click, cursor_warp, auto_fullscreen, focus_on_window_activation, wmname

def getSettings():
    return return_settings() 