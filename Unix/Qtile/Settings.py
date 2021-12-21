
class Settings:

    def get_settings(self) -> dict:
        return dict(
            dgroups_key_binder = None,
            dgroups_app_rules = [],
            main = None,
            follow_mouse_focus = True,
            bring_front_click = True,
            cursor_warp = False,
            auto_fullscreen = True,
            focus_on_window_activation = "smart",
            wmname = "LG3D"
        )