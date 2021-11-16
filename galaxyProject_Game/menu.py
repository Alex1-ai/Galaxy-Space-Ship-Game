from kivy.uix.relativelayout import RelativeLayout


class MenuWidget(RelativeLayout):

    def on_touch_down(self, touch):
       if self.opacity == 0:
           return False

        # so that when you click on the start game it can respond
       return super(RelativeLayout, self).on_touch_down(touch)